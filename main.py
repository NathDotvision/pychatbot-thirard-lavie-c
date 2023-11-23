# -*- coding: utf-8 -*-
"""
PyChat Bot
Programme projet python semestre 01 L1 Efrei

Auteur : Téo Lavie & Wagner Thirard
Date : novembre 2023"""


# Importations de modules externes#


from fct_names import afficher_noms_presidents_uniques, nettoyer_et_enregistrer_fichiers_dossier_entier

if __name__ == "__main__":
    # Répertoire contenant les fichiers originaux
    repertoire_entree = './speeches'
    # Répertoire de sortie pour les fichiers nettoyés
    repertoire_sortie = './cleaned'
    # Extension des fichiers à considérer
    extension = '.txt'

    # Nettoyer et enregistrer les fichiers du répertoire speeches dans le répertoire cleaned
    nettoyer_et_enregistrer_fichiers_dossier_entier(repertoire_entree, repertoire_sortie)

    # Appeler la fonction pour afficher les noms uniques des présidents
    afficher_noms_presidents_uniques(repertoire_sortie, extension)

