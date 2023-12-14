import string
import math
from fct_tf_idf import tout_mots, list_f, tfidf_matrice
qst = ("mesdames les")

def matrice_to_dict(tfidf_matrice, tout_mots):
    tfidf_dict = {}
    for i in range(len(tout_mots)):
        tfidf_dict[tout_mots[i]] = tfidf_matrice[i]
    return tfidf_dict

tfidf_dict = matrice_to_dict(tfidf_matrice, tout_mots)

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
    return list(common_words)

from fct_tf_idf import idf_scores

def calculer_vecteur_tf_idf_qst(qst):
    # Tokeniser la question
    mots_question = tokenqst(qst)
    termes_communs = find_common_terms(qst)

    # Calculer le score TF pour chaque mot dans la question
    tf_scores = {}
    for mot in termes_communs:
        tf_scores[mot] = mots_question.count(mot) / len(mots_question)

    # Utiliser les scores IDF du corpus pour les mots de la question
    tf_idf_scores = {}
    for mot, tf in tf_scores.items():
        if mot in idf_scores:  # Ensure the word is in the idf_scores dictionary
            tf_idf_scores[mot] = tf * idf_scores[mot]

    # Transform the dictionary into a list of TF-IDF scores
    tf_idf_list = list(tf_idf_scores.values())

    print(tf_idf_list)
    return tf_idf_list

tfidf_qst = calculer_vecteur_tf_idf_qst(qst)


def dot_product(A, B):
    return sum(float(a)*float(b) for a, b in zip(A, B))

def norm(vector):
    return math.sqrt(sum(float(x)**2 for x in vector))

def cosine_similarity(A, B):
    norm_A = norm(A)
    norm_B = norm(B)
    if norm_A != 0 and norm_B != 0:
        return dot_product(A, B) / (norm_A * norm_B)
    else:
        return 0

def most_relevant_document(tfidf_matrix, tfidf_vector_qst, list_f):
    # Ensure tfidf_vector_qst is a list of floats
    tfidf_vector_qst = [float(i) for i in tfidf_vector_qst]
    similarities = [cosine_similarity(tfidf_vector_qst, [float(i) for i in tfidf_vector]) for tfidf_vector in tfidf_matrix]
    max_index = similarities.index(max(similarities))
    return list_f[max_index]


relevant_document = most_relevant_document(tfidf_matrice, tfidf_qst, list_f)

def generate_response(tfidf_vector_qst, relevant_document):
    max_tf_idf_word = max(tfidf_vector_qst)
    with open('cleaned/' + relevant_document, 'r') as file:
        text = file.read()
        print(type(text))
        sentences = text.split(' ')
        print(type(sentences))
    for sentence in sentences:
        if max_tf_idf_word in sentence:
            return sentence.strip().capitalize() + '.'
    return 1

response = generate_response(tfidf_qst, relevant_document)
print(response)