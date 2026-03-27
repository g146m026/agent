# SKILL: Obsidian Knowledge Graph Architect

## Description
Transforme un vault Obsidian en graphe de connaissance structuré (business, technique, Neo4j, Mermaid, HTML).

## Capabilities
- Scan de vault Obsidian (Markdown, YAML, tags, liens, dossiers)
- Classification automatique des notes (business_domain, process, system, etc.)
- Extraction des propriétés métier (frontmatter + corps markdown) et tags inline (#tasmota, #devices, ...)
- Fusion de tags frontmatter + inline et normalisation
- Mapping vers modèle Neo4j (labels, relations)
- Détection des gaps de connaissance
- Génération de graphes Mermaid (L1-L4) et HTML
- Suggestions d’enrichissement et structuration

## Entrées
- Dossier Obsidian, notes Markdown, structure de dossiers, liens, tags, frontmatter

## Sorties
- Inventaire, classification, mapping Neo4j, Mermaid, HTML, recommandations

## Utilisation
- Pour tout besoin d’analyse, structuration ou visualisation de connaissance à partir d’un vault Obsidian.

## Prompts internes
- Classifier une note
- Enrichir une note métier
- Générer un sous-graphe
- Relier médias et business

## Auteur
- Conçu pour l’architecture de la connaissance métier et technique.
