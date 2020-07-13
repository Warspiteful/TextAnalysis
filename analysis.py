import os

import spacy
from functions import read_file, process_speeches, merge_speeches, get_president_sentences, get_presidents_sentences, most_frequent_words
from fileNames import text1, text2, text3, text4
import nltk, re
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer
from collections import Counter
import gensim


class textAnalyst():
    stop_words = stopwords.words('english')
    stop_words += ["like","want","know","ye","idk","i'm","really","kinda","ah","ok","oof","oh","mhm","hmm","also","lol","lmao","yeah","ooh"]
    def read_file(self,file_name):
        with open(file_name, 'r+', encoding='utf-8') as file:
            file_text = file.read()
        return file_text

    def process(self,text):
        sentence_tokenizer = PunktSentenceTokenizer()
        sentence_tokenized_speech = sentence_tokenizer.tokenize(text)
        word_tokenized_sentences = list()
        for sentence in sentence_tokenized_speech:
            word_tokenized_sentence = [word.lower().strip('.').strip('?').strip('!') for word in sentence.replace(",","").replace("-"," ").replace(":","").replace("~","").split()]
            word_tokenized_sentences.append(word_tokenized_sentence)
        return word_tokenized_sentences

    def most_frequent_words(self,list_of_sentences,num):
        all_words = [word for sentence in list_of_sentences for word in sentence if word not in stop_words]
        return Counter(all_words).most_common(num)

    def merge_texts(self,text_list):
        compiled = [process(read_file(text)) for text in text_list]
        all_sentences = list()
        for file in compiled:
            for sentence in file:
                all_sentences.append(sentence)
        return all_sentences

    def return_most_similar(self,sentence_list, word, num):
        model = gensim.models.Word2Vec(sentence_list, size=96, window=5, min_count=1, workers=2, sg=1)
        return model.most_similar(word,topn = num)


