import os

# URL du référentiel GitHub contenant le fichier requirements.txt
github_repo_url = "https://github.com/data-IA-2023/WebFloox_Groupe4/blob/main/requirements.txtpip install "

# Cloner le référentiel GitHub localement
os.system(f"git clone {github_repo_url}")

# Emplacement local du référentiel cloné
local_repo_path = os.path.basename(github_repo_url)

# Chemin complet du fichier requirements.txt
requirements_file_path = os.path.join(local_repo_path, "requirements.txt")

# Vérifier si le fichier requirements.txt existe
if os.path.exists(requirements_file_path):
    # Lire les packages depuis le fichier requirements.txt
    with open(requirements_file_path, "r") as f:
        packages = f.readlines()
    
    # Installer les packages à l'aide de pip
    for package in packages:
        package = package.strip()  # Supprimer les espaces blancs
        os.system(f"pip install {package}")
    print("Tous les packages ont été installés avec succès.")
else:
    print("Le fichier requirements.txt n'a pas été trouvé.")
