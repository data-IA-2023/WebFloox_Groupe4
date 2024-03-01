# Projet Wetfloox : Sandy, Rémi & Laurence


* **Trello** :
  https://trello.com/b/uU3wjKIq/webfloox
  

* **La Présentation** : 

* **Documentation** : https://developer.imdb.com/non-commercial-datasets/   et   https://help.imdb.com/article/contribution/other-submission-guides/country-codes/G99K4LFRMSC37DCN# 

* **Codes SQL** : 
   * XXXXXXX permet de créer toutes les clés primaires et de mettre les bons types dans la base de données. Il contient également les SQL pour la créations des tables et des views.

* La **Base de Donnée Relationnelle**, réalisée sous _DBeaver_ et hébergée sur _Azure_. 




  
* **Code Python** :
  * Le fichier *requirements.txt* indique l'ensemble des packages qui seront utilisés dans ce projet.
  * Le fichier *.gitignore* inclus l'ensemble des extensions qui ne sont pas partagées en ligne.
  * *xxxxxxx* nous permet avec l'input d'un film de ressortir 5 films les plus similaires. Il s'appuie sur le CSV cosine_features.csv qui contient l'ensemble des films et des features importantes.
  * *xxxxxx* est le script pour la réalisation des graphiques sous python.
Cette section lit des fichiers CSV contenant des données sur les films, et utilise _plotnine_ ou _matplotlib_ pour créer un scatter plot, box plot, pairplot, ou des camemberts représentant les informations du data set.
  * On utilise le fichier *xxxxxxx* pour la recommandation d'un film.
  
 
Ce code est une mise en œuvre d'un pipeline complet pour la construction et l'évaluation de modèles de régression utilisant différents algorithmes et techniques de prétraitement des données. Les différentes bibliothèques utilisées dans le code sont importées, y compris des outils de machine learning de scikit-learn, ainsi que pandas, numpy et psycopg2 pour la manipulation des données.

Les données sont lues à partir d'un fichier CSV situé à l'URL spécifiée. En cas d'erreur de lecture, un message d'erreur est affiché. Les fonctions de nettoyage sont définies pour transformer les données textuelles dans certaines colonnes en listes, remplacer les valeurs manquantes par 'inconnu', et convertir certaines colonnes en types numériques. Ensuite, les données textuelles sont fusionnées en une seule chaîne pour chaque ligne. Un pipeline est créé  qui effectue le prétraitement des données, y compris l'imputation, la mise à l'échelle et l'encodage, puis applique un modèle d'apprentissage automatique donné. Différents ensembles de paramètres sont définis pour les différents modèles d'apprentissage automatique à évaluer. Chaque ensemble de paramètres spécifie les prétraitements et les hyperparamètres spécifiques au modèle. Les données sont divisées en ensembles d'entraînement et de test pour l'évaluation des modèles.

Un modèle final est entraîné en utilisant le meilleur pipeline identifié par la recherche sur la grille avec les meilleurs hyperparamètres. Le modèle final est évalué sur l'ensemble de test à l'aide de différentes métriques telles que le coefficient de détermination (R²), l'erreur absolue moyenne (MAE) et l'erreur quadratique moyenne (MSE). Le modèle final est sauvegardé sous forme de fichier pickle pour une utilisation ultérieure.

  * On utilise le fichier *xxxxxx* pour la notation d'un film.

Ce script démontre une approche complète pour la construction, l'optimisation et l'évaluation de modèles d'apprentissage automatique pour prédire des notes de films en utilisant diverses techniques de prétraitement des données et des algorithmes d'apprentissage automatique.




* Le fichier **style.css** contient du code CSS qui définit les styles pour un menu latéral (sidenav) qui s'ouvre et se ferme au clic d'un bouton.

Ce code CSS définit les styles pour un menu latéral (sidenav) qui s'ouvre et se ferme au clic d'un bouton. Voici une explication ligne par ligne :

 `body { font-family: "Lato", sans-serif; }` Définit que tout le texte dans le corps de la page sera affiché en police "Lato" ou en police sans serif si "Lato" n'est pas disponible. `.sidenav { height: 100%;width: 0;position: fixed; z-index: 1;top: 0; left: 0; background-color: #111;overflow-x: hidden; transition: 0.5s;padding-top: 60px;}`
   - Définit les styles pour la barre de navigation latérale.
   - Elle est positionnée de manière fixe (`position: fixed`) afin qu'elle reste en place lorsque l'utilisateur fait défiler la page.
   - Sa largeur initiale est de 0, ce qui signifie qu'elle est fermée par défaut.
   - `z-index: 1` assure que la barre de navigation reste au-dessus du contenu principal.
   - `background-color: #111` définit la couleur de fond à un noir foncé.
   - `overflow-x: hidden` cache tout contenu qui dépasse horizontalement de la barre de navigation.
   - `transition: 0.5s` ajoute une transition de 0,5 seconde pour une ouverture en douceur.
   - `padding-top: 60px` ajoute un espace en haut de la barre de navigation pour éviter qu'elle ne chevauche le contenu.
     
 `.sidenav a { padding: 8px 8px 8px 32px;text-decoration: none;font-size: 25px;color: #b2b2b2; display: block; transition: 0.3s; }`
   - Définit les styles pour les liens à l'intérieur de la barre de navigation.
   - `padding` définit l'espacement intérieur des liens.
   - `text-decoration: none` supprime les soulignements des liens.
   - `font-size: 25px` définit la taille de la police des liens.
   - `color: #b2b2b2` définit la couleur du texte des liens.
   - `display: block` affiche les liens comme des blocs afin qu'ils remplissent toute la largeur de la barre de navigation.
   - `transition: 0.3s` ajoute une transition de 0,3 seconde lorsqu'on survole les liens.

`.sidenav a:hover { color: #f1f1f1; } }`Change la couleur du texte des liens lorsque l'utilisateur survole un lien avec la souris.

`.sidenav .closebtn {position: absolute;top: 0; right: 25px;font-size: 36px;margin-left: 50px; }` Styles pour le bouton de fermeture de la barre de navigation.
 Il est positionné en haut à droite de la barre de navigation. `font-size: 36px` définit la taille de la police du bouton de fermeture.

 `#main {transition: margin-left .5s; padding: 16px;}` Définit les styles pour la section principale de la page. La transition spécifiée permet un déplacement en douceur (`margin-left`) lorsque la barre de navigation est ouverte ou fermée.

`@media screen and (max-height: 450px) {.sidenav {padding-top: 15px;} .sidenav a {font-size: 18px;} }`
   - Ajoute des styles spécifiques lorsque la hauteur de l'écran est inférieure à 450 pixels.
   - Réduit l'espacement supérieur de la barre de navigation et la taille de police des liens.

* Le fichier *home.html* situé dans : apli/templates/home.html contient le code HTML  de base pour une page web avec un menu latéral réactif (sidenav) qui s'ouvre et se ferme au clic d'un bouton.







  ## Notre projet combine un système de recommandation de films basé sur le contenu déjà noté par l'utilisateur, avec un modèle de prédiction de popularité des films. L'utilisateur peut interagir avec l'application en saisissant le nom d'un film, en explorant les détails des films et en obtenant des recommandations personnalisées. 
