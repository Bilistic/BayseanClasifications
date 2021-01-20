import os
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem  import WordNetLemmatizer

class Parser:
    def __init__(self, dataset):
        """
        Generates the object pulls in stop words and populates the amount of pos and neg reviews
        :param dataset: the main folder that contains pos and neg sub folders
        :param stopwords: the txt doc of stopwords
        """
        nltk.download('stopwords')
        nltk.download('punkt')
        nltk.download('wordnet')
        nltk.download('averaged_perceptron_tagger')
        self.lemz = WordNetLemmatizer()
        self.stopwords = set(stopwords.words('english'))
        self.v_c = set()
        self.c_p = 0
        self.c_n = 0
        self.p_d = self.folder_crawl(dataset+"\\pos", "POS")
        self.n_d = self.folder_crawl(dataset+"\\neg", "NEG")
        #self.p_d = self.frequency_Clean(self.p_d, 10)
        #self.n_d = self.frequency_Clean(self.n_d, 10)

    def read_txt(self, path, dictionary = {}, vocab = True):
        """
        reads in a text file and adds words to a dictioanry based on word and frequency
        :param path: path to the txt file
        :param dictionary: the dictionary the words are added to
        :param vocab: weather or not to add the new words to the vocab set
        :return:
        """
        with open(path, "r", encoding="utf8") as file:
            for line in file:
                for word in  word_tokenize(line):
                    word = re.sub("\W+", '', word).lower()
                    word = re.sub(r'[0-9]+', '', word)
                    if word:
                        #word = self.lemz.lemmatize(word)
                        if word not in self.stopwords:
                            dictionary[word] = dictionary.get(word, 0) + 1
                            if vocab:
                                self.v_c.add(word)
        return dictionary

    def folder_crawl(self, path, _class):
        """
        gets the words from a directory of txt files
        :param path: the directory to crawl through
        :param _class: weather it is pos or neg directory of files
        :return:
        """
        dictionary = {}
        listing = os.listdir(path)
        if _class is "POS":
            self.c_p = len(listing)
        else:
            self.c_n = len(listing)
        for file in listing:
            dictionary.update(self.read_txt(path+"\\"+file, dictionary))
        return dictionary

    def folder_files(self, path):
        """
        returns files from a directory
        :param path: the path of the directory
        :return:
        """
        return os.listdir(path)

    def frequency_Clean(self, dictionary, freq):
        """
        removes words of low frequency
        :param dictionary: the dictionary to clean
        :param freq: the frequency of which it will remove below
        :return: dictionary cleaned of low frequency words
        """
        list = {}
        for ind, x in enumerate(dictionary):
            if dictionary.get(x) > freq:
                list[x] = dictionary.get(x)
        return list
