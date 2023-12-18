# -*- coding: utf-8 -*-
"""
PyChat Bot
Programme projet python semestre 01 L1 Efrei

Auteur : Téo Lavie & Wagner Thirard
Date : novembre-décembre 2023

Fichier : fct_tf_idf.py
Fonction : Fonctions de calcul des scores TF-IDF
"""


import os
import math

"""
Retourne une liste des noms de fichiers avec l'extension spécifiée dans le répertoire donné

paramètre directory: Le répertoire à examiner
paramètre extension: L'extension des fichiers recherchés
return: Une liste des noms de fichiers avec l'extension spécifiée
"""
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def calculer_tf(fichier):
    occurrences = {}
    with open('./cleaned/' + fichier, 'r', encoding='utf-8') as file:
        contenu = file.read()

        # boucle à travers chaque mot dans le contenu du fichier
        for mot in contenu.split(' '):
            # Vérifie si le mot est déjà dans le dictionnaire d'occurrences
            if mot in occurrences:
                # si le mot existe ça incrémente le compteur d'occurrences
                occurrences[mot] += 1
            else:
                # si le mot n'existe pas ça initialise le compteur d'occurrences à 1
                occurrences[mot] = 1
    return occurrences


directory = './cleaned/'
list_f = list_of_files(directory, '.txt')


for fichier in list_f:
    # appelle la fonction calculer_tf pour obtenir le dictionnaire d'occurrences
    resultat_occurrences = calculer_tf(fichier)

"""
Calcule le terme fréquence-inverse du document (IDF) pour chaque mot dans la liste de fichiers donnée.

paramètre liste_f: La liste des noms de fichiers
return: Un dictionnaire contenant les scores IDF pour chaque mot
"""
def calculer_idf(liste_f):
    score = {}
    nb_docs = len(liste_f)
    tf_scores_per_file = {}

    for fichier in liste_f:# stocke les scores TF dans un dictionnaire pour éviter les recalculs inutiles
        tf_scores_per_file[fichier] = calculer_tf(fichier)
        with open('./cleaned/' + fichier, 'r', encoding='utf-8') as file:
            contenu = file.read()
            mots_pres = set()
            # boucle à travers chaque mot dans le contenu du fichier
            for mot in contenu.split(' '):
                if mot not in mots_pres:
                    mots_pres.add(mot)
                    if mot in score:
                        score[mot] += 1
                    else:
                        score[mot] = 1

    for mot in score:
        compt = 0
        # boucle à travers chaque fichier pour calculer le nombre de documents contenant le mot
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

"""
Calcule la matrice TF-IDF pour tous les mots et fichiers dans le répertoire spécifié

paramètre directory: Le répertoire contenant les fichiers à analyser
return: La matrice TF-IDF la liste de tous les mots uniques et la liste des noms de fichiers
"""
def calculer_tf_idf_matrice(directory):
    list_f = list_of_files(directory, '.txt')
    tfidf_matrice_data = []
    # boucle sur chaque fichier pour calculer les scores TF-IDF
    for fichier in list_f:
        # calculez les scores TF pour le fichier actuel
        tf_scores = calculer_tf(fichier)
        # calculez les scores TF-IDF pour chaque mot dans le fichier
        tfidf_scores = {}
        for mot, tf in tf_scores.items():
            tfidf_scores[mot] = tf * idf_scores[mot]
        # ajoute les scores TF-IDF du fichier à la liste
        tfidf_matrice_data.append(tfidf_scores)

    # boucle à travers chaque fichier pour obtenir la liste de tous les mots uniques
    tout_mots = []
    for tfidf_scores in tfidf_matrice_data:
        for mot in tfidf_scores.keys():
            if mot not in tout_mots:
                tout_mots.append(mot)

    tfidf_matrice = []
    # boucle sur chaque mot pour creer une ligne dans la matrice
    for mot in tout_mots:
        lig_data = []
        # boucle sur chaque fichier pour récupérer le score TF-IDF du mot
        for tfidf_scores in tfidf_matrice_data:
            lig_data.append(tfidf_scores.get(mot, 0))
        # ajoutez la ligne à la matrice TF-IDF
        tfidf_matrice.append(lig_data)
    return tfidf_matrice, tout_mots, list_f


directory = './cleaned/'
# utilise la fonction calcule la matrice TF-IDF
tfidf_matrice, tout_mots, list_f = calculer_tf_idf_matrice(directory)

"""
Affiche la matrice TF-IDF avec les mots en ligne et les fichiers en colonnes.

paramètre tfidf_matrice: La matrice TF-IDF
paramètre tout_mots: La liste de tous les mots uniques
paramètre list_f: La liste des noms de fichiers
"""
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

