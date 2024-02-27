from flask import Flask, render_template, request
from flask_login import login_user
from flask_login import LoginManager
import pandas as pd
import numpy as np
import os
import hashlib
import json

from module_utilisateur import utilisateur as m_user

# fonction de hashage de mot de passe
def hashage(valeur):
    return hashlib.md5(valeur.encode("utf-8")).hexdigest()

user_connect = pd.DataFrame({"identifiant" : "toto", "mot_de_passe" : [hashage("toto")], "preference" : [np.nan]})

identifiant_var = "toto"
mot_de_passe_v = user_connect["mot_de_passe"].to_list()
mot_de_passe_var = mot_de_passe_v[0]

# création de l'utilisateur
pref_list = user_connect["preference"].to_list()
if pref_list[0] == np.nan :
    pref_list = []
user_obj = m_user(identifiant_var, mot_de_passe_var, pref_list)

# is_authenticated = true
global connect_user 
connect_user = user_obj.is_authenticated
print("connect_user", connect_user)
print(user_obj)