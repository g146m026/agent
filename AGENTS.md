# AGENTS.md

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
