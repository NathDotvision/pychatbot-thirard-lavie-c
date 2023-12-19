# -*- coding: utf-8 -*-
"""
PyChat Bot
Programme projet python semestre 01 L1 Efrei

Auteur : Téo Lavie & Wagner Thirard
Date : novembre-décembre 2023

Fichier : main.py
Fonction : Menu principal du programme
"""

# Importations des fonctions provenant des autres branches #
from fct_clean import nettoyer_et_enregistrer_fichiers_dossier_entier
from fct_names import afficher_noms_presidents_uniques
from fct_analyze import *
from fct_chatbot import *

# Répertoire contenant les discours
repertoire_entree = './speeches'
# Répertoire de sortie pour les fichiers nettoyés
repertoire_sortie = './cleaned'
# Nettoyer et enregistre les fichiers de speeches dans cleaned
nettoyer_et_enregistrer_fichiers_dossier_entier(repertoire_entree, repertoire_sortie)



# Choix des options
def afficher_presidents_disponibles():
    repertoire_entree = './speeches'
    extension = '.txt'
    afficher_noms_presidents_uniques(repertoire_entree, extension)



def menu_analyse():
    print("Bienvenue dans le sous-menu d'analyse : \n"
          "1 - Afficher la liste des mots les moins importants\n"
          "2 - Afficher les mots ayant le score TD-IDF le plus élevé\n"
          "3 - Afficher les mots les plus répétés par le président Chirac\n"
          "4 - Chercher un mot qu'un président a le plus répété \n"
          "5 - Le premier président à avoir parlé d'écologie ou de climat\n"
          "6 - Afficher les mots que tous les présidents ont évoqués \n"
          "0 - Retour au menu principal")
    # choix_sous_menu = int(input("Quel est votre choix ? "))
    choix_sous_menu = 3
    print("\n")

    if choix_sous_menu == 1:
        listniw()
    elif choix_sous_menu == 2:
        tdfmax()
    elif choix_sous_menu == 3:
        repete()
    elif choix_sous_menu == 4:
        occmot()
    elif choix_sous_menu == 5:
        climeco()
    elif choix_sous_menu == 6:
        communs()
    elif choix_sous_menu == 0:
        menu()
    else:
        print("This choice doesn't exist :/ \n")


def menu():
    while True:
        try:
            print("\n")
            print("Voici la liste des choix possibles :")
            print("1 : Afficher la liste des présidents dont les discours sont disponibles dans le programme \n"
                  "2 : Accéder au menu d'analyse \n3 : Accéder au ChatBot \n0 : Quitter le programme")
            choix_menu = int(input("Quel est votre choix ? "))
            print("\n")

            if choix_menu == 1:
                afficher_presidents_disponibles()
                menu()
            elif choix_menu == 2:
                menu_analyse()
            elif choix_menu == 3:
                print("Bienvenue dans le ChatBot !")
                chatbot()
                menu()
            elif choix_menu == 0:
                print("\nAu revoir !\n")
                break
            else:
                print("This choice doesn't exist :/ \n")
        except ValueError:
            print("Veuillez entrer un nombre entier.\n")
        except Exception as e:
            print(f"Une erreur s'est produite : {e}\n")


# Call the menu function to start the program
menu()
