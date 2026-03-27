# Agent Instructions (migration)

Copie initiale de l’ancien fichier, à adapter selon la nouvelle structure et les conventions 2026-03-01.

## Objectif
- Supporter le développement sur les projets multi-modules : `girard-hub`, `jukebox`, `soccer-phenix`
- Préférer architecture claire : HTML/CSS/JS séparés + templates
- API local (PHP/Plesk) et données JSON persistantes
- Test automatisés et validations compatibles avec les scripts existants

## Activités couvertes
- Corrections de bug fonctionnel (auth, score, routing)
- Ajout de tests (unitaires, intégrations JS via Node/JSDOM)
- Refactor de presentation (layout, theme, responsive)
- Gestion de données JSON + schemas (validation extras)
- Documenter et commenter chaque changement
- Adaptation d’agents Obsidian->Neo4j (importation des notes, tags, relations, slots #tasmota/#devices)

## Style et conventions
- Pas de code spaghetti : un changement par ticket, commits atomiques
- Utiliser `replace_string_in_file` avec 3-5 lignes de contexte
- Ne pas toucher fichiers non concernés
- Toujours vérifier avec tests (`docker compose restart web && node test/...`)

## Questions pour l'utilisateur
1. Quel comportement exact attends-tu (ex: un écran précis, URL, template) ?
2. Si plusieurs modes existent (admin, non-admin, debug), lequel prioriser ?
3. Faut-il ajuster également docs / README du module ?

## Exemples de prompt
- "Ajoute un bouton de filtre pour matches / pratiques dans `soccer-phenix` et test JS".
- "Corrige la liaison score/gallerie pour ne pas partager score de pratique/match".
- "Génère un itinéraire API en PHP pour sauvegarder et valider une soumission de contribution."

## Rappels
- On utilise `safeJson` et `safeJsonFallback` existants.
- `data/*.json` est source de vérité, éviter `links.json` non namespaced.
- Préférer `form` + validation front/back (client et PHP).
