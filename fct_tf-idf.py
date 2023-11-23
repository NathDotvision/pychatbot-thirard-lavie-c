
import string

def nettoyer_texte(texte):
    # Supprime la ponctuation et met le texte en minuscules
    texte = texte.lower()
    texte = texte.translate(str.maketrans("", "", string.punctuation))
    return texte

def calculer_tf(texte):
    # Nettoie le texte
    texte_nettoye = nettoyer_texte(texte)

    # Divise la chaîne de caractères nettoyée en mots
    mots = texte_nettoye.split()

    # Initialise le dictionnaire pour stocker les occurrences de chaque mot
    occurrences = {}

    # Parcourt chaque mot dans la liste de mots
    for mot in mots:
        # Utilise la méthode get() pour récupérer la valeur actuelle de l'occurrence du mot,
        # ou initialise à zéro s'il n'existe pas encore dans le dictionnaire
        occurrences[mot] = occurrences.get(mot, 0) + 1

    # Retourne le dictionnaire des occurrences
    return occurrences

# Exemple d'utilisation
texte_exemple = "Ceci est un exemple. Un exemple simple."

# Appelle la fonction avec le texte d'exemple
occurrences_resultat = calculer_tf(texte_exemple)

# Affiche le résultat
print("Occurrences de chaque mot dans le texte après nettoyage :")
for mot, occurrence in occurrences_resultat.items():
    print(f"{mot}: {occurrence}")