# Projet 10 : Analyse de Réseaux et Détection de Communautés

## Objectif
Analyser la structure d'un réseau social pour identifier les individus les plus influents (centralité) et détecter les communautés naturelles (clustering).

## Questions Business
1. Quels sont les "influenceurs" clés du réseau (nœuds centraux) ?
2. Comment le réseau se divise-t-il en groupes ou communautés ?
3. Quels nœuds servent de "ponts" entre différentes communautés ?

## Dataset
Source : Zachary's Karate Club (intégré à NetworkX).
- 34 membres d'un club de karaté.
- 78 interactions/relations.
- Conflit historique ayant mené à la scission du club en 2 groupes.

## Méthodologie
- **Représentation** : Graphe non-orienté avec NetworkX.
- **Centralité** : Degré (popularité) et Intermédiarité (Betweenness - rôle de pont).
- **Détection de communautés** : Algorithme de Girvan-Newman.
- **Visualisation** : Matplotlib avec coloration par communauté.
- **MLOps** : Tracking des métriques de réseau avec MLflow.

## Installation
```bash
pip install -r requirements.txt
