# -*- coding: utf-8 -*-
"""
PyChat Bot
Programme projet python semestre 01 L1 Efrei

Auteur : Téo Lavie & Wagner Thirard
Date : novembre 2023
"""


# Importations des fonctions provenant des autres branches #
from fct_clean import nettoyer_et_enregistrer_fichiers_dossier_entier
from fct_names import afficher_noms_presidents_uniques
from fct_analyze import *


# Choix des options
def menu():
    print("\n")
    print("Voici la liste des choix possibles :")
    print("1 : Afficher la liste des présidents dont les discours sont disponibles dans le programme \n2 : Supprimer la ponctuation dans les fichiers des discours\n3 : Accéder au menu d'analyse \n0 : Quitter le programme")
    choice = int(input("Quel est votre choix ? "))
    print("\n")
    if choice == 1:
        if __name__ == "__main__":
            # Répertoire contenant les discours
            repertoire_entree = './speeches'
            # Extension des fichiers à analyser
            extension = '.txt'
            # Appeler la fonction pour afficher les noms uniques des présidents avec leurs prénoms
            afficher_noms_presidents_uniques(repertoire_entree, extension)
            menu()

    elif choice == 2:
        if __name__ == "__main__":
            # Répertoire contenant les discours
            repertoire_entree = './speeches'
            # Répertoire de sortie pour les fichiers nettoyés
            repertoire_sortie = './cleaned'
            # Nettoyer et enregistre les fichiers de speeches dans cleaned
            nettoyer_et_enregistrer_fichiers_dossier_entier(repertoire_entree, repertoire_sortie)
            menu()


    elif choice == 3 :
        print("Bienvenue dans le sous-menu d'analyse : \n1 - Afficher la liste des mots les moins importants\n2 - Afficher les mots ayant le score TD-IDF le plus élevé\n3 - Afficher les mots les plus répétés par le président Chirac\n4 - les président qui ont parlé de nation\n5 - le premier président a avoir parlé d'écologie ou de climat\n6 - Afficher les mots que tout les présidents ont évoqués\n0 - Retour au menu principal")
        chan = int(input("Quel est votre choix ? "))
        print("\n")
        if chan == 1 :
            if __name__ == "__main__":
                listniw()
                print("\n")
                menu()
        elif chan == 2 :
            if __name__ == "__main__":
                tdfmax()
                print("\n")
                menu()
        elif chan == 3 :
            if __name__ == "__main__":
                repete()
                print("\n")
                menu()
        elif chan == 4 :
            if __name__ == "__main__":
                occnation()
                print("\n")
                menu()
        elif chan == 5 :
            if __name__ == "__main__":
                climeco()
                print("\n")
                menu()
        elif chan == 6 :
            if __name__ == "__main__":
                communs()
                print("\n")
                menu()
        elif chan == 0 :
            print("\n")
            menu()
        else :
            print("This choice doesn't exist :/ \n")
            return menu()

    elif choice == 0 :
        print("\nAu revoir !\n")
    else:
        print("This choice doesn't exist :/ \n")
        return menu()

menu()