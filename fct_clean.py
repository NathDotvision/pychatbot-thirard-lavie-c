import os
import string

def nettoyer_texte(texte):
    # Convertir le texte en minuscules
    texte = texte.lower()
    # Supprimer la ponctuation
    ponctuation = string.punctuation
    texte_sans_ponctuation = ''.join(char if char not in ponctuation else ' ' for char in texte)
    # Remplacer l'apostrophe et le tiret avec un traitement spécial
    texte_sans_ponctuation = texte_sans_ponctuation.replace("’", "").replace("-", "").replace("\n", " ")
    return texte_sans_ponctuation

def nettoyer_et_enregistrer_fichier_entier(chemin_entree, chemin_sortie):
    # Lire le contenu du fichier
    with open(chemin_entree, 'r', encoding='utf-8') as file:
        contenu = file.read()

    # Nettoyer le texte
    texte_nettoye = nettoyer_texte(contenu)

    # Écrire le texte nettoyé dans le nouveau fichier
    with open(chemin_sortie, 'w', encoding='utf-8') as file:
        file.write(texte_nettoye)

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