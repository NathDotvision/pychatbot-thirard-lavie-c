
import os
from fct_tf_idf import calculer_tf


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# Function n°3
def mots_plus_repetes_par_chirac(directory):
    chirac_occurrences = {}  # Dictionnaire pour stocker les occurrences de chaque mot pour Chirac
    chirac_files = [fichier for fichier in list_of_files(directory, '.txt') if 'Chirac' in fichier]

    for fichier in chirac_files:
        occurrences = calculer_tf(fichier)
        for mot, occ in occurrences.items():
            if mot != '':
                if mot in chirac_occurrences:
                    chirac_occurrences[mot] += occ
                else:
                    chirac_occurrences[mot] = occ

    mots_plus_repetes = sorted(chirac_occurrences.items(), key=lambda x: x[1], reverse=True)
    return mots_plus_repetes[:10]  # Les 10 mots les plus répétés

directory = './cleaned/'
mots_repetes_chirac = mots_plus_repetes_par_chirac(directory)
print("Les mots les plus répétés par le président Chirac :", mots_repetes_chirac)

def analyse_occurrences_nation(directory):
    presidents_occurrences = {}  # Dictionnaire pour stocker les occurrences de chaque président pour "Nation"
    all_presidents = set()  # Ensemble pour stocker tous les noms de président

    for fichier in list_of_files(directory, '.txt'):
        # Extraire le nom du président en utilisant le modèle "_NomPresident."
        parts = fichier.split('_')
        if len(parts) > 1:
            president = parts[-1].replace('.txt', '')
            all_presidents.add(president)

            occurrences = calculer_tf(fichier)
            if "nation" in occurrences:
                if president in presidents_occurrences:
                    presidents_occurrences[president] += occurrences["nation"]
                else:
                    presidents_occurrences[president] = occurrences["nation"]

    if not presidents_occurrences:  # Vérifier si la liste est vide
        return [], None  # Si la liste est vide, retourner des résultats vides

    # Trouver le(s) président(s) qui a (ont) parlé de la "Nation"
    presidents_nation = [president for president, occ in presidents_occurrences.items() if occ > 0]
    # Trouver le président qui a répété le plus de fois le mot "Nation"
    president_plus_repete = max(presidents_occurrences, key=presidents_occurrences.get)

    return presidents_nation, president_plus_repete

directory = './cleaned/'
presidents_nation, president_plus_repete = analyse_occurrences_nation(directory)

if president_plus_repete == "Chirac2" :
    president_plus_repete = "Chirac"
if president_plus_repete == "Mitterrand2" :
    president_plus_repete = "Mitterrand"
if presidents_nation:
    print("Président(s) qui ont parlé de la « Nation » :", presidents_nation)
    print("Président qui l’a répété le plus de fois :", president_plus_repete)
else:
    print("Aucun président n'a parlé de la « Nation » dans les discours analysés.")


def premier_president_climat_ecologie(directory):
    all_presidents = set()  # Ensemble pour stocker tous les noms de président

    for fichier in list_of_files(directory, '.txt'):
        # Extraire le nom du président à partir du nom du fichier (supposons que le nom soit avant la première "_")
        president = fichier.split('_')[1].split('.')[0]
        all_presidents.add(president)

        occurrences = calculer_tf(fichier)
        if "climat" in occurrences or "écologie" in occurrences:
            return president  # Le premier président à parler du climat et/ou de l'écologie

    return None  # Aucun président n'a parlé du climat ou de l'écologie

directory = './cleaned/'
premier_president = premier_president_climat_ecologie(directory)
print("Premier président à parler du climat et/ou de l’écologie :", premier_president)
