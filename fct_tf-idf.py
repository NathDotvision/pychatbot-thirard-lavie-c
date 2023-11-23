import os


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names



def calculer_occurrences_mot(chemin_fichier):
    list_f=list_of_files(chemin_fichier,'.txt')
    occurrences = {}
    for fichier in list_f:

        with open(chemin_fichier+fichier, 'r', encoding='utf-8') as file:
            contenu = file.read()
            for mot in contenu:
                    if mot in occurrences:
                        occurrences[mot] += 1
                    else:
                        occurrences[mot] = 1

    return occurrences
chemin_du_fichier = './cleaned/'
resultat_occurrences = calculer_occurrences_mot(chemin_du_fichier)

