import os

# crée un tableau avec lec listes des fichiers de discours
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# Extrait le nom du président à partir du nom du fichier
def extraire_noms_presidents(nom_fichier):
    # Extraire le nom du fichier sans l'extension
    nom_president = nom_fichier.replace('Nomination_', '').replace('.txt', '')
    return nom_president

def associer_prenom_nom(nom):
    # Ajouter des règles de correspondance pour associer un prénom et un nom à chaque nom si nécessaire
    presidents = {
        'Chirac1': {'prenom': 'Jacques', 'nom': 'Chirac'},
        'Chirac2': {'prenom': 'Jacques', 'nom': 'Chirac'},
        'Giscard dEstaing': {'prenom': 'Valéry', 'nom': "Giscard d'Estaing"},
        'Hollande': {'prenom': 'François', 'nom': 'Hollande'},
        'Macron': {'prenom': 'Emmanuel', 'nom': 'Macron'},
        'Mitterrand1': {'prenom': 'François', 'nom': 'Mitterrand'},
        'Mitterrand2': {'prenom': 'François', 'nom': 'Mitterrand'},
        'Sarkozy': {'prenom': 'Nicolas', 'nom': 'Sarkozy'}
    }
    return presidents.get(nom, {'prenom': 'Prénom non trouvé', 'nom': 'Nom non trouvé'})

def afficher_noms_presidents_uniques(directory, extension):
    # Liste des fichiers dans le répertoire avec l'extension spécifiée
    fichiers = list_of_files(directory, extension)

    # Ensemble pour stocker les noms uniques des présidents
    noms_presidents_uniques = set()

    # Parcourir les fichiers et extraire les noms des présidents
    for fichier in fichiers:
        nom_president = extraire_noms_presidents(fichier)
        info_president = associer_prenom_nom(nom_president)
        nom_complet = f"{info_president['prenom']} {info_president['nom']}"
        noms_presidents_uniques.add(nom_complet)

    # Afficher la liste des noms uniques des présidents
    print("Liste des noms uniques des présidents :")
    for nom in noms_presidents_uniques:
        print(nom)

