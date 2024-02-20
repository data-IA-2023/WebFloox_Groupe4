import os

# Obtenir le répertoire courant du projet
current_directory = os.getcwd()
print("Le répertoire courant du projet est :", current_directory)
# PS C:\Users\Lau\Documents\Moi\1-Travail (sept 23)\3- IA\1- Formation Greta\3- Projets\4-Webfloox>

# Nouveau chemin vers le répertoire
#new_directory = "E:/Documents/4- Projets/3- Projet Netfloox/3- Projet Netfloox "

# Changer le répertoire courant
#os.chdir(new_directory)

# Vérifier si le répertoire a bien été changé
#current_directory = os.getcwd()
# print("Le nouveau répertoire courant est :", current_directory)

#%% Packages
import pandas as pd
from plotnine import ggplot, aes, geom_bar, ggtitle, xlab, ylab, scale_fill_brewer, guides
from plotnine import options, scales, theme_minimal, scale_fill_manual
from plotnine.themes import theme
from plotnine import element_text,geom_point, geom_segment, theme_classic, scale_color_manual
import matplotlib.pyplot as plt
import numpy as np

import pkg_resources
#%% Connaitre les packages et les exporter dans le fichier requierments

# Récupérer une liste de tous les packages installés
installed_packages = pkg_resources.working_set

# Créer un dictionnaire pour stocker les noms des packages et leurs versions
packages_info = {}

# Parcourir chaque package installé et stocker son nom et sa version dans le dictionnaire
for package in installed_packages:
    packages_info[package.key] = package.version
    
# Afficher les noms des packages et leurs versions
for package, version in packages_info.items():
    print(f"{package}: {version}")