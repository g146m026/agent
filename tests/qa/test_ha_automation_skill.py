import json
import subprocess
from pathlib import Path

def test_ha_automation_report_python(tmp_path):
    autos = [
        {"id": "auto_test", "alias": "Test automation", "description": "", "area_id": "", "action": [{"service": "light.turn_on", "entity_id": "light.test"}]},
    ]
    entity_registry = {"data": [{"entity_id": "light.test", "area_id": "salon"}]}
    device_registry = {"data": []}

    autos_file = tmp_path / "automations.yaml"
    entity_file = tmp_path / "core.entity_registry"
    device_file = tmp_path / "core.device_registry"
    output_file = tmp_path / "report_automations.csv"

    import yaml
    with autos_file.open("w", encoding="utf-8") as f:
        yaml.safe_dump(autos, f)
    with entity_file.open("w", encoding="utf-8") as f:
        json.dump(entity_registry, f)
    with device_file.open("w", encoding="utf-8") as f:
        json.dump(device_registry, f)

    script = Path(__file__).resolve().parents[2] / "scripts" / "ha_automation_report.py"
    result = subprocess.run([
        "python3",
        str(script),
        "--automations",
        str(autos_file),
        "--entity_registry",
        str(entity_file),
        "--device_registry",
        str(device_file),
        "--out_csv",
        str(output_file),
    ], capture_output=True, text=True)

    assert result.returncode == 0, f"Script failed: {result.stderr}"
    assert output_file.exists()

    lines = output_file.read_text(encoding="utf-8").splitlines()
    assert lines[0].startswith("automation_id,alias")
    assert any("auto_test" in line for line in lines)
