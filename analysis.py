import os

import spacy
from functions import read_file, process_speeches, merge_speeches, get_president_sentences, get_presidents_sentences, most_frequent_words
from fileNames import text1, text2
import nltk, re
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer
from collections import Counter

stop_words = stopwords.words('english')
stop_words += ["like","want","know","ye","idk","i'm","really"]
def read_file(file_name):
    with open(file_name, 'r+', encoding='utf-8') as file:
        file_text = file.read()
    return file_text

def process(text):
    sentence_tokenizer = PunktSentenceTokenizer()
    sentence_tokenized_speech = sentence_tokenizer.tokenize(text)
    word_tokenized_sentences = list()
    for sentence in sentence_tokenized_speech:
      word_tokenized_sentence = [word.lower().strip('.').strip('?').strip('!') for word in sentence.replace(",","").replace("-"," ").replace(":","").replace("~","").split()]
      word_tokenized_sentences.append(word_tokenized_sentence)
    return word_tokenized_sentences

def most_frequent_words(list_of_sentences):
    all_words = [word for sentence in list_of_sentences for word in sentence if word not in stop_words]
    return Counter(all_words).most_common(100)

text = read_file(text2)
text = process(text)

word = most_frequent_words(text)
for w in word:
    print(w)

