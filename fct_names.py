import os
import string

"""test"""
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def extraire_noms_presidents(nom_fichier):
    # Extraire le nom du fichier sans l'extension
    nom_president = nom_fichier.replace('Nomination_', '').replace('.txt', '')
    return nom_president

def associer_prenom_nom(nom):
    # Ajouter des règles de correspondance pour associer un prénom et un nom à chaque nom si nécessaire
    presidents = {
        'Chirac1': {'prenom': 'Jacques', 'nom': 'Chirac'},
        'Chirac2': {'prenom': 'Jacques', 'nom': 'Chirac'},
        'Giscard dEstaing': {'prenom': 'Valéry', 'nom': 'Giscard dEstaing'},
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


def nettoyer_texte(texte):
    # Convertir le texte en minuscules
    texte = texte.lower()
    # Supprimer la ponctuation
    ponctuation = string.punctuation
    texte_sans_ponctuation = ''.join(char if char not in ponctuation else ' ' for char in texte)
    # Remplacer l'apostrophe et le tiret avec un traitement spécial
    texte_sans_ponctuation = texte_sans_ponctuation.replace("’", " ").replace("-", " ")
    return texte_sans_ponctuation

def nettoyer_et_enregistrer_fichier_entier(chemin_entree, chemin_sortie):
    # Lire le contenu du fichier
    with open(chemin_entree, 'r', encoding='utf-8') as file:
        contenu = file.read()

    # Nettoyer le texte
    texte_nettoye = nettoyer_texte(contenu)

    # Écrire le texte nettoyé dans le nouveau fichier
    with open(chemin_sortie, 'w', encoding='utf-8') as file:
        file.write(texte_nettoye)

def nettoyer_et_enregistrer_fichiers_dossier_entier(repertoire_entree, repertoire_sortie):
    # Créer le répertoire de sortie s'il n'existe pas
    if not os.path.exists(repertoire_sortie):
        os.makedirs(repertoire_sortie)

    # Liste des fichiers dans le répertoire d'entrée
    fichiers = list_of_files(repertoire_entree, '.txt')

    # Parcourir les fichiers et nettoyer chaque fichier
    for fichier in fichiers:
        chemin_entree = os.path.join(repertoire_entree, fichier)
        chemin_sortie = os.path.join(repertoire_sortie, fichier)

        nettoyer_et_enregistrer_fichier_entier(chemin_entree, chemin_sortie)