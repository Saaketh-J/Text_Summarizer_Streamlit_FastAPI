import streamlit as st
from annotated_text import annotated_text
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx


def read_clean_text(text):
    text = text.split('.')
    sentences = []

    for sentence in text:
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop()
    return sentences


def sentence_similarity(sentence1, sentence2, stop_words=None):
    if stop_words is None:
        stop_words = []

    sentence1 = [word.lower() for word in sentence1]
    sentence2 = [word.lower() for word in sentence2]

    all_words = list(set(sentence1 + sentence2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for word in sentence1:
        if word in stop_words:
            continue
        vector1[all_words.index(word)] += 1

    for word in sentence2:
        if word in stop_words:
            continue
        vector2[all_words.index(word)] += 1

    return 1 - cosine_distance(vector1, vector2)


def similarity_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                similarity_matrix[i][j] = sentence_similarity(
                    sentences[i], sentences[j], stop_words)
    return similarity_matrix


def generate_summary(text, sentence_num):
    if(text != ""):
        if(len(read_clean_text(text)) >= sentence_num):
            pass
        else:
            return "Please choose a summarization length lesser than the number of available sentences."

    stop_words = stopwords.words('english')
    summarized_text = []

    sentences = read_clean_text(text)

    sentence_similarity_matrix = similarity_matrix(sentences, stop_words)

    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph, max_iter=1000)

    ranked_sentence = sorted(
        ((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    #print("Indexes of top ranked_sentence order are ", ranked_sentence)

    for i in range(sentence_num):
        summarized_text.append(" ".join(ranked_sentence[i][1]))

    return ".".join(summarized_text) + "."


def create_streamlit_app():
    text_input = st.text_area("Type a text to summarize")
    num_sentences = st.slider(
        "How many sentences would you like the summary to be?", 0, 10)
    summarize = st.button("Summarize")

    if(text_input != "" and summarize):
        if(len(read_clean_text(text_input)) >= num_sentences):
            summary = generate_summary(text_input, num_sentences)
            st.markdown(summary)
        else:
            st.text(
                "Please choose a summarization length lesser than the number of available sentences.")


create_streamlit_app()
