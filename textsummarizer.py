import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
from nltk.tokenize import sent_tokenize
import numpy as np
import networkx as nx


def read_article(text):
    sentences = []
    sentences = sent_tokenize(text)
    for sentence in sentences:
        sentence.replace("[^a-zA-Z0-9]", " ")
    return sentences


def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
    all_words = list(set(sent1 + sent2))
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
    for w in sent1:
        if w not in stopwords:
            vector1[all_words.index(w)] += 1
    for w in sent2:
        if w not in stopwords:
            vector2[all_words.index(w)] += 1
    return 1-cosine_distance(vector1, vector2)


def build_similarity_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 != idx2:
                similarity_matrix[idx1][idx2] = sentence_similarity(
                    sentences[idx1],
                    sentences[idx2],
                    stop_words,
                )
    return similarity_matrix


def generate_summary(text, top_n):
    nltk.download('stopwords')
    nltk.download('punkt')
    stop_words = stopwords.words('english')
    summarize_text = []
    sentences = read_article(text)
    sentence_similarity_matrix = build_similarity_matrix(sentences, stop_words)
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)
    ranked_sentences = sorted(
        ((scores[i], s) for i,
            s in enumerate(sentences)),
        reverse=True,
    )
    for i in range(top_n):
        summarize_text.append(ranked_sentences[i][1])
    return " ".join(summarize_text), len(sentences)
