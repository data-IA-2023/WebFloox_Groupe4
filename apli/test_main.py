from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os
import hashlib
import json

from module_utilisateur import utilisateur as m_user

import database

q = database.query_retourn()

df = pd.DataFrame.from_records(q)
print(df)

"""
# fonction de hashage de mot de passe
def hashage(valeur):
    return hashlib.md5(valeur.encode("utf-8")).hexdigest()

user_connect_nan = pd.DataFrame({"identifiant" : "toto", "mot_de_passe" : hashage("toto"), "preference" : {"0" : np.nan}})
user_connect = user_connect_nan.fillna(0)
print(user_connect)

identifiant_var = "toto"
mot_de_passe_v = user_connect["mot_de_passe"].to_list()
mot_de_passe_var = mot_de_passe_v[0]

# création de l'utilisateur
pref_list = user_connect["preference"].to_dict()
print("pref_list", pref_list)
print("pref_list['0']", pref_list["0"])
print("pref_list['0'] == 0", pref_list["0"] == 0)

print ("len", len(pref_list.items()))
if len(pref_list.items()) == 1 : 
    for cle, valeur in pref_list.items():
        if valeur == 0 :
            pref_dict = {}
        else :
            pref_dict = pref_list
else :
    pref_dict = pref_list
print("pref_dict 2", pref_dict)
user_obj = m_user(identifiant_var, mot_de_passe_var, pref_dict)

# is_authenticated = true
global connect_user 
connect_user = user_obj.is_authenticated
print("connect_user", connect_user)
print(user_obj)
"""