# =========================================================
# classe = IMDB
# 
# attribut : 
#     id
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
# 
# 
# methode :
# 
# 
# =========================================================
# from module_film import video_IMDB

# =========================================================
# import
# =========================================================
from dataclasses import dataclass

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
@dataclass
class utilisateur() :

    # ===== attribut =====
    identifiant: str # nom
    mot_de_pass: str # mdp
    preference_video_IMDB: dict # liste de video préféré
    is_authenticated: bool # statut de l'autentification

    # ===== constructeur =====
    def __init__ (self, json_nom, json_mdp, json_pref):
        self.identifiant = json_nom
        self.mot_de_pass = json_mdp
        self.preference_video_IMDB = json_pref
        self.is_authenticated = True

    # ===== methode =====
    def connect_statut (self):
        """
        entée = /
        sorti = bool is_authenticated
        =================================
        /
        """
        return self.is_authenticated
    
    def user_name_get (self):
        """
        entée = /
        sorti = identifiant
        =================================
        /
        """
        return self.identifiant
    
    def ajout_preference (self, key, value):
        """
        entée = un objet de classe video_IMDB
        sorti = /
        =================================
        ajout l'objet a la liste de préférence
        """ 
        self.preference_video_IMDB[key]=value

    def get_preference (self):
        """
        entée = self
        sorti = liste des préférence
        =================================
        retourne la liste des préférence
        """ 
        return self.preference_video_IMDB

