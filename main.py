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
    print("Voici la liste des choix possibles :")
    print("1 : Afficher la liste des présidents dont les discours sont disponibles dans le programme \n2 : Supprimer la ponctuation dans les fichiers des discours\n3 : Accéder au menu d'analyse")
    choice = int(input("Quel est votre choix ? "))
    if choice == 1:
        if __name__ == "__main__":
            # Répertoire contenant les discours
            repertoire_entree = './speeches'
            # Extension des fichiers à analyser
            extension = '.txt'
            # Appeler la fonction pour afficher les noms uniques des présidents avec leurs prénoms
            afficher_noms_presidents_uniques(repertoire_entree, extension)

    elif choice == 2:
        if __name__ == "__main__":
            # Répertoire contenant les discours
            repertoire_entree = './speeches'
            # Répertoire de sortie pour les fichiers nettoyés
            repertoire_sortie = './cleaned'
            # Nettoyer et enregistre les fichiers de speeches dans cleaned
            nettoyer_et_enregistrer_fichiers_dossier_entier(repertoire_entree, repertoire_sortie)


    elif choice == 3 :
        if not os.path.exists(dossier_cleaned) or not os.path.isdir(dossier_cleaned):
            print("Veuillez d'abord utiliser la fonctionnalité de nettoyage du texte.")
            menu()
        print("Bienvenue dans le sous-menu d'analyse : \n1 - Afficher la liste des mots les moins importants\n2 - Afficher les mots ayant le score TD-IDF le plus élevé\n3 - Afficher les mots les plus répétés par le président Chirac\n4 - les président qui ont parlé de nation\n5 - le premier président a avoir parlé d'écologie ou de climat\n6 - Afficher les mots que tout les présidents ont évoqués\n0 - Retour au menu principal")
        chan = int(input("Quel est votre choix ? "))
        if chan == 1 :
            if __name__ == "__main__":
                listniw()
        elif chan == 2 :
            if __name__ == "__main__":
                tdfmax()
        elif chan == 3 :
            if __name__ == "__main__":
                repete()
        elif chan == 4 :
            if __name__ == "__main__":
                occnation()
        elif chan == 5 :
            if __name__ == "__main__":
                climeco()
        elif chan == 6 :
            if __name__ == "__main__":
                communs()
        elif chan == 0 :
            menu()
        else :
            print("This choice doesn't exist :/ \n")
            return menu()

    else:
        print("This choice doesn't exist :/ \n")
        return menu()

menu()
