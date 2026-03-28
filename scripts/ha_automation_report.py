#!/usr/bin/env python3
"""Analyse et rapport de normalisation pour automations Home Assistant."""

from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


def load_yaml(path: Path) -> Any:
    try:
        import yaml
    except ImportError as exc:
        raise RuntimeError("PyYAML requis: pip install pyyaml") from exc
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def collect_entity_ids(obj: Any) -> List[str]:
    ids: List[str] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "entity_id" and isinstance(v, str):
                ids.append(v)
            elif isinstance(v, (dict, list)):
                ids.extend(collect_entity_ids(v))
    elif isinstance(obj, list):
        for item in obj:
            ids.extend(collect_entity_ids(item))
    return ids


def normalize_automation(item: Dict[str, Any], entity_map: Dict[str, str], device_map: Dict[str, str]) -> Dict[str, Any]:
    autom = {
        "id": item.get("id", ""),
        "alias": item.get("alias", ""),
        "description": item.get("description", ""),
        "area_id": item.get("area_id", ""),
        "entity_ids": [],
        "area_from_registry": "",
        "needs_description": False,
        "needs_area": False,
    }

    if autom["id"] == "" and "alias" in item:
        autom["id"] = item.get("alias", "")

    entity_ids = collect_entity_ids(item)
    autom["entity_ids"] = sorted(set(entity_ids))

    if autom["area_id"]:
        autom["area_from_registry"] = autom["area_id"]
    else:
        for eid in autom["entity_ids"]:
            if eid in entity_map:
                autom["area_from_registry"] = entity_map[eid]
                break
            if eid in device_map:
                autom["area_from_registry"] = device_map[eid]
                break

    autom["needs_description"] = (not bool(str(autom["description"]).strip()))
    autom["needs_area"] = (not bool(str(autom["area_id"]).strip()) or not bool(str(autom["area_from_registry"]).strip()))
    return autom


def build_maps(entity_registry: Dict[str, Any], device_registry: Dict[str, Any]) -> Tuple[Dict[str, str], Dict[str, str]]:
    entity_map: Dict[str, str] = {}
    device_map: Dict[str, str] = {}

    for ent in entity_registry.get("data", []):
        e = ent.get("entity_id")
        a = ent.get("area_id")
        if e and a:
            entity_map[e] = a

    for dev in device_registry.get("data", []):
        d = dev.get("id")
        a = dev.get("area_id")
        if d and a:
            device_map[d] = a

    return entity_map, device_map


def generate_csv(automations: List[Dict[str, Any]], out_path: Path) -> None:
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["automation_id", "alias", "description", "area_id", "area_from_registry", "needs_description", "needs_area", "entity_ids"],
        )
        writer.writeheader()
        for a in automations:
            row = {
                "automation_id": a.get("id", ""),
                "alias": a.get("alias", ""),
                "description": a.get("description", ""),
                "area_id": a.get("area_id", ""),
                "area_from_registry": a.get("area_from_registry", ""),
                "needs_description": a.get("needs_description", ""),
                "needs_area": a.get("needs_area", ""),
                "entity_ids": ";".join(a.get("entity_ids", [])),
            }
            writer.writerow(row)


def main() -> int:
    parser = argparse.ArgumentParser(description="Rapport HA Automations normalization")
    parser.add_argument("--automations", default="automations.yaml")
    parser.add_argument("--entity_registry", default=".storage/core.entity_registry")
    parser.add_argument("--device_registry", default=".storage/core.device_registry")
    parser.add_argument("--out_csv", default="report_automations.csv")
    args = parser.parse_args()

    automations_path = Path(args.automations)
    entity_path = Path(args.entity_registry)
    device_path = Path(args.device_registry)
    out_csv = Path(args.out_csv)

    if not automations_path.exists():
        raise FileNotFoundError(f"{automations_path} introuvable")

    autos = load_yaml(automations_path)
    if not isinstance(autos, list):
        raise ValueError("automations.yaml doit être une liste de dicts")

    entity_registry = load_json(entity_path) if entity_path.exists() else {"data": []}
    device_registry = load_json(device_path) if device_path.exists() else {"data": []}

    entity_map, device_map = build_maps(entity_registry, device_registry)

    results: List[Dict[str, Any]] = []
    for item in autos:
        if not isinstance(item, dict):
            continue
        results.append(normalize_automation(item, entity_map, device_map))

    generate_csv(results, out_csv)

    # print summary
    n = len(results)
    missing_desc = sum(1 for r in results if r["needs_description"])
    missing_area = sum(1 for r in results if r["needs_area"])
    print(f"Automations analysées: {n}")
    print(f"Descriptions manquantes: {missing_desc}")
    print(f"Area manquante: {missing_area}")
    print(f"Rapport généré: {out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
