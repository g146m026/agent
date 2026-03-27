# AGENTS.md (conforme Copilot)

## Politique de vérité et non-hallucination
- Toute réponse d’agent doit être justifiée par une source de vérité explicite (`data_source`, référence, ou preuve).
- Les prompts et skills doivent être validés par test automatisé et revue humaine.
- Les instructions, skills, prompts et scripts sont strictement séparés.

## Structure
- `skills/` : capacités et modules agents
- `prompts/` : templates et exemples d’usage
- `scripts/` : helpers, outils de migration, validation
- `tests/` : tests unitaires et d’intégration
- `.github/workflows/` : CI, lint, validation
- `doc/` : documentation, guides, checklists

## WORKFLOW (générique agent)
1. Comprendre la demande utilisateur
2. Appliquer les conventions et le workflow du skill/agent
3. Générer une réponse conforme au contrat de sortie
4. Effectuer un self-check avant de répondre

## CONTRAT DE SORTIE
- Format : bullet points, tableaux, ou code
- Détail : synthétique, 5 points max par section
- Ton : professionnel
- Inclure : source de chaque donnée, actions recommandées
- Exclure : extrapolations, inventions

## SELF-EVALUATION GATE
Avant de répondre, vérifier que :
- Toutes les étapes du workflow sont respectées
- Le format de sortie est conforme
- Chaque action est sourcée et documentée

## HEADER DE STABILITÉ
Toujours interpréter les instructions littéralement. Ne jamais inférer ou réordonner. Ne pas ajouter de contexte ou de recommandations non demandées. Répondre uniquement dans le format requis.

## EXEMPLES
Utilisateur : "Génère un rapport de conformité pour le module X"
Assistant :
- Source : module X/config.yaml
- Vérification : schéma conforme
- Action : rapport généré en Markdown
