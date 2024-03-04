# =========================================================
# import
# =========================================================
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import declarative_base

# =========================================================
# classe = ratings
# 
# attribut : 
#     tconst
#     averageRating
#     numVotes
#
# methode :
#     __str__
#     items
#     id_film
# 
# =========================================================

# =========================================================
# classe = principal
# 
# attribut : 
#     tconst
#     originaltitle
#     genres_type
#     startyear
#     runtimeminutes
#     isadult
#     titletype
#
# methode :
#     __str__
#     items
#     id_film
# 
# =========================================================

# déclaraction de la classe de basse de sqlalchimy
# tous les modèles en hérite
Base = declarative_base()

metadata = Base.metadata

# clase pour la table ratings
class ratings( Base ):
    __tablename__ = "title_ratings"
    __table_args__ = {'extend_existing': True}

    tconst = Column(String, primary_key=True)
    averagerating = Column(Float)
    numvotes = Column(Integer)

    def __init__(self, tconst="tt0000001", averagerating=5.7, numvotes=2020):
        self.tconst = tconst
        self.averagerating = averagerating
        self.numvotes = numvotes

    def __str__(self):
        return f"{self.tconst},{self.averagerating},{self.numvotes}"
    
    def items(self):
        return { "tconst":self.tconst, "averagerating":self.averagerating, "numvotes":self.numvotes}
    
    def id_film (self):
        return self.tconst

# clase pour la table title_basics
class principal ( Base ):
    __tablename__ = "title_basics"
    __table_args__ = {'extend_existing': True}

    tconst = Column(String, primary_key=True)
    originaltitle = Column(String)
    genres_type = Column(String)
    startyear = Column(Integer)
    runtimeminutes = Column(Integer)
    isadult = Column(Integer)
    titletype = Column(String)

    def __init__(self, tconst="tt6329900", originaltitle="Hua hua gong zi", genres_type=["Comedy", "Romance"], startyear=1974, runtimeminutes=80, isadult=0, titletype="movie"):
        self.tconst = tconst
        self.originaltitle = originaltitle
        self.genres_type = genres_type
        self.startyear = startyear
        self.runtimeminutes = runtimeminutes
        self.isadult = isadult
        self.titletype = titletype

    def __str__(self):
        return f"{self.tconst},{self.originaltitle},{self.genres_type},{self.startyear},{self.runtimeminutes},{self.isadult},{self.titletype}"
    
    def items(self):
        return { "tconst":self.tconst, "originaltitle":self.originaltitle, "genres_type":[self.genres_type], "startyear":self.startyear, "runtimeminutes":self.runtimeminutes, "isadult":self.isadult, "titletype":self.titletype}
    
    def id_film (self):
        return self.tconst