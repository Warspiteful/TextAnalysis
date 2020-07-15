from fileNames import text1, text2, text3, text4
import sys
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer
from collections import Counter
import gensim
from TextWriter import write_file
from nltk import pos_tag
import ntpath
import string
import re

class textAnalyst():
    stop_words = stopwords.words('english')
    text_files = []

    text = ""
    processed_text = []
    text_fields = [text,processed_text]

    def __init__(self, user_file):
        self.set_stopwords()
        self.append_text(user_file)
      
        
    def set_stopwords(self):
        self.stop_words += ['']
        try:
            with open('stopwords.txt', 'r+', encoding='utf-8') as file:
                self.stop_words += self.process(file.read())[0]
        except:
            writer = open("stopwords.txt","a")
            writer.close() 
    
    def get_stopwords(self):
        return self.stop_words

    def read_file(self,file_name):
        try:
            
            with open(file_name, 'r+', encoding='utf-8') as file:
                file = file.read()
            self.text_files.append(file_name)
            return file
        except Exception:
            if len(self.text_files) > 0:
                print("Invalid File Path")
            else:
                raise NameError("Invalid File Path") from None
        

    def print_text_files(self):
        print("\nIncluded in this model:")
        for file in self.text_files:
            print(ntpath.basename(file))

    def remove_text_file(self,file_name):
        
        for file in enumerate(self.text_files):
            if file_name in ntpath.basename(file[1]):    
                print("\nRemoving " + ntpath.basename(file_name) + " from the model.")
                del self.text_files[file[0]]
                self.text = ""
                self.processed_text = []
                self.append_text(self.text_files)
                return
        print("File not found")


    def find_favorite_pos(self, pos):
        
        pos_words = []
        all_words = [word for sentence in self.processed_text for word in sentence if word not in self.stop_words and word]
        tagged_words = pos_tag(all_words)

        for token in tagged_words:
            if token[1].startswith(pos):
                pos_words.append(token[0])

        return Counter(pos_words).most_common(1)[0]
      

    def append_text(self,user_file):
        if type(user_file) == list:
            if user_file[0][-4:] == 'json':
                
                if len(user_file) > 3:
                    raise TypeError("Too many arguments provided in JSon list")
                    sys.exit()
                print("\nReading json file from \'" + user_file[0] + "\'")

                try:
                    print("Looking for messages from " + user_file[1])
                except Exception:
                    raise NameError('User Missing. Please try again') from None
                    sys.exit()
                try:
                    print("Writing text to and reading text from \'" + ntpath.basename(user_file[2]) + "\'")
                except Exception:
                    print("No text file path provided. Created \'default.txt\' in local directory.")
                    user_file[2] = ( 'default.txt')
                write_file(user_file[0],user_file[1],user_file[2])
                self.text += self.read_file(user_file[2])
                self.processed_text += self.process(self.text)
            else:
                print("\nReading from:\n" + "\n".join([ntpath.basename(file) for file in user_file]))
                text = [self.read_file(text) for text in user_file]
                self.text += "".join(text)
                compiled = [self.process(texts) for texts in text]
                all_sentences = list()
                for file in compiled:
                    for sentence in file:
                        all_sentences.append(sentence)
                self.processed_text += all_sentences
            
        elif type(user_file) == str:
            print("\nReading from " + ntpath.basename(user_file))
            self.text += self.read_file(user_file)
            self.processed_text += self.process(self.text)
        else:
            raise Exception("Invalid Input.")

        
        

    def process(self,text):
        
        sentence_tokenizer = PunktSentenceTokenizer()
        sentence_tokenized_speech = sentence_tokenizer.tokenize(text)
        word_tokenized_sentences = list()
        for sentence in sentence_tokenized_speech:
            word_tokenized_sentence = [word.lower().strip('.').strip('?').strip('!').strip(string.digits) for word in sentence.replace(",","").replace("-"," ").replace(":","").replace("~","").replace("(", "").replace(")", "").split()]
            word_tokenized_sentences.append(word_tokenized_sentence)
        return word_tokenized_sentences

    def most_frequent_words(self,n):
        all_words = [word for sentence in self.processed_text for word in sentence if word not in self.stop_words]
        return Counter(all_words).most_common(n)

    
    def print_word(self):
        print(self.text)

    def print_processed(self):
        print(self.processed_text)

    def return_most_similar(self, word, num):
        model = gensim.models.Word2Vec(self.processed_text, size=96, window=5, min_count=1, workers=2, sg=1)
        return model.most_similar(word,topn = num)


