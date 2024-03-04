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
# 
#     crée le dataframe
# 
# methode :
#     get_df
# 
# =========================================================
import database

# =========================================================
# autre import
# =========================================================
from flask import Flask, render_template, request, redirect
import pandas as pd
import numpy as np
import os, requests
import hashlib
import json

# =========================================================
# main instruction
# =========================================================

# import df
df_film = database.get_df()

# chemin du fichier
repertoir_fichier = os.path.dirname(__file__)
print(repertoir_fichier)

# fonction de hashage de mot de passe
def hashage(valeur):
    return hashlib.md5(valeur.encode("utf-8")).hexdigest()

# ouvre le fichier users_data.json si il existe, le crée sinon
if os.path.isfile(f"{repertoir_fichier}\\users_data.json") == False:
    df = pd.DataFrame({"identifiant" : "root", "mot_de_passe" : hashage("root"), "preference" : {"0" : np.nan}})
    df.to_json(f"{repertoir_fichier}\\users_data.json", index=False, orient='index')
else :
    df = pd.read_json(f"{repertoir_fichier}\\users_data.json", orient='index')

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

# crée le top des films les mieux noté
# print(df_film.info())
top_film = df_film.sort_values(by=["averagerating"]).head(10)

# créé les 2 colonne avec le lien de l'image et le resumé de chaque film
top_film["url_post"] = top_film["tconst"].apply(get_movie_poster_url)
print("df url :", top_film)

top_film["synopsis"] = top_film["tconst"].apply(get_movie_synopsis)
print("df url + resum :", top_film)

row_data=list(top_film.values.tolist())
print("row_data :", row_data)

# for film in row_data :
#     print("film :", film)
#     print("film[0] :", film[0])

# home, page ouverte par défault
@app.route("/")
def home():
    global connect_user
    global user_obj
    global top_film
    if request.method == "POST":
        film = request.form["film_get"]
        return redirect("/film", film_post = film)
    elif connect_user == True :
        # retourne le succes        
        user_name = user_obj.user_name_get()
        return render_template("home.html", user_statut=connect_user, user_get=user_name, get_top_5=list(top_film.values.tolist()) )
    else :
        return render_template("home.html", user_statut=connect_user, get_top_5=list(top_film.values.tolist()) )

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
            df_concat.to_json(f"{repertoir_fichier}\\users_data.json", orient='index')
            
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

# page de deconnexion 
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

