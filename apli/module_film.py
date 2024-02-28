# =========================================================
# import
# =========================================================
from dataclasses import dataclass

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
@dataclass
class video_IMDB() :

    # ===== attribut =====
    id_video: int # auto
    key: str # tconst
    parent_key: str # parentTconst
    title: str # primaryTitle
    types: str # titleType
    genres: list[str] # genres
    duree: int # runtimeMinutes
    start_year: int # startYear
    end_year: int # endYear
    actor: list[str] # actor
    director: list[str] # director
    writer: list[str] # writer
    producer: list[str] # producer
    cinematographer: list[str] # cinematographer
    composer: list[str] # composer
    editor: list[str] # editor
    production_designer: list[str] # production_designer
    self_role: list[str] # self
    archive_footage: list[str] # archive_footage
    archive_sound: list[str] # archive_sound
    averageRating: list[str] # averageRating
    numVotes: list[str] # numVotes
    region: int # count des differentes region
    resume: str # à crée
    image: image() # à crée

    # ===== constructeur =====

    # ===== methode =====
