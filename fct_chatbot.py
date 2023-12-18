# -*- coding: utf-8 -*-
"""
PyChat Bot
Programme projet python semestre 01 L1 Efrei

Auteur : Téo Lavie & Wagner Thirard
Date : novembre-décembre 2023

Fichier : fct_chatbot.py
Fonction : Fonctions du chatbot basé xur les discours
"""


from math import sqrt

from fct_tf_idf import tfidf_matrice, idf_scores, list_f, tout_mots


def transpose_matrice(matrice):
    # Transpose la matrice en échangeant les lignes par les colonnes
    return [list(colonne) for colonne in zip(*matrice)]


def nettoyer_texte(texte):
    # Nettoie le texte en ne conservant que les caractères alphabétiques et les exceptions définies
    exceptions = "çàéèêëïù0123456789"
    texte = [character if ("a" <= character <= "z") or character in exceptions else " " for character in texte]
    texte = ("".join(texte)).split(" ")
    return [mot for mot in texte if mot]


def tf_question(quest):
    # Calcule la fréquence des mots dans la question
    mots = nettoyer_texte(quest)
    occurences = {}
    for mot in mots:
        if mot:
            occurences[mot] = occurences.get(mot, 0) + 1
    return occurences


def tf_idf_question(quest):
    # Calcule le score TF-IDF pour chaque mot de la question
    mots = nettoyer_texte(quest)
    scores_tf = tf_question(mots)
    return [scores_tf.get(mot, 0) * idf_scores.get(mot, 0) for mot in tout_mots]


def produit_scalaire(vecteur1, vecteur2):
    # Calcule le produit scalaire entre deux vecteurs
    return sum(a * b for a, b in zip(vecteur1, vecteur2))


def norme_vectorielle(vecteur):
    # Calcule la norme euclidienne d'un vecteur
    return sqrt(sum(i**2 for i in vecteur))


def similarite(vecteur1, vecteur2):
    # Calcule la similarité cosinus entre deux vecteurs
    produit_scalaire_resultat = produit_scalaire(vecteur1, vecteur2)
    norme_a = norme_vectorielle(vecteur1)
    norme_b = norme_vectorielle(vecteur2)
    return produit_scalaire_resultat / (norme_a * norme_b) if norme_a and norme_b else 0


def trouver_document_pertinent(noms_fichiers):
    # Trouve le document le plus pertinent en calculant la similarité entre la question et chaque document
    similarite_max = (0, None)
    vecteur_question = tf_idf_question(question)
    for i, vecteur_doc in enumerate(transpose_matrice(tfidf_matrice)):
        score_similarite = similarite(vecteur_doc, vecteur_question)
        if score_similarite > similarite_max[0]:
            similarite_max = (score_similarite, noms_fichiers[i])
    return similarite_max[1]


def mot_plus_pertinent(quest):
    # Trouve le mot le plus pertinent dans la question en utilisant le score TF-IDF
    scores_tf_idf = tf_idf_question(quest)
    score_max = max(scores_tf_idf)
    if score_max > 0:
        return tout_mots[scores_tf_idf.index(score_max)]
    return None


def phrase_avec_mot(nom_fichier, mot):
    # Retourne la première phrase dans le fichier contenant le mot spécifié
    with open(f'./speeches/{nom_fichier}', 'r', encoding="utf-8") as f:
        texte = f.read().replace(chr(10), ' ')
    for phrase in texte.split('.'):
        if mot in phrase.lower():
            return phrase.strip()
    return None


question = input('Posez votre question : ')
fichier_pertinent = trouver_document_pertinent(list_f)
mot_pertinent = mot_plus_pertinent(question)
if mot_pertinent:
    reponse = phrase_avec_mot(fichier_pertinent, mot_pertinent)
    print(reponse if reponse else "Aucune phrase pertinente trouvée.")
else:
    print("Aucun mot pertinent trouvé dans la question.")