# page de recommendation 
@app.route("/recommendation")
def recommendation():
    global connect_user
    global user_obj
    global df_film

    """
    df['title'].fillna('', inplace=True)
        df['genres'] = df['genres'].fillna('')
        df['genres'] =  df['genres'].str.replace(',', ' ')
        df['actor'] = df['actor'].astype(str) 
        df['director'] =df['director'].astype(str)
        df['writer'] =df['writer'].astype(str)
        df['genres'] = df['genres'].fillna('')
        df['title'] = df['title'].fillna('')
        df['countTitleByRegion']= df['countTitleByRegion'].fillna('')
        df['averageRating'] =df['averageRating'].astype(str)
        
        # For simplicity,  fill missing values for categorical data with a placeholder and numerical with median
        df.fillna({'title': 'Unknown', 'director': 'Unknown', 'actor': 'Unknown', 
                'genres': 'Unknown', 'writer': 'Unknown'}, inplace=True)
        
        # Imputing missing numerical values with median
        num_imputer = SimpleImputer(strategy='median')
        df[['startYear', 'runtimeMinutes' , 'countTitleByRegion']] = num_imputer.fit_transform(df[['startYear', 'runtimeMinutes','countTitleByRegion']])
        
        # Normalize 'startYear' and 'runtimeMinutes'
        # Combine textual features
        return df
        
        
    df = load_data()
    df['combined_features'] = df['title']+ ' ' + df['director']+ ' ' + df['actor'] + ' ' + df['genres'] + ' ' + df['writer'] 
    scaler = MinMaxScaler()
    numerical_features_scaled = scaler.fit_transform(df[['startYear', 'runtimeMinutes', 'countTitleByRegion']])
    vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')
    combined_features_tfid1 = vectorizer.fit_transform(df['combined_features'])
    model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
    model_knn.fit(combined_features_tfid1)
    combined_features_tfidf = hstack([combined_features_tfid1, numerical_features_scaled])

    def suggest_film_name_contains(input_film_name, df):
        input_film_name_lower = input_film_name.lower()
        contains_match_df = df[df['title'].str.lower().str.contains(input_film_name_lower)]
        if not contains_match_df.empty:
            return contains_match_df.iloc[0]['title']
        else:
            return None

    def get_recommendations(film_name,df):
        film_index = df[df['title'] == film_name].index[0] # Assuming film_name exactly matches a title in df
        film_features = vectorizer.transform([df.iloc[film_index]['combined_features']])
        distances, indices = model_knn.kneighbors(film_features, n_neighbors=50) # Fetching 6 neighbors to exclude the film itself
        recommendations = []
        
        for i in range(0, len(distances.flatten())):

            if i == 0:
                print(f'Recommendations for "{film_name}":\n')
            else:
                # Append recommendation details to the list
                index = indices.flatten()[i]  # Get the original DataFrame index for the recommended item
                recommendations.append({
                    'index': df.index[index],
                    'title': df.iloc[indices.flatten()[i]]['title'],
                    'Distance': distances.flatten()[i],
                    'rating': df['averageRating'][i] 
                })
        recommendations_df = pd.DataFrame(recommendations)
        return recommendations_df

        

    film_to_index = pd.Series(df.index, index=df['title']).to_dict()
    # Recommendation cosine_sim
    @st.cache_data
    def get_cosine_sim_recommendations(film_name):
        if film_name in film_to_index:
            # Get the index of the film from its name
            idx = film_to_index[film_name]
            # Compute cosine similarity between the film's features and the features of all films
            cosine_sim = cosine_similarity(combined_features_tfid1, combined_features_tfid1[idx])
            
            # Get pairwise similarity scores for all films with that film
            sim_scores = list(enumerate(cosine_sim.flatten()))
            
            # Sort the films based on the similarity scores
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            
            # Get the scores of the 50 most similar films, skip the first one since it is the query film itself
            sim_scores = sim_scores[1:51]
            
            # Get the film indices
            film_indices = [i[0] for i in sim_scores]
            
            # Return the top 50 most similar films
            return  df.iloc[film_indices][['title']].reset_index()
        else:
            return None

    def create_graph(recommendations_df, input_film_name):
        G = nx.Graph()
        G.add_node(input_film_name, size=20, color= "black" , title=input_film_name)
        
        for index, row in recommendations_df.iterrows():
            G.add_node(row['title'], size=15,color= "red", title=row['title'])
            G.add_edge(input_film_name, row['title'])
        
        return G

    def show_graph(G):
        nt = Network('500px', '100%', notebook=True)
        nt.from_nx(G)
        nt.show('nx.html')
        return 'nx.html'


    def main():
        # Main page
        input_film_name = st.text_input("Enter the name of the film:")
        if st.button('Recommendations'):
            if input_film_name:
                # Apply filtering only if a specific genre is selected; otherwise, use the full dataset
            
                
                suggested_film_name = suggest_film_name_contains(input_film_name,df)
                if suggested_film_name:
                    st.write(f"Suggested Name: {suggested_film_name}")
                    rec_knn = get_recommendations(suggested_film_name,df)
                    rec_knn = pd.DataFrame(rec_knn)
                    rec_movies = get_cosine_sim_recommendations(suggested_film_name )

                    if not rec_knn.empty and rec_movies is not None and not rec_movies.empty:
                        # Use columns to display results side by side
                            st.write("KNN Recommendations:")
                            st.dataframe(rec_knn)
                            G_knn = create_graph(rec_knn, suggested_film_name)
                            knn_graph_path = show_graph(G_knn)
                            HtmlFile = open(knn_graph_path, 'r', encoding='utf-8')
                            source_code = HtmlFile.read() 
                            components.html(source_code, width=500, height=500)

                    
                            st.write("Cosine Similarity :")
                            st.dataframe(rec_movies)

                            G_cosine = create_graph(rec_movies, suggested_film_name)
                            cosine_graph_path = show_graph(G_cosine)
                            HtmlFile = open(cosine_graph_path, 'r', encoding='utf-8')
                            source_code = HtmlFile.read()
                            components.html(source_code, width=500, height=500)

                            matched_df = pd.merge(rec_knn, rec_movies, how='inner', on=('index', 'title')).head(5)
                        
                            if not matched_df.empty:
                                st.write("Matched Recommendations:")
                                st.dataframe(matched_df)
                                G_cosine = create_graph(matched_df , suggested_film_name)
                                cosine_graph_path = show_graph(G_cosine)
                                HtmlFile = open(cosine_graph_path, 'r', encoding='utf-8')
                                source_code = HtmlFile.read()
                                components.html(source_code, width=500, height=500)

                            else:
                                st.write("No matched recommendations found.")
                    else:
                        st.write("No recommendations found.")
                else:
                    st.write("No film found with that name. Please try another name.")
            else:
                st.write("Please enter a film name for recommendations.")

    return render_template("recommendation.html", user_statut=connect_user)
    """

