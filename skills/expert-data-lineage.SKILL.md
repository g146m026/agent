---
name: expert-data-lineage
summary: "Skill pour découverte d'architecture, data lineage, et règles métier dans le repo"
---

# Expert Data Lineage

Cet expert skill est conçu pour analyser et diriger l’évolution des architectures du projet:
- `api_plesk` (PHP JSON API)
- `jukebox` (FastAPI + MQTT + SQLite)
- `hass` (scripts de monitoring)

## Capacités

- analyser le flux des données (source -> traitement -> stockage)
- détecter les points d’échec et les risques de sync/dérive
- suggérer des schémas de gouvernance et tests de conformité
- proposer migration/containérisation Docker multi-service

## Commandes suggérées

- `Audit: data lineage pour api_plesk et jukebox`
- `Validation: exécuter validate_data_stores.py`
- `Architecture: générer plan docker-compose + nginx`
