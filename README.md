# Food Suggestor

### Introduction

Ce programme permet de substituer des aliments par d'autres meilleurs pour la santé.
Il se base sur les données publique de la base de donnée [OpenFoodFact](https://fr.openfoodfacts.org/decouvrir).

Les aliments sont repertoriés et triés par catégorie, il vous sera alors possible de choisir
une catégorie et ensuite un produit particulier.
Il vous sera alors proposé une alternative et vous pourrez, si vous le désirer enregistrer ce
choix dans la base de donnée pour pouvoir le retrouver plus tard.

Les bienfais alimentaires des aliments sont basés sur leur nutriscrore. "A" étant la meilleure note et "E" la moins bonne.

----------------------- 

### Documentation-Driven Development

#### Strategie générale adoptée pour le développement, séparation des fonctionnalités en différents "Blocs" de développement. 

1. Créer une base de donnnée pour contenir les aliments et les substitutions
    ```
        db_management/
    ```
    - 3 tables differentes :
        - 1. Table contenant les différentes catégories chargées depuis notre programme
        - 2. Table contenant tout les aliments ordonés par catégorie
        - 3. Table contenant les subsitutions
    
2. Recupérer les informations sur les produits et les enregistrer dans notre BDD
    ```
        management_api/
    ```
    - Charger les différentes catégories
    - Requêter l'API d'OpenFoodFact (catégorie, nombre de produits souhaités)
    - Vérifier les données récupérées pour avoir des données complètes.
    - Les enregistrer en BDD

3. Créer une interaction avec l'utilisateur pour pouvoir répondre à ses attentes
    ```
        user_interaction/
        food_suggestor
    ```
    - Récupérer les catégories / Récupérer le choix / Afficher les produits associés

4. Proposer des substitutions
    ```
        db_interaction/
    ```
    - Explorer notre base de donnée et afficher les produits de la même catégorie qui ont un meilleur nutriscore que celui du produit actuel.

5. Enregistrer les résultats si voulu
    ```
        food_suggestor
        db_interaction/
    ```
    - Proposer aux utilisateur de sauvegarder la substitution

-------------------------- 
### Pré-requis

Ce programme est écrit en Python et le systeme de base de donnée utilisé est SQL et MySql.
Vous aurez besoin pour lancer ce programme :

- [Python3](https://www.python.org/)
- [MySql](https://www.mysql.com/fr/)

Pour installer les dépendances vous aurez également du gestionnire de package (PyPi)

- [Pip](https://pip.pypa.io/en/stable/installing/)

Deux libraires externes seront utilisés dans ce projet (Requests pour requêter l'API et PyMysql pour gérer la base de donnée depuis le programme) vous pourrez les installer avec la commande ci-dessous. Elle sera à executer à la racine du projet (ou vous trouverez le fichier 'requirements.txt')

```
pip install -r requirements.txt
```

## Installations

Une fois les dépendances et les programmes installés connectez vous à MySql et exectuez le fichier .sql

```
source [path script mysql db_management/db_creation_script.sql]
```

Votre schéma de donnée est désormais crée.
Vous devez ensuite renseigner les informations spécifiés dans le dossier "environnement.example.txt" et enregistrer celui ci comme "environnement.txt" **à l'emplacement suivant** :

```
settings_confs_files/environnement.txt
```


Pour le premier lancement de l'application vous aller devoir remlir la base de donnée avec
des données de l'API.

Pour cela :

1. Lancez le programme :
```
    python food-suggestor
```
2. Séléctionnez l'option n°3, cela aura pour effect de remplir la base de donnée
3. Vous êtes désormais prêt et vous pouvez utiliser l'application

---------

## Lancement

1. Lancez le programme :
```
    python food-suggestor
```

- 4 choix vous sont proposés:
    - 1- Choisir une catégorie d'aliment parmis celles proposés
        - Vous pouvez ensuite choisir un aliment à substituer en indiquant sont numéro
        - Un substitut vous est proposé et vous pouvez choisir de l'enregistrer

    - 2- Afficher les produits subsitués que vous avez auparavant sauvegardés

    - 3- (Ré)initialiser la base de donnée (supprimer vos enregistrement et recharger
     des données d'aliments depuis OpenFoodFact)
    
    - 4- Quitter le programme

-------------------

## Paramètres

Plusieurs paramètres sont configurables :

1. Choix des catégories :
    - Trouvez les catégories que vous voulez depuis [OpenFoodFact](https://fr.openfoodfacts.org/categories)
    - Changer les dans le fichier setting_confs_files/settings.py dans la variable "CATEGORIE"
    - Relancer le programme et reinitialiser la base de données pour que les nouvelles catégories soient effectivent.

1. NB_RESULTS : 
    Choisir le nombre de résultat que nous allons requeter sur le site d'open food fact pour remplir chaque catégories (plus le nombre est grand plus la requête sera longue, en effet il faut compter NB_RESULTS * CATEGORIES). Minimum 50 pour être sur d'avoir des données satisfaisant et au dessus 200 comportement non testé.

2. NB_DISPLAY:
    Le nombre de résultat qui vous seront proposés lors du choix d'une catégorie.
