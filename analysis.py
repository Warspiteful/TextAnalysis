from fileNames import text1, text2, text3, text4
import sys
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer
from collections import Counter
import gensim
from TextWriter import write_file
import ntpath

class textAnalyst():

    def __init__(self, user_file):
        self.set_text(user_file)
        
    stop_words = stopwords.words('english')
    stop_words += ["like","want","know","ye","idk","i'm","really","kinda","ah","ok","oof","oh","mhm","hmm","also","lol","lmao","yeah","ooh","u"]
    text_files = []

    def read_file(self,file_name):
        try:
            
            with open(file_name, 'r+', encoding='utf-8') as file:
                file = file.read()
            self.text_files.append(ntpath.basename(file_name))
            return file
        except Exception:
            if len(self.text_files) > 0:
                print("Invalid File Path")
            else:
                raise NameError("Invalid File Path") from None

    def append_text(self,text_file):
        pass

    def print_text_files(self):
        print("Included in this model:")
        for file in self.text_files:
            print(ntpath.basename(file))



    def set_text(self,user_file):
        if type(user_file) == list:
            if user_file[0][-4:] == 'json':
                
                if len(user_file) > 3:
                    raise TypeError("Too many arguments provided in JSon list")
                    sys.exit()
                print("Reading json file from \'" + user_file[0] + "\'")

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
                self.text = self.read_file(user_file[2])
                self.processed_text = self.process(self.text)
            else:
                text = [self.read_file(text) for text in user_file]
                self.text = "".join(text)
                compiled = [self.process(texts) for texts in text]
                all_sentences = list()
                for file in compiled:
                    for sentence in file:
                        all_sentences.append(sentence)
                self.processed_text = all_sentences
            
        elif type(user_file) == str:
            print("Reading from " + ntpath.basename(user_file))
            self.text = self.read_file(user_file)
            self.processed_text = self.process(self.text)
        else:
            raise Exception("Invalid Input.")


        if hasattr(self,'processed_text'):
            print("The 10 most frequent words in this text file are: ")
            for word in self.most_frequent_words(10):
                print(word[0])
        
        

    def process(self,text):
        sentence_tokenizer = PunktSentenceTokenizer()
        sentence_tokenized_speech = sentence_tokenizer.tokenize(text)
        word_tokenized_sentences = list()
        for sentence in sentence_tokenized_speech:
            word_tokenized_sentence = [word.lower().strip('.').strip('?').strip('!') for word in sentence.replace(",","").replace("-"," ").replace(":","").replace("~","").split()]
            word_tokenized_sentences.append(word_tokenized_sentence)
        return word_tokenized_sentences

    def most_frequent_words(self,n):
        all_words = [word for sentence in self.processed_text for word in sentence if word not in self.stop_words]
        return Counter(all_words).most_common(n)

    
    def print_word(self):
        print(self.text)

    def return_most_similar(self, word, num):
        model = gensim.models.Word2Vec(self.processed_text, size=96, window=5, min_count=1, workers=2, sg=1)
        return model.most_similar(word,topn = num)


