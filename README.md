# Weeding
Ce projet est un travail d'exposé donné au cours de Programmation web 2  en Faculté des Sciences et Technologies, promotion L2 LMD Mathématique Informatique à l'Université de Kinshasa (UNIKIN).

<br/>

## <a name="s-1"></a>1 - Installation de l'environnement du projet et lancement du serveur Django
Les points [1.1](#s-1.1) et [1.3](#s-1.3) seront exécutés uniquement lors de la première initialisation du projet. Ils ne seront pas exécutés à moins qu'il y ait de nouvelles dépendances, auquel cas vous devrez réexécuter le point [1.3](#s-1.3) uniquement.<br/>
Chaque fois que vous voudrez lancer le serveur, vous devrez exécuter le point [1.2](#s-1.2), puis le point [1.4](#s-1.4).
<br/>
### <a name="s-1.1"></a>1.1 - Mise en place de l'environnement
Exécutez la commande suivante à la racine du projet :
```sh
python -m venv env
```
Cette commande mettra en place l'environnement local du projet.
> Vous verrez un dossier ***env*** ajouté à la racine du projet.

<br/>

### <a name="s-1.2"></a>1.2 - Activation de l'environnement du projet dans la console
Exécutez le fichier suivante à la racine du projet :
```sh
env\Scripts\activate.bat
```
> Dans votre console, vous verrez ***(env)*** ajouté à la ligne d'exécution de votre console.

<br/>

### <a name="s-1.3"></a>1.3 - Installation des dépendances
Exécutez la commande suivante à la racine du projet :
```sh
pip install -r requirements.txt
```
Cette commande installera toutes les dépendances du projet se trouvant dans le fichier ***requirements.txt***.

<br/>

### <a name="s-1.4"></a>1.4 - Lancement du serveur Django
> Ce serait mieux avant de lancer le serveur que vous créiez les [migrations](#s-2.1) en premier, pour prévenir d'éventuelles erreurs liées au manque de BDD

Exécutez la commande suivante à la racine du projet :
```sh
python weeding/manage.py runserver
```

<br/>
<br/>

## <a name="s-2"></a>2 - Les Migrations et Seeders
### <a name="s-2.1"></a>2.1 - Création des migrations
Exécutez la commande suivante à la racine du projet :
```sh
python weeding/manage.py makemigrations
```

<br/>

### <a name="s-2.2"></a>2.2 - Appliquer les migrations
Exécutez la commande suivante à la racine du projet :
```sh
python weeding/manage.py migrate
```
Cette commande appliquera les changements dans la base de données.

<br/>

### <a name="s-2.3"></a>2.3 - Remplir la BDD
Exécutez la commande suivante à la racine du projet :
```sh
python weeding/manage.py seed
```
Cette commande ajoutera des fausses données dans la base de données afin de la remplir au minimum.
> Afin de voir quels sont les modèles concernés par l'ajout de ces données<br/>Consulter le fichier de la commande `seed` se trouvant dans `./app/diab/management/commands/seed.py`.<br/>Dans ce fichier, vous trouverez les ***Factory*** de ***Model*** et le nombre de données qu'elles créeront dans la base de données.
