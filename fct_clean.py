# -*- coding: utf-8 -*-
"""
PyChat Bot
Programme projet python semestre 01 L1 Efrei

Auteur : Téo Lavie & Wagner Thirard
Date : novembre-décembre 2023

Fichier : fct_clean.py
Fonction : Fonctions de nettoyage des discours
"""


import os
import string

"""
Récupère la liste des noms de fichiers avec une certaine extension dans un répertoire donné.

paramètre directory: Le chemin du répertoire à parcourir
paramètre extension: L'extension des fichiers à rechercher
return: Une liste contenant les noms des fichiers avec l'extension spécifiée
"""
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

"""
Nettoie un texte en le convertissant en minuscules en supprimant la ponctuationl'apostrophe le tiret et les retours à la ligne.

paramètre texte: Le texte à nettoyer
return: Le texte nettoyé
"""
def nettoyer_texte(texte):
    # Convertir le texte en minuscules
    texte = texte.lower()
    # Supprimer la ponctuation
    ponctuation = string.punctuation
    texte_sans_ponctuation = ''.join(char if char not in ponctuation else ' ' for char in texte)
    # Remplacer l'apostrophe, le tiret et le retour à la ligne
    texte_sans_ponctuation = texte_sans_ponctuation.replace("’", "").replace("-", " ").replace("\n", "")
    return texte_sans_ponctuation

"""
Nettoie le contenu d'un fichier puis écrit le texte nettoyé dans un nouveau fichier.

paramètre chemin_entree: Le chemin du fichier d'entrée
paramètre chemin_sortie: Le chemin du fichier de sortie nettoyé
"""
def nettoyer_et_enregistrer_fichier_entier(chemin_entree, chemin_sortie):
    # Lire le contenu du fichier
    with open(chemin_entree, 'r', encoding='utf-8') as file:
        contenu = file.read()

    # Nettoyer le texte
    texte_clean = nettoyer_texte(contenu)

    # Écrire le texte nettoyé dans le nouveau fichier
    with open(chemin_sortie, 'w', encoding='utf-8') as file:
        file.write(texte_clean)

"""
Nettoie tous les fichiers d'un répertoire et enregistre les versions nettoyéesdans un répertoire de sortie.

paramètre repertoire_entree: Le chemin du répertoire d'entrée
paramètre repertoire_sortie: Le chemin du répertoire de sortie
"""
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
