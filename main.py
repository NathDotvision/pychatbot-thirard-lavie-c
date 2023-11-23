# -*- coding: utf-8 -*-
"""
PyChat Bot
Programme projet python semestre 01 L1 Efrei

Auteur : Téo Lavie & Wagner Thirard
Date : novembre 2023"""


# Importations des fonctions provenant des autres branches#
from fct_clean import nettoyer_et_enregistrer_fichiers_dossier_entier
from fct_names import afficher_noms_presidents_uniques

# Choix des options
def menu():
    print("Voici la liste des choix possibles :")
    print("1 : Afficher la liste des présidents dont les discours sont disponibles dans le programme \n2 : supprimer la ponctuation dans les fichiers des discours")
    choice = int(input("Quel est votre choix ? "))
    if choice == 1:
        if __name__ == "__main__":
            # Répertoire contenant les fichiers
            repertoire_entree = './speeches'
            # Extension des fichiers à analyser
            extension = '.txt'
            # Appeler la fonction pour afficher les noms uniques des présidents avec leurs prénoms
            afficher_noms_presidents_uniques(repertoire_entree, extension)

    elif choice == 2:
        if __name__ == "__main__":
            # Répertoire contenant les fichiers originaux
            repertoire_entree = './speeches'
            # Répertoire de sortie pour les fichiers nettoyés
            repertoire_sortie = './cleaned'

            # Nettoyer et enregistrer les fichiers du répertoire speeches dans le répertoire cleaned
            nettoyer_et_enregistrer_fichiers_dossier_entier(repertoire_entree, repertoire_sortie)

    else:
        print("This choice doesn't exist :/ \n")
        return menu()
menu()