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
from TextWriter import write_file

class textAnalyst():

    def __init__(self, writing_list = None, text_file = None, list_of_text = None):
        if writing_list:
            print("Reading json file from \'" + writing_list[0] + "\'")
            print("Looking for messages from " + writing_list[1])
            print("Writing text to and reading text from \'" + writing_list[2] + "\'")
            write_file(writing_list[0],writing_list[1],writing_list[2])
            self.text = read_file(writing_list[2])
        if text_file:
            self.text = read_file(text_file)
        if hasattr(self,'text'):
            self.processed_text = self.process(self.text)
        if list_of_text:
            compiled = [self.process(read_file(text)) for text in list_of_text]
            all_sentences = list()
            for file in compiled:
                for sentence in file:
                    all_sentences.append(sentence)
            self.processed_text = all_sentences
            self.text = all_sentences
        if hasattr(self,'processed_text'):
            print("The 10 most frequent words in this text file are: ")
            for word in self.most_frequent_words(10):
                print(word[0])
            

    stop_words = stopwords.words('english')
    stop_words += ["like","want","know","ye","idk","i'm","really","kinda","ah","ok","oof","oh","mhm","hmm","also","lol","lmao","yeah","ooh","u"]
    
    def read_file(self,file_name):
        with open(file_name, 'r+', encoding='utf-8') as file:
            return file.read()

    def set_text(self,file_name):
        self.text = self.read_file(file_name)
        

    def process(self,text):
        sentence_tokenizer = PunktSentenceTokenizer()
        sentence_tokenized_speech = sentence_tokenizer.tokenize(text)
        word_tokenized_sentences = list()
        for sentence in sentence_tokenized_speech:
            word_tokenized_sentence = [word.lower().strip('.').strip('?').strip('!') for word in sentence.replace(",","").replace("-"," ").replace(":","").replace("~","").split()]
            word_tokenized_sentences.append(word_tokenized_sentence)
        return word_tokenized_sentences

    def most_frequent_words(self,num):
        all_words = [word for sentence in self.processed_text for word in sentence if word not in self.stop_words]
        return Counter(all_words).most_common(num)

    
    def print_word(self):
        print(self.text)

    def return_most_similar(self, word, num):
        model = gensim.models.Word2Vec(self.processed_text, size=96, window=5, min_count=1, workers=2, sg=1)
        return model.most_similar(word,topn = num)


