def calculer_occurrences_mot_dans_fichier(chemin_fichier):
    for i in range
    occurrences = {}

    with open(chemin_fichier, 'r', encoding='utf-8') as file:
        contenu = file.read()
        for mot in mots:
                if mot in occurrences:
                    occurrences[mot] += 1
                else:
                    occurrences[mot] = 1

        return occurrences
chemin_du_fichier = './cleaned/'
resultat_occurrences = calculer_occurrences_mot(chemin_du_fichier)

