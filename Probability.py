import math

class Probability:
    def __init__(self, pos, neg, pos_r, neg_r, vc):
        self.pos = pos
        self.neg = neg
        self.pos_R = pos_r
        self.neg_R = neg_r
        self.vc = vc
        self.p_p = self.generate_prob(pos)
        self.p_n = self.generate_prob(neg)

    def class_probability(self, _class):
        """
        Gets P(c) - prob of class
        :param _class: POS || NEG
        :return:
        """
        if _class is "POS":
            return math.log(self.pos_R / (self.pos_R+self.neg_R))
        else:
            return math.log(self.neg_R / (self.pos_R+self.neg_R))

    def word_probability(self, w_f, w_c, v_c):
        """
        Gets the probability of a word
        :param w_f: word frequency
        :param w_c: number of words (include dupe) in dictionary
        :param v_c: number of unique words in vocabulary
        :return: probability
        """
        return w_f + 1 / (w_c + v_c + 1)

    def naive_bayes(self, review):
        """
        gets the probability of the review being negative and positive the greater value being the polarity of the review
        log(P(c)) + sum of the log of probability of each word in the document
        :param review: the review the work on
        :return: True || False (Positive : Negative)
        """
        _n_probability = self.class_probability("NEG")#log(P(c))
        _p_probability = self.class_probability("POS")#log(P(c))
        for word in review:
            _n_probability += (math.log(self.get_prob(word, self.p_n, self.neg)) * review.get(word, 1))
            _p_probability += (math.log(self.get_prob(word, self.p_p, self.pos)) * review.get(word, 1))
        print(str(_p_probability), " : ", str(_n_probability))
        return (_p_probability > _n_probability)

    def get_prob(self, word, dic_p, dic_d):
        """
        Gets the probability of a word.
        if the word has not been previously calculated it will calculate based on the provided dictionary
        :param word: the word to find
        :param dic_p: dictionary with word and probabilities
        :param dic_d: dictionary with word and frequency
        :return: probability
        """
        if word in dic_p:
            return dic_p.get(word)
        else:
            return self.word_probability(dic_d.get(word,0), sum(dic_d.values()), len(self.vc))

    def generate_prob(self, dic):
        """
        Generates a dictioanry of word : probability
        :param dic: the dictionary to get words from
        :return: dictionary - word : probability
        """
        print("Generating Probabilities...")
        dictionary = {}
        for x in dic:
            dictionary[x] = self.word_probability(dic.get(x,0), sum(dic.values()), len(self.vc))
        return dictionary
