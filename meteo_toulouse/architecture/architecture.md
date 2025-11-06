# 🧱 Architecture du projet Météo Toulouse

## 1. Objectif
Ce document décrit la structure logicielle du projet Météo Toulouse, son organisation, et les principes SOLID appliqués.

---

## 2. Vue d’ensemble
Le projet est structuré en 5 couches principales :

1. **Collectors** → récupération des données météo depuis l’API Open Data.
2. **Cleaners** → nettoyage et transformation des données brutes.
3. **Models** → définition des entités Python (données météo structurées).
4. **Services** → logique métier (prévision, planification, rapports).
5. **Utils** → fonctions transversales (logs, configuration).

---

## 3. Application des principes SOLID

| Principe | Application |
|-----------|-------------|
| **S** | Chaque dossier correspond à une seule responsabilité. |
| **O** | Le code est ouvert à l’extension (nouvelles implémentations). |
| **L** | Les sous-classes peuvent remplacer leurs interfaces. |
| **I** | Chaque interface est spécifique (`ICollector`, `ICleaner`, `IService`). |
| **D** | Les dépendances sont injectées dans `main.py`. |

---

## 4. Schéma logique (simplifié)


main.py
 ├── ForecastService (IService)
 │     ├── OpenDataCollector (ICollector)
 │     └── DataCleaner (ICleaner)
 └── Utils (Logger, Config)
