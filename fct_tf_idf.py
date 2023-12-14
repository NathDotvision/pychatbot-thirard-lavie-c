import os
import math
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# Fonction qui calcul le tf des fichier
def calculer_tf(fichier):
    # initialise un dictionnaire pour stocker les occurrences de chaque mot dans le fichier
    occurrences = {}
    # Ouverture du fichier en mode lecture avec l'encodage UTF-8
    with open('./cleaned/' + fichier, 'r', encoding='utf-8') as file:
         #Lit le contenu complet du fichier
        contenu = file.read()

        # boucle à travers chaque mot dans le contenu du fichier
        for mot in contenu.split(' '):
            # Vérifie si le mot est déjà dans le dictionnaire d'occurrences
            if mot in occurrences:
                #si le mot existe, incrémente le compteur d'occurrences
                occurrences[mot] += 1
            else:
                #si le mot n'existe pas, initialise le compteur d'occurrences à 1
                occurrences[mot] = 1
    return occurrences


# Définit le répertoire des fichiers et permet d'obtenir la liste des noms de fichiers avec l'extension '.txt' dans le répertoire cleaned
directory = './cleaned/'
list_f = list_of_files(directory, '.txt')

# création d'une boucle à travers chaque fichier dans la liste
for fichier in list_f:
    #appelle la fonction calculer_tf pour obtenir le dictionnaire d'occurrences
    resultat_occurrences = calculer_tf(fichier)

# Affiche le nom du fichier et le dictionnaire d'occurrences pour le fichier
#    print("Dictionnaire pour le fichier ", fichier, ":")
#    print(resultat_occurrences)


#fonction qui calcul idf
def calculer_idf(liste_f):
    score = {}
    nb_docs = len(liste_f)
    tf_scores_per_file = {}  # Store TF scores for each file

    for fichier in liste_f:
        tf_scores_per_file[fichier] = calculer_tf(fichier)  # Calculate TF scores once per file
        with open('./cleaned/' + fichier, 'r', encoding='utf-8') as file:
            contenu = file.read()
            mots_pres = set()
            for mot in contenu.split(' '):
                if mot not in mots_pres:
                    mots_pres.add(mot)
                    if mot in score:
                        score[mot] += 1
                    else:
                        score[mot] = 1

    for mot in score:
        compt = 0
        for fichier in liste_f:
            if mot in tf_scores_per_file[fichier]:  # Refer to stored TF scores
                compt += 1
        idf = nb_docs / (compt + 1)
        score[mot] = math.log(idf) if idf > 1 else 0

    return score


directory = './cleaned/'
list_f = list_of_files(directory, '.txt')
# Appelle dela fonction calculer_idf pour obtenir le dictionnaire des scores IDF
idf_scores = calculer_idf(list_f)




def calculer_tf_idf_matrice(directory):
    list_f = list_of_files(directory, '.txt')
    #initialisation de la liste des scores TF-IDF pour chaque fichier
    tfidf_matrice_data = []
# boucle sur chaque fichier pour calculer les scores TF-IDF
    for fichier in list_f:
        # calculez les scores TF pour le fichier actuel
        tf_scores = calculer_tf(fichier)
        # calculez les scores TF-IDF pour chaque mot dans le fichier
        tfidf_scores = {}
        for mot, tf in tf_scores.items():
            tfidf_scores[mot] = tf * idf_scores[mot]
        # ajoutez les scores TF-IDF du fichier à la liste
        tfidf_matrice_data.append(tfidf_scores)

    # obtenez la liste de tous les mots uniques
    tout_mots = []
    for tfidf_scores in tfidf_matrice_data:
        for mot in tfidf_scores.keys():
            if mot not in tout_mots:
                tout_mots.append(mot)
    # initialisez la matrice TF-IDF
    tfidf_matrice = []
    # Boucle sur chaque mot pour creer une ligne dans la matrice
    for mot in tout_mots:
        # initialisez une ligne de la matrice avec des zeros
        lig_data = []
        # boucle sur chaque fichier pour récupérer le score TF-IDF du mot
        for tfidf_scores in tfidf_matrice_data:
            lig_data.append(tfidf_scores.get(mot, 0))
        # ajoutez la ligne à la matrice TF-IDF
        tfidf_matrice.append(lig_data)
    return tfidf_matrice, tout_mots, list_f

directory = './cleaned/'
#utilise la fonction calcule la matrice TF-IDF
tfidf_matrice, tout_mots, list_f = calculer_tf_idf_matrice(directory)




#Création de la fonction pour plus de lisibilité pour la comprehension des reponses
def afficher_matrice_mots_et_fichiers(tfidf_matrice, tout_mots, list_f):
    # affichez les noms de fichiers en tant qu'en tête
    print("", end="    ")
    for col_fi in list_f:
        print(col_fi, end="    ")
    print()
    # affichez chaque mot avec les  scores TF-IDF correspondant
    for i in range(len(tout_mots)):
        print(tout_mots[i], end="    ")
        for j in range(len(list_f)):
            print(tfidf_matrice[i][j], end="    ")
        print()

directory = './cleaned/'
#utilise la fonction calcule la matrice TFIDF
tfidf_matrice, tout_mots, list_f = calculer_tf_idf_matrice(directory)
# affichez la matrice avec les mots, les fichiers et les scores TF-IDF
#afficher_matrice_mots_et_fichiers(tfidf_matrice, tout_mots, list_f)