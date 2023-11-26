from fct_tf_idf import *
# fonction liste des fichiers
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# fonction qui calcule la matrice TF-IDF
directory = './cleaned/'
tfidf_matrice, tout_mots, list_f = calculer_tf_idf_matrice(directory)

############################
#Question 1:
############################


def mots_non_importants():

    # initialise une liste pour stocker les mots non importants
    mots_non_importants = []
    for i in range(len(tout_mots)):
        # initialise un booleen pour indiquer si le mot est "non important"
        est_non_important = True
        # vérifie si le score TF-IDF est 0 dans tous les fichiers
        for j in range(len(list_f)):
            if tfidf_matrice[i][j] != 0:
                est_non_important = False
            # si le mot est non important l'ajoute à la liste
        if est_non_important:
            mots_non_importants.append(tout_mots[i])
    return mots_non_importants

# affiche les mots non importants
def listniw():
    mots_non_importants_liste = mots_non_importants()
    print("Mots non importants :")
    print(mots_non_importants_liste)


############################
#Question 2:
############################


def plus_grand_tfidf():
    # appel de la fonction pour trouver le mot ayant le score TF-IDF le plus élevé

    max_tfidf = -1
    max_tfidf_words = []
    for i in range(len(tout_mots)):
        mot = tout_mots[i]
        max_tfidf_word_score = max(tfidf_matrice[i])

        if max_tfidf_word_score > max_tfidf:
            max_tfidf = max_tfidf_word_score
            max_tfidf_words = [mot]
        elif max_tfidf_word_score == max_tfidf:
            max_tfidf_words.append(mot)

    return max_tfidf_words, max_tfidf

# affiche le mot ayant le score TF-IDF le plus élevé
def tdfmax():
    max_tfidf_words, max_tfidf_value = plus_grand_tfidf()
    print("Mot ayant le score TF-IDF le plus élevé ", max_tfidf_value, ":")
    print(max_tfidf_words)

############################
# Function n°3
############################

def mots_plus_repetes_chirac(directory):
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

# affiche les mots les plus répétés par le président Chirac
def repete():
    directory = './cleaned/'
    mots_repetes_chirac = mots_plus_repetes_chirac(directory)
    print("Les mots les plus répétés par le président Chirac :", mots_repetes_chirac)

############################
# Function n°4
############################

def occurrences_nation(directory):
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

    # Trouve les présidents qui ont parlé de "nation"
    presidents_nation = [president for president, occ in presidents_occurrences.items() if occ > 0]
    # Trouve le président qui a répété le plus de fois le mot "nation"
    president_plus_repete = max(presidents_occurrences, key=presidents_occurrences.get)

    return presidents_nation, president_plus_repete

# affiche les président qui ont utilisé « nation » dans leurs discours
def occnation():
    directory = './cleaned/'
    presidents_nation, president_plus_repete = occurrences_nation(directory)

    if president_plus_repete == "Chirac2" :
        president_plus_repete = "Chirac"
    if president_plus_repete == "Mitterrand2" :
        president_plus_repete = "Mitterrand"
    if presidents_nation:
        print("Président(s) qui ont parlé de la « Nation » :", presidents_nation)
        print("Président qui l’a répété le plus de fois :", president_plus_repete)
    else:
        print("Aucun président n'a parlé de la « Nation » dans les discours analysés.")

############################
# Function n°5
############################

def climat_ecologie(directory):
    all_presidents = set()  # Ensemble pour stocker tous les noms de président

    for fichier in list_of_files(directory, '.txt'):
        # Extraire le nom du président à partir du nom du fichier
        president = fichier.split('_')[1].split('.')[0]
        all_presidents.add(president)

        occurrences = calculer_tf(fichier)
        if "climat" in occurrences or "écologie" in occurrences:
            return president  # Le premier président à parler du climat ou de l'écologie

# affiche le premier président à parler du climat ou de l’écologie
def climeco():
    directory = './cleaned/'
    premier_president = climat_ecologie(directory)
    print("Premier président à parler du climat et/ou de l’écologie :", premier_president)


############################
#Question 6:
############################


def mots_communs(tfidf_matrice, tout_mots, list_f):
    # initialise une liste pour stocker les mots communs à tous les présidents
    mots_comm = []

    # boucle sur chaque mot
    for i, mot in enumerate(tout_mots):
        # initialise une variable pour indiquer si le mot est commun à tous les présidents
        est_commun = True
        # boucle sur chaque fichier pour vérifier si le score TF-IDF est non nul
        j = 0
        while est_commun and j < len(list_f):
            if tfidf_matrice[i][j] == 0:
                # si le score TF-IDF est nul dans un fichier le mot n'est pas commun
                est_commun = False
            j += 1
        # si le mot est commun à tous les présidents l'ajoute à la liste
        if est_commun:
            mots_comm.append(mot)
    return mots_comm

# affiche les mots communs à tous les présidents
def communs():
    directory = './cleaned/'
    # utilise la fonction qui calcule la matrice TF-IDF
    tfidf_matrice, tout_mots, list_f = calculer_tf_idf_matrice(directory)

    # affiche les mots communs à tous les présidents
    mots_communs_liste = mots_communs(tfidf_matrice, tout_mots, list_f)
    print("Mots important communs à tous les présidents :")
    print(mots_communs_liste)
