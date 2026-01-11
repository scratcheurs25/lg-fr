# lg-fr — Le langage de programmation pour les francophones

lg-fr est un petit langage de programmation pensé pour les francophones, conçu comme étape intermédiaire entre les langages visuels (type Scratch) et Python. Les fichiers source ont l'extension `.lfr` et sont écrits en texte (non par blocs).

Ce dépôt contient :
- Un interpréteur/runner en Python : `main.py`
- Des exemples de programmes `.lfr`
- Un fichier `notepad++.xml` pour la coloration Notepad++

## Prérequis

- Python 3.x installé
- (Optionnel) Notepad++ si vous souhaitez importer la coloration

## Installation et exécution

1. Cloner le dépôt ou télécharger les fichiers.
2. Exécuter un fichier `.lfr` avec Python, par exemple :
   ```bash
   python main.py nom_du_programme.lfr
   ```
## Syntaxe de base

- Chaque instruction se termine par un point `.`.
- Chaînes littérales sont écrites entre chevrons : `<bonjour>`.
- Exemples d'instructions :

Hello world
```lg-fr
AFFICHER <hello world>.
```

Déclaration de variables
```lg-fr
VARIABLE exemple1 TYPE ENTIER.
// entier (int).
VARIABLE exemple2 TYPE TEXT.
// texte (str).
VARIABLE exemple3 TYPE BOOLEEN.
// booléen (bool).
```

Affectation
```lg-fr
METTRE exemple1 à 15.
METTRE exemple2 à <hello world>.
METTRE exemple3 à VRAIS.
```

Opérations et conversions
```lg-fr
METTRE exemple1 à (25*3).
METTRE exemple2 à <hello > + <world>.
METTRE exemple3 à !((exemple1 COMME TEXT) = exemple2).
```
- `COMME` convertit entre types (ex : convertir un entier en texte).
- Les opérateurs admis entre parenthèses sont un seul opérateur par parenthèse : `+ - * / = COMME !`

Conditions
```lg-fr
SI !((exemple1 COMME TEXT) = exemple2) ALORS.
    AFFICHER <exemple 1 pas egal à exemple2>.
SINON.
    AFFICHER <exemple 1 egal à exemple2>.
FIN.
```

Boucles
```lg-fr
REPETER.
    AFFICHER <ceci est affiche indefiniment>.
FIN.
```
- Pour arrêter une boucle depuis l'intérieur : `STOP`.
```lg-fr
VARIABLE exemple TYPE ENTIER.
REPETER.
	AFFICHER exemple.
	METTRE exemple à exemple + 1.
	SI exemple = 100 ALORS.
		STOP.
	FIN.
FIN.

```

Exemple — calculer entrer1 ^ entrer2 (puissance par itération)
```lg-fr
VARIABLE entrer1 TYPE ENTIER.
VARIABLE entrer2 TYPE ENTIER.
METTRE entrer1 à ENTRER COMME ENTIER.
METTRE entrer2 à ENTRER COMME ENTIER.

VARIABLE index TYPE ENTIER.
VARIABLE result TYPE ENTIER.
METTRE result à 1.
REPETER.
    METTRE result à result * entrer1.
    METTRE index à index + 1.
    SI index = entrer2 ALORS.
        STOP.
    FIN.
FIN.
AFFICHER result.
```

## Éditeur

- Importez `notepad++.xml` dans Notepad++ pour la coloration du langage `.lfr` :
  https://github.com/scratcheurs25/lg-fr/blob/master/notepad%2B%2B.xml

## Améliorations recommandées

- Ajouter un fichier `requirements.txt` ou `pyproject.toml` si `main.py` a des dépendances externes.
- Documenter la ligne de commande exacte et les options de `main.py`.
- Ajouter des exemples supplémentaires et des tests.
- Ajouter un fichier LICENSE pour préciser la licence d'utilisation.

## Contribution

Contributions bienvenues : ouvrez une issue ou proposez une pull request.
