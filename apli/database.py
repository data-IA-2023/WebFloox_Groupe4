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
from module_film import ratings, principal

# =========================================================
# autre import
# =========================================================
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text, MetaData, Table
from sqlalchemy import select
import pandas as pd
from sqlalchemy import Column, Integer, Text, MetaData, Table, String, Float
from sqlalchemy import select
from sqlalchemy.orm import declarative_base

# =========================================================
# main instruction
# =========================================================

# a changer par des variable d'environnement
db_user = 'citus'   
db_password = 'floox2024!'   
db_host = 'c-groupe1.duymdlia3bmy3f.postgres.cosmos.azure.com'   
db_port = '5432'  
db_name = 'netfloox' 

# connection a la base de donnee
db_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(db_url)

# creation de la session
session = sessionmaker(bind=engine)()

# query pour ratings et principal avec filtre
q = session.query(ratings, principal).filter( ratings.tconst == principal.tconst ).filter(
         principal.isadult == 0, principal.titletype == "movie", principal.startyear >= 1950).filter(
        ratings.averagerating > 3).limit(10000).all()

# création du dataframe à partire du query
df = pd.DataFrame()
count = 0
for row in q :
    dict_ratings = row[0].items()
    df_rating = pd.DataFrame(dict_ratings, columns = ['tconst', 'averagerating', 'numvotes'], index=[count])
    # print("df_rating :", df_rating)
    dict_princip = row[1].items()
    # print("dict_princip :", dict_princip)
    df_princip = pd.DataFrame(dict_princip, columns = ['tconst', 'originaltitle', 'genres_type', 'startyear', 'runtimeminutes', 'isadult', 'titletype'], index=[count])
    # print("df_princip :", df_princip)
    df_tot = df_princip.merge(df_rating, left_on='tconst', right_on='tconst')
    # print("df_tot :", df_tot)
    df = pd.concat([df, df_tot], ignore_index=True)
    count += 1
print("df :", df)

# clé de l'api TMDB
api_key = "85cdde7a5ded572cc0dd44be5b0af9eb"

# foction qui retourne l'image d'un film
def get_movie_poster_url(tmdb_id):
    global api_key
    base_url = 'https://api.themoviedb.org/3/movie/'
    endpoint = f'{tmdb_id}?api_key={api_key}'
    response = requests.get(base_url + endpoint)
    if response.status_code == 200:
        data = response.json()
        if 'poster_path' in data:
            poster_path = data['poster_path']
            return f'https://image.tmdb.org/t/p/w500/{poster_path}'
    return None

# foction qui retourne le resumé d'un film
def get_movie_synopsis(tmdb_id):
    global api_key
    base_url = 'https://api.themoviedb.org/3/movie/'
    endpoint = f'{tmdb_id}?api_key={api_key}&language=fr-FR'
    response = requests.get(base_url + endpoint)
    if response.status_code == 200:
        data = response.json()
        if 'overview' in data:
            return data['overview']
    return None

# créé les 2 colonne avec le lien de l'image et le resumé de chaque film
# df["url_post"] = df["tconst"].apply(get_movie_poster_url)
# print("df url :", df)

# df["synopsis"] = df["tconst"].apply(get_movie_synopsis)
# print("df url + resum :", df)

# fonction qui retourne le dataframe 
def get_df ():
    global df
    return df