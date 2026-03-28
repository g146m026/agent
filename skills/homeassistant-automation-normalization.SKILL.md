---
name: homeassistant-automation-normalization
summary: "Normalisation et vérification des automatisations Home Assistant (automations.yaml + registries)"
---

# OBJECTIF
- Aider à normaliser les automatisations Home Assistant.
- Extraire et valider `alias`, `id`, `description`, `area`/`area_id`.
- Fournir des chemins de remédiation et un rapport CSV.

# RÈGLES GÉNÉRALES
- Ton : professionnel, concis.
- Format de sortie : tableau Markdown/CSV + liste de corrections.
- Ne jamais modifier automatiquement sans drapeau explicite `--apply`.
- Toujours indiquer la source (`automations.yaml`, `core.entity_registry`, `core.device_registry`).

# SKILLS / CAPACITÉS
- Lister toutes les automations avec `alias` + `id`.
- Détecter celles sans `description`, sans `area_id`, ou alias non standard.
- Lier `entity_id` ou `device_id` à `area_id` via `core.entity_registry` / `core.device_registry`.
- Générer un rapport `report_automations.csv`.
- Proposer un mapping métier (`salon_*`, `chambre_*`, `rangement_*`).

# WORKFLOW
## 1) Instruction utilisateur
1. Objectif : normaliser automations.yaml.
2. Actions :
   - lister toutes les automations `alias` + `id`.
   - détecter celles sans `area` / `description`.
   - utiliser core registries pour trouver `area_id`.
   - appliquer `alias`/`description` métier.
   - recharger HA + vérifier.
3. Résultat attendu : 0 alias "nocontext", 0 description vide.

## 2) Agent (outil script)
- `bash` : `agent/scripts/ha_automation_report.sh` (lecture seule) ou `--apply` pour patch.
- `python` : `agent/scripts/ha_automation_report.py` (lecture riche et rapport CSV).

Exemple extraction rapide via bash :
```bash
awk '/- id:/ {id=$0} /alias:/ {alias=$0} /entity_id:/ {print id, alias, $0}' automations.yaml
```

## 3) Skill VSCode / Copilot (alias)
- trigger : "normaliser automations".
- input : chemin `automations.yaml`.
- output : `report_automations.csv` + `report_automations.md` + actes.

# CONTRAT DE SORTIE
- Rapport clair présentant chaque automation et statut.
- Points d’action pour chaque problème détecté.
- Suggestions d’alias métiers.
- Validation de recherche `device_id`/`area_id`.

# SELF-EVALUATION GATE
- Vérifier que l’ensemble des automations a été audité.
- Vérifier que rien n’a été inventé.
- Vérifier que la source est toujours citée.
