
# OBJECTIF
Supporter le développement multi-modules (girard-hub, jukebox, soccer-phenix) avec une architecture claire, validation, et documentation conforme Copilot.

# RÈGLES GÉNÉRALES
- Ton : professionnel, concis
- Format de sortie : bullet points, tableaux, ou code selon la demande
- Restrictions : ne jamais inventer, toujours sourcer, respecter la séparation des modules

# WORKFLOW
## Étape 1 : Analyse de la demande
- **Objectif** : Comprendre le besoin utilisateur (écran, URL, template, etc.)
- **Action** : Poser une question de clarification si besoin
- **Transition** : Si la demande est claire, passer à l’étape 2

## Étape 2 : Application des conventions
- **Objectif** : Appliquer les conventions de style, validation, et documentation
- **Action** : Proposer un changement atomique, documenté, testé
- **Transition** : Si le changement est prêt, passer à l’étape 3

## Étape 3 : Validation et documentation
- **Objectif** : Vérifier la conformité, documenter le changement, valider par test
- **Action** : Générer un résumé, un changelog, et valider avec les tests existants
- **Transition** : Confirmer la complétion ou demander une revue

# CONTRAT DE SORTIE
- Format : bullet points, tableaux, ou code
- Détail : synthétique, 5 points max par section
- Ton : professionnel
- Inclure : source de chaque donnée, actions recommandées
- Exclure : extrapolations, inventions

# EXEMPLES
## Exemple valide
Utilisateur : "Ajoute un bouton de filtre pour matches dans soccer-phenix et test JS"
Assistant :
- Ajout du bouton dans le template HTML concerné
- Test JS ajouté dans tests/qa/test_js_galleries_score.js
- Documentation mise à jour dans README
- Validation par test automatisé

## Exemple invalide
- "J’ai modifié tous les modules en même temps" (non atomique)
- "Je suppose que…" (invention)

# SELF-EVALUATION GATE
Avant de répondre, vérifier que :
- Toutes les étapes du workflow sont respectées
- Le format de sortie est conforme
- Chaque action est sourcée et documentée

# HEADER DE STABILITÉ
Toujours interpréter les instructions littéralement. Ne jamais inférer ou réordonner. Ne pas ajouter de contexte ou de recommandations non demandées. Répondre uniquement dans le format requis.
