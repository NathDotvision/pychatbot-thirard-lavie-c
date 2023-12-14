import string
from fct_tf_idf import tout_mots
qst = input("Quelle est votre question ? ")
def tokenqst(qst):
    # Supprimer la ponctuation
    texte_question = qst.translate(str.maketrans('', '', string.punctuation))
    # Convertir en minuscules
    texte_question = texte_question.lower()
    # Diviser en mots
    mots_question = texte_question.split()
#    mots_question = mots_question.replace("’", "").replace("-", " ").replace("\n", "")

#    mots_vides = ["le", "la", "les", "de", "des", "du", "et", "ou", "en", "à"]
#    mots_question = [mot for mot in mots_question if mot not in mots_vides]
    print(mots_question)
    return mots_question

def find_common_terms(qst):
    # Créer un ensemble de tous les mots uniques dans le corpus
    corpus_words = set(tout_mots)

    # Créer un ensemble de tous les mots uniques dans la question
    question_words = set(tokenqst(qst))

    # Trouver l'intersection de ces deux ensembles
    common_words = corpus_words.intersection(question_words)
    print(common_words)
    return common_words

from fct_tf_idf import idf_scores

def calculer_vecteur_tf_idf_qst(qst):
    # Tokeniser la question
    mots_question = tokenqst(qst)

    # Calculer le score TF pour chaque mot dans la question
    tf_scores = {}
    for mot in mots_question:
        if mot in tf_scores:
            tf_scores[mot] += 1
        else:
            tf_scores[mot] = 1

    for mot in tf_scores:
        tf_scores[mot] /= len(mots_question)

    # Initialiser le vecteur TF-IDF avec des zéros pour tous les mots du corpus
    tf_idf_vecteur = {mot: 0 for mot in tout_mots}

    # Calculer le score TF-IDF pour chaque mot dans la question
    for mot, tf in tf_scores.items():
        if mot in idf_scores:
            tf_idf_vecteur[mot] = tf * idf_scores[mot]

    # Filtrer le dictionnaire pour ne garder que les mots dont le score est différent de 0
    tf_idf_vecteur = {mot: score for mot, score in tf_idf_vecteur.items() if score != 0}
    print(tf_idf_vecteur)
    return tf_idf_vecteur

calculer_vecteur_tf_idf_qst(qst)