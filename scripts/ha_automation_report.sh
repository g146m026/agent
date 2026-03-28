#!/usr/bin/env bash
# Lecture seule par défaut, produit des rapports et des diagnostics.
set -euo pipefail

AUTOS=${1:-automations.yaml}
ENTITY_REG=${2:-.storage/core.entity_registry}
DEVICE_REG=${3:-.storage/core.device_registry}
REPORT_CSV=${4:-report_automations.csv}
REPORT_MD=${5:-report_automations.md}

if [ ! -f "$AUTOS" ]; then
  echo "ERROR: automations file not found: $AUTOS" >&2
  exit 2
fi
if [ ! -f "$ENTITY_REG" ]; then
  echo "WARNING: entity registry not found: $ENTITY_REG" >&2
fi
if [ ! -f "$DEVICE_REG" ]; then
  echo "WARNING: device registry not found: $DEVICE_REG" >&2
fi

# Extrari, recherche manuelle
echo "### 1) Quick check (alias, description vide, area_id absent)"
 grep -n "alias:" "$AUTOS" | head -n 40 || true
 echo "---"
 grep -n "description: ''" "$AUTOS" || true
 echo "---"
 grep -n "area: \|area_id:" "$AUTOS" || true

# Build CSV header
printf 'automation_id,alias,description,has_area,has_description,missing_description,missing_area\n' > "$REPORT_CSV"

echo "### 2) Parse automations (sans parser YAML complet)"
# Parse minimal; chaque automation doit commencer par '- id:' dans un flux YAML normal.
awk -v CSV="$REPORT_CSV" 'BEGIN {FS=":"; id=""; alias=""; desc=""; area=""}
  /- id:/ {if (id!="") {
        has_desc=(desc!=""?"1":"0"); has_area=(area!=""?"1":"0"); missing_desc=(desc==""?"1":"0"); missing_area=(area==""?"1":"0");
        gsub(/^[ \\t]+|[ \\t]+$/, "", id);
        gsub(/^[ \\t]+|[ \\t]+$/, "", alias);
        gsub(/^[ \\t]+|[ \\t]+$/, "", desc);
        gsub(/^[ \\t]+|[ \\t]+$/, "", area);
        printf "%s,%s,%s,%s,%s,%s,%s\n", id, alias, desc, has_area, has_desc, missing_desc, missing_area >> CSV;
      }
      sub(/^[ \\t]*- id:[ \\t]*/, "", $0); id=$0; alias=""; desc=""; area=""; next }
  /alias:/ {sub(/^[ \\t]*alias:[ \\t]*/, "", $0); alias=$0; next }
  /description:/ {sub(/^[ \\t]*description:[ \\t]*/, "", $0); desc=$0; next }
  /area_id:/ {sub(/^[ \\t]*area_id:[ \\t]*/, "", $0); area=$0; next }
  /area:/ {sub(/^[ \\t]*area:[ \\t]*/, "", $0); if(area=="") area=$0; next}
  END {if (id!="") {has_desc=(desc!=""?"1":"0"); has_area=(area!=""?"1":"0"); missing_desc=(desc==""?"1":"0"); missing_area=(area==""?"1":"0"); gsub(/^[ \\t]+|[ \\t]+$/, "", id); gsub(/^[ \\t]+|[ \\t]+$/, "", alias); gsub(/^[ \\t]+|[ \\t]+$/, "", desc); gsub(/^[ \\t]+|[ \\t]+$/, "", area); printf "%s,%s,%s,%s,%s,%s,%s\n", id, alias, desc, has_area, has_desc, missing_desc, missing_area >> CSV; }}' "$AUTOS"

# Reporting MD
cat <<EOF > "$REPORT_MD"
# Home Assistant Automation Report

- Source : $AUTOS
- Entity registry : $ENTITY_REG
- Device registry : $DEVICE_REG

## Résumé
- Automations analysées : $(tail -n +2 "$REPORT_CSV" | wc -l)
- descriptions vides : $(awk -F',' '$6=="1"{c++} END{print c+0}' "$REPORT_CSV")
- areas manquantes : $(awk -F',' '$7=="1"{c++} END{print c+0}' "$REPORT_CSV")

## Détails
| id | alias | description | area | status |
|--|--|--|--|--|
$(tail -n +2 "$REPORT_CSV" | while IFS=',' read -r aid aal desc has_area has_desc missing_desc missing_area; do
  st="ok";
  if [ "$missing_desc" -eq 1 ]; then st="missing description"; fi;
  if [ "$missing_area" -eq 1 ]; then st="$st, missing area"; fi;
  echo "| $aid | $aal | $desc | $( [ "$has_area" -eq 1 ] && echo yes || echo no) | $st |";
done)
EOF

echo "Rapports générés: $REPORT_CSV et $REPORT_MD"

echo "### 3) device_id/entity_id mapping (core registries)"
if [ -f "$ENTITY_REG" ]; then
  echo "Samples entity -> area_id via entity_registry:";
  jq -r '.data[] | select(.area_id!=null) | "\(.entity_id),\(.area_id)"' "$ENTITY_REG" | head -n 20
else
  echo "entity_registry absent, impossible de mapper area_id.";
fi
if [ -f "$DEVICE_REG" ]; then
  echo "Samples device -> area_id via device_registry:";
  jq -r '.data[] | select(.area_id!=null) | "\(.id),\(.area_id)"' "$DEVICE_REG" | head -n 20
else
  echo "device_registry absent, impossible de mapper area_id.";
fi

echo "### 4) Recommandations"
cat <<EOD
- Vérifier que configuration.yaml inclut automations.yaml.
- Recharger automations dans HA : configuration -> automations -> reload.
- Éliminer descriptions vides et alias nocontext.
- Pour appliquer automatiquement, utiliser le script Python (semi-automatique). 
EOD
