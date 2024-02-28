# =========================================================
# classe = utilisateur
# 
# attribut : 
#     id_util
#     name
#     mot_de_pass
#     preference_video_IMDB
#     is_authenticated
# 
# constructeur : 
#     self, json_nom, json_mdp, json_pref
# 
# methode :
#     connect_statut(self)
#     user_name_get(self)
#     ajout_preference (self, video_preference)
#     get_preference (self)
# 
# =========================================================
from module_utilisateur import utilisateur as m_user

# =========================================================
# classe = IMDB
# 
# attribut : 
#     id_video
#     key
#     parent_key
#     title
#     types
#     genres
#     duree
#     actor
#     director
#     writer
#     producer
#     cinematographer
#     composer
#     editor
#     production_designer
#     self_role
#     archive_footage
#     archive_sound
#     averageRating
#     numVotes
#     region
# 
# constructeur : 
#     /
# 
# methode :
#     /
# 
# =========================================================
# from module.module_film import video_IMDB as m_video

# =========================================================
# autre import
# =========================================================
from flask import Flask, render_template, request, redirect
import pandas as pd
import numpy as np
import os
import hashlib

# =========================================================
# main instruction
# =========================================================

# chemin du fichier
repertoir_fichier = os.path.dirname(__file__)
print(repertoir_fichier)

# fonction de hashage de mot de passe
def hashage(valeur):
    return hashlib.md5(valeur.encode("utf-8")).hexdigest()

# ouvre le fichier users_data.json si il existe, le crée sinon
if os.path.isfile(f"{repertoir_fichier}\\users_data.json") == False:
    df = pd.DataFrame({"identifiant" : "root", "mot_de_passe" : hashage("root"), "preference" : {"0" : np.nan}})
    df.to_json(f"{repertoir_fichier}\\users_data.json", index=False)
else :
    df = pd.read_json(f"{repertoir_fichier}\\users_data.json")

# crée la liste d'utilisateur
df = df.fillna(0)
print(df)
list_users = df["identifiant"].to_list()
print(list_users)

# connection, l'instence user ne peux pas exister sans connection, l'erreur est normal
try :
    connect_user = user_obj.connect_statut
except :
    user_obj = None
    connect_user = False

print (connect_user)

# crée l'app flask
app = Flask(__name__)

# home, page ouverte par défault
@app.route("/")
def home():
    global connect_user
    global user_obj
    if connect_user == True :
        # retourne le succes        
        user_name = user_obj.user_name_get()
        return render_template("home.html", user_statut=connect_user, user_get=user_name)
    else :
        return render_template("home.html", user_statut=connect_user)

# page d'inscription 
@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    global connect_user
    global user_obj
    print("connect_user", connect_user)
    print("user_obj", user_obj)
    if request.method == "POST":
        # obient identifien et mot_de_passe du formulaire de la page html et en fait un dataframe
        identifiant_var = request.form["identifiant_get"]
        mot_de_passe_var = hashage(request.form["mot_de_passe_get"])

        if identifiant_var not in list_users :
            df_user = pd.DataFrame({'identifiant' : identifiant_var, 'mot_de_passe' : mot_de_passe_var, 'preference' : {"0" : np.nan}})

            # concat le df_user avec le dataframe actuel et l'enregistre dans le json
            df_concat = pd.concat([df, df_user], ignore_index=True)
            print(df_concat)
            df_concat.to_json(f"{repertoir_fichier}\\users_data.json")
            
            # retourne le succes
            succes_user = "Ce compte a bien été créé"
            return render_template("inscription.html", user_statut=connect_user, succes_get = succes_user)
        
        else :
            # retourne l'erreur
            error_user = "Ce nom d'utilisateur est déjà utilisé"
            return render_template("inscription.html", user_statut=connect_user, error_get = error_user)
    else:
        return render_template("inscription.html", user_statut=connect_user)

# page de connexion 
@app.route("/login", methods=["GET", "POST"])
def login():
    global connect_user
    global user_obj
    if request.method == "POST":
        # obient identifien et mot_de_passe du formulaire de la page html et en fait un dataframe
        identifiant_var = request.form["identifiant_get"]
        mot_de_passe_var = hashage(request.form["mot_de_passe_get"])

        # print(identifiant_var, mot_de_passe_var)

        # vérifie que le nom d'utilisateur est bon
        if identifiant_var in list_users :
            user_connect = df.loc[df["identifiant"] == identifiant_var]
            mot_de_passe_save = user_connect["mot_de_passe"].values
            mot_de_passe_item = mot_de_passe_save.item(0)
            print("user_connect", user_connect)
            print ("mot_de_passe_save", mot_de_passe_save)
            print ("mot_de_passe_item", mot_de_passe_item)
            print ("mot_de_passe_var", mot_de_passe_var)
            
            # vérifie que le mot de passe est bon
            if mot_de_passe_var == mot_de_passe_item :
                # création de l'utilisateur
                pref_list = user_connect["preference"].to_dict()
                print(pref_list)
                if len(pref_list.items()) == 1 : 
                    for cle, valeur in pref_list.items():
                        if valeur == 0 :
                            pref_dict = {}
                        else :
                            pref_dict = pref_list
                else :
                    pref_dict = pref_list
                user_obj = m_user(identifiant_var, mot_de_passe_var, pref_dict)
                
                # is_authenticated = true
                connect_user = user_obj.is_authenticated
                print("connect_user", connect_user)
                print(user_obj)
                
                # retourne la page home
                return redirect("/")
            else :
                # retourne l'erreur
                error_connect = "Le mot de passe est incorrecte"
                return render_template("login.html", user_statut=connect_user, error_get = error_connect)
        else :
            # retourne l'erreur
            error_connect = "Ce nom d'utilisateur est inconnu"
            return render_template("login.html", user_statut=connect_user, error_get = error_connect)
    else:
        return render_template("login.html", user_statut=connect_user)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    global connect_user
    global user_obj
    if request.method == "POST":
        # supprime l'utilisateur
        user_obj = None
        connect_user = False
        print("user_obj", user_obj)
        print ("connect_user", connect_user)

        # retourne la page home
        return redirect("/")
    elif connect_user == False :
        # retourne la page home
        return redirect("/")
    else :
        return render_template("logout.html", user_statut=connect_user)

@app.route("/recommendation")
def recommendation():
    global connect_user
    global user_obj
    return render_template("recommendation.html", user_statut=connect_user)

@app.route("/preference")
def preference():
    global connect_user
    global user_obj
    return render_template("preference.html", user_statut=connect_user)

# app.run => permet d'executer l'application flack
if __name__ == "__main__":
    app.run()