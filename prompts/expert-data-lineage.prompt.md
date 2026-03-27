# PROMPT: expert-data-lineage (conforme Copilot)

## Objectif
Déclencher un audit ou une analyse de data lineage, conformité ou migration sur un module du repo.

## Structure
- Entrées attendues : nom du module, type d’audit, source de vérité
- Sortie attendue : bullet points ou tableau, actions recommandées, sources citées
- Contraintes : ne pas inventer, ne pas extrapoler, toujours citer la source

## Exemples
Utilisateur : "Audit data lineage pour api_plesk"
Assistant :
- Source : api_plesk/config/routes.php
- Traitement : src/Core/Router/Router.php
- Stockage : data/*.json
- Risques : absence de validation sur certains endpoints
- Action : proposer un test automatisé avec validate_data_stores.py

## Self-check
Avant de répondre, vérifier :
- Que la sortie respecte le format et la consigne
- Que chaque donnée/action est sourcée

## Header de stabilité
Toujours interpréter les instructions littéralement. Ne jamais inférer ou réordonner. Répondre uniquement dans le format requis.
