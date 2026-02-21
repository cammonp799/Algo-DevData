# 🧱 Architecture du projet Météo Toulouse

"""Architecture et design de l'application Météo Toulouse.

PRINCIPES APPLIQUÉS
===================

1. PRINCIPES SOLID
------------------
- Single Responsibility Principle (SRP): Chaque classe a une seule responsabilité
  * Record: Modèle de données uniquement
  * Station: Stockage des records d'une station
  * ApiDataExtractor: Extraction depuis API uniquement
  * RecordMapper: Mappage des données uniquement

- Open/Closed Principle (OCP): Classes ouvertes à l'extension, fermées à la modification
  * IDataExtractor interface pour ajouter de nouveaux extracteurs
  * IDataMapper interface pour ajouter de nouveaux mappeurs

- Liskov Substitution Principle (LSP): Substitution des implémentations
  * ApiDataExtractor peut remplacer IDataExtractor
  * RecordMapper peut remplacer IDataMapper

- Interface Segregation Principle (ISP): Interfaces spécifiques
  * IDataExtractor: extract()
  * IDataMapper: to_object()

- Dependency Inversion Principle (DIP): Dépendre des abstractions
  * main() dépend des interfaces, pas des implémentations concrètes

2. PRINCIPES KISS ET DRY
------------------------
- Code simple et lisible sans surengineering
- Configuration centralisée dans config.py
- Réutilisation de composants (extracteur, mappeur)
- Pas de code dupliqué

3. PRINCIPES YAGNI
------------------
- Toutes les classes sont utilisées dans main()
- Toutes les méthodes sont nécessaires

DESIGN PATTERNS UTILISÉS
========================

1. STRATEGY PATTERN
-------------------
Lieu: interfaces/ + extractors/ + mappers/

Objectif: Permettre différentes stratégies d'extraction et de mappage

Classes concernées:
- IDataExtractor (stratégie abstraite)
- ApiDataExtractor (implémentation concrète)
- IDataMapper (stratégie abstraite)
- RecordMapper (implémentation concrète)

Avantages:
✓ Facile d'ajouter de nouveaux extracteurs (CSV, JSON, XML)
✓ Facile d'ajouter de nouveaux mappeurs
✓ Respecte OCP et DIP

Exemple d'extension:
    class CsvDataExtractor(IDataExtractor):
        def extract(self, file_path: str):
            # Implémenter l'extraction CSV
            pass

2. DECORATOR PATTERN
--------------------
Lieu: decorators/

Objectif: Ajouter des responsabilités d'affichage sans modifier les modèles

Classes concernées:
- StationDisplayDecorator (décorateur pour Station)
- RecordDisplayDecorator (décorateur pour Record)

Avantages:
✓ Séparation des préoccupations (modèle vs affichage)
✓ Facilité de changer le formatage d'affichage
✓ Les modèles restent purs et simples

3. SINGLETON PATTERN
--------------------
Lieu: utils/Configuration.py

Objectif: Accès global à une configuration unique

Classe concernée:
- Configuration (méthodes statiques)

Avantages:
✓ Configuration centralisée et cohérente
✓ Accès facile et global
✓ Modification simple des paramètres

STRUCTURES DE DONNÉES
=====================

1. LISTE CHAÎNÉE (LinkedList)
-----------------------------
Localisation: models/LinkedList.py

Classes: Node, StationLinkedList

Utilisation: Stocker et parcourir les stations

Caractéristiques:
- Chaque Node contient une Station et un pointeur vers le suivant
- Traversée séquentielle du début à la fin
- Opération append(): O(n)
- Opération display_all(): O(n)

Avantages:
✓ Insertion/suppression facile entre éléments
✓ Pas de limite de taille prédéfinie
✓ Affichage séquentiel des stations

2. FILE D'ATTENTE (Queue - FIFO)
--------------------------------
Localisation: extractors/ExtractionQueue.py

Classes: ExtractionTask, ExtractionQueue

Utilisation: Gérer les tâches d'extraction en ordre FIFO

Caractéristiques:
- FIFO: First-In-First-Out
- Ajout à la fin (enqueue)
- Suppression au début (dequeue)
- Opération enqueue(): O(1)
- Opération dequeue(): O(n) [améliorer avec deque]

Avantages:
✓ Traitement des tâches dans l'ordre
✓ Gestion facile des tâches asynchrones
✓ Contrôle du flux de traitement

3. DICTIONNAIRE (Dictionary)
---------------------------
Localisation: config.py + main.py

Utilisation: Configuration centralisée et stockage de résultats

Caractéristiques:
- Clé-valeur pour accès rapide
- Clé: nom de la station, Valeur: données
- Complexité accès: O(1)

Avantages:
✓ Accès rapide aux données
✓ Structure flexible
✓ Facile à itérer

FLUX D'EXÉCUTION
================

main()
├─ 1. Initialisation
│  ├─ ApiDataExtractor() [Strategy Pattern]
│  └─ RecordMapper() [Strategy Pattern]
│
├─ 2. Création de la file d'attente
│  ├─ ExtractionQueue() [Queue - FIFO]
│  └─ Enqueue des tâches pour chaque station
│
├─ 3. Traitement de la file
│  ├─ process_queue()
│  └─ Extraction via ApiDataExtractor.extract()
│
├─ 4. Création de la liste chaînée
│  ├─ StationLinkedList() [LinkedList]
│  ├─ Création des Station
│  ├─ Mappage des Records via RecordMapper
│  └─ Ajout à la liste chaînée
│
└─ 5. Affichage
   └─ StationLinkedList.display_all()
      └─ StationDisplayDecorator [Decorator Pattern]
         └─ RecordDisplayDecorator [Decorator Pattern]

RESPECT DES CRITÈRES
====================

✓ Exécution sans erreur
✓ Respect SOLID (SRP, OCP, LSP, ISP, DIP)
✓ Respect KISS (code simple, lisible)
✓ Respect DRY (configuration centralisée)
✓ Respect YAGNI (pas d'éléments inutiles)
✓ Documentation complète (docstrings)
✓ Data Profiling (README.md)
✓ Typage des données (type hints)
✓ 3 Design Patterns (Strategy, Decorator, Singleton)
✓ Tests unitaires (test_models.py, test_extractors.py, test_mappers.py)
✓ PEP8 compliance (noms, formatage)

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