# page de detaille du film 
@app.route("/film", methods=['GET', 'POST'])
def film():
    global connect_user
    global user_obj
    global df_film
    film_id = request.args['id']
    print("film_id :", film_id)
    film_select = df_film.loc[df_film['tconst'] == film_id]
    film_select["url_post"] = film_select["tconst"].apply(get_movie_poster_url)
    film_select["synopsis"] = film_select["tconst"].apply(get_movie_synopsis)

    list_film_select = film_select.values.tolist()
    print("list_film_select_test 1 :", list_film_select)
    list_film = list_film_select[0]
    print("list_film_test :", list_film)
    if request.method == "POST":
        note_user = request.form["note_get"]

        user_obj.ajout_preference(film_id, note_user)
        dict_pref = user_obj.get_preference().values
        print("dict_pref :", dict_pref)

        name = user_obj.user_name_get()
        index_list = df.index[df['identifiant'] == name].to_list()
        index = index_list[0]
        print(index)

        df.loc[index, 'preference'] = dict_pref
        print("df :", df)

        df.to_json(f"{repertoir_fichier}\\users_data.json", orient='index')

        return render_template("film.html", user_statut=connect_user, get_film=list_film)
    else:
        return render_template("film.html", user_statut=connect_user, get_film=list_film)

# page de preference 
@app.route("/preference")
def preference():
    global connect_user
    global user_obj
    pref_user = user_obj.get_preference()
    if len(pref_user) == 0 :
        # retourne l'erreur'        
        user_name = user_obj.user_name_get()
        error_pref = f"{user_name}, tu n'as pas encore rensseigner test préférences"
        return render_template("preference.html", user_statut=connect_user, error_get = error_pref, user_get=user_name)
    
    elif len(pref_user) >= 1 :
        # genere les préférence à afficher

        # post => modification/suppretion des préférences
        
        # retourne l'erreur'        
        user_name = user_obj.user_name_get()
        error_pref = f"{user_name}, tu n'as pas encore rensseigner test préférences"
        return render_template("preference.html", user_statut=connect_user, error_get = error_pref, user_get=user_name)
    else :
        return render_template("preference.html", user_statut=connect_user)


# app.run => permet d'executer l'application flack
if __name__ == "__main__":
    app.run()