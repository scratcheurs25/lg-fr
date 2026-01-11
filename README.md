# lg-fr , le language de programation fait pour les français


Ce language est créer pour que de nouveaux developeur puisse créer des projet en utilisant du text , et non des block .

Ce projet permmet d'avoir une étapes entre les language visuelle (scratch) et Python

le fichier code sont en .lfr

pour lancer un fichier il faut d'abord installer l'interpreteur https://github.com/scratcheurs25/lg-fr/blob/master/main.py.

Puis installer Python.

pour coder dans ce language il est recomander d'installer notepad++ et d'y ajouter le language notepad++.xml

# Comment fonctionne le language

le code pour le hello world est le suivant



```lg-fr
AFFICHER <hello world>.
```

chaque ligne doit ce finir par un point .

Comment on créer une vraiable

```lg-fr
VARIABLE exemple1 TYPE ENTIER.
//ceci créer une variable entier (int).
VARIABLE exemple2 TYPE TEXT.
//ceci créer une vraiable text (str).
VARIABLE exemple3 TYPE BOOLEEN.
//ceci créer une vraiable booleen (bool).
```

et comment on les modifie
```lg-fr
METTRE exemple1 à 15.
METTRE exemple2 à <hello world>.
METTRE exemple3 à VRAIS.
```

on peut aussi faire des opperation
```lg-fr
METTRE exemple1 à (25*3).
METTRE exemple2 à <hello > + <world>.
METTRE exemple3 à !((exemple1 COMME TEXT) = exemple2). 
```
le COMME traduis l'entier 75 en le text <75>

on peut avec des booleen faire des condition avec le si

```lg-fr
SI !((exemple1 COMME TEXT) = exemple2) ALORS.
    AFFICHER <exemple 1 pas egal à exemple2>
SINON.
    AFFICHER <exemple 1 egal à exemple2>
FIN.
```
il peut y avoir que 1 opperateur par parentaise (+ - * / = COMME !)

enfin on peut repeter des action
```lg-fr
REPETER.
    AFFICHER <ceci est afficher indefiniment>.
FIN.
```
on peut arreter une boucle avec STOP

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

# exemple de code
se code calcule entrer1 ^ entrer2

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


