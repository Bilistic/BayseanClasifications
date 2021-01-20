# BayseanClasifications

Machine Learning – Bayesian Classification
Joshua Nuttall

Contents

1 Introduction 

2 Basic Evaluation 

3 Research

# 1 Introduction

Following the Implementation of the naive Bayes algorithm for lab assignment:
”Machine Learning – Bayesian Classification”, the following is the corresponding
report.

# 2 Basic Evaluation

With my first attempt at cleaning data I used a simple regular expression to
remove all none alphanumerical values, I first broke a text doc line down to
each individual word. This returned words which included hyphen’s, underscores, commas, etc.. there was often cases where words where conjoined using
a hyphen, in order to remove these I split the word using the regular expression
”W+”. ”W” for all non alphanumerical values and ”+” for it to get multiple
instances, this will return a new array of strings that I can in turn parse and
check if it needs to be added to its designated dictionary.
With this technique of cleansing the data I received an initial accuracy of
50% without this I was receiving an accuracy that was negligible (20 : 980) for
a positive prediction, on a small data set.
Prior to cleaning the data via re.split() I used str.lower() to convert the
object to a lowercase instance this will make all my data uniform across.
This was all done during parsing of the directory and sorting of the files, to
increase speed of loading the files I sorted the reviews straight into a dictionary
oppose to looping twice and loading into the vocabulary (set) the second or first
time. this reduced the wait time, although still long for the large data set.
Over all I feel I made the code unnecessarily complicated as I struggled to
understand the concept initially (This later changed). The Method of cleansing
data I implemented was poor and gave insufficient matching of words, I considered stemming however was concerned at the cost this would have on word
accuracy and sentiment since we are merging words, ”didn’t” becomes ”did”
changing the context of the word etc. Overall the base implementation I have
created gave poor accuracy and I feel this is due to the poor cleaning of the
data.
After writing this I once again went back and re-wrote my code to try to
increase the accuracy this time replace the re.split with re.sub keeping it as a
string, I also used NLTK’s tokenizer to break down sentences and also implemented NLTK’s lemmatisation however I noticed an immediate drop in accuracy
so I later disabled this. I think the drop in accuracy was due to me judging all
lemmatised words as a noun, it is possible to use NLTK to figure out if the word
is a noun adjective etc, however this would of required a complete restructure
of my parsing class hence I opted to disable this feature.

# 3 Research

My first initial finding for increasing the accuracy of prediction was to remove
common words such as ”a”, ”and”, ”is”, etc... These words would skew the
probability you are calculating and have no relevance to sentiment in a review.
for this I went to https://algs4.cs.princeton.edu/35applications/stopwords.txt
and cleaned these words by adding a check when parsing the reviews. This
method raised my accuracy to 70% for positive test data and 60 for negative.
My next method I found useful for increasing accuracy was to remove words
that don’t have a high frequency from the training data, logic being that these
words are irrelevant to the data set. This method of further cleaning my words
seemed to of skewed the training data as I was now at a situation where positive
predictions had increased by 12% to 82% however negative had dropped by 5%.
Due to time limitations I was unable to implement more advanced methods
of refining my work. However when researching, certain methods did seem like
they would of been beneficial such as appending the word NOT prior to a word
based on the context the word is used in. an example of this being ”I didn’t like
this movie”, The word ”didn’t” completely changes the context of this sentence
meaning it would now class the words ”Like”, ”This”, ”Movie” as negative.
With this method the words would be transformed to ”Not Like”, ”Not This”,
”Not Movie” making these words completely different for comparison again the
positive sentence. [1]

Another method I come across to increase the accuracy of classification was
to boost the training data, Algorithms such as Ada Boost work on these simple
two class classification problems since not all words have the same weight (certain positive words are more positive than others). Each positive or negative
word acts as a ”weak” classifier, it works by assigning higher probability to parts
it does not classify correctly and focusing the new weak classifier on it. It does
this X times and combines the sum of all the results to form the weight of the
classifier. In order for this to be relevant in this context we look for the now
weighted words in a review and calculate the total weight of the weighted words
detected in order to determine the polarity of the review. [2]
As mentioned above stemming was considered however after research I concluded it was of no use for this application, I did come across lemmatisation
during the research of this. This process, although similar to stemming aims to
obtain the grammatically correct version of the word based on the context it is
used in. For the example ”saw”, Lemmatisation would attempt to return either
”see” or ”saw” in contrast stemming might just return ”s”. [3] [4]

References
[1] Daniel Jurafsky, James H. Martin, [Speech and Language Processing]
https://web.stanford.edu/~jurafsky/slp3/6.pdf
[2] Andres Cassinelli, Chih-Wei Chen, [ Sentiment Categorization with Machine
Learning Techniques], June 5, 2009
https://nlp.stanford.edu/courses/cs224n/2009/fp/16.pdf
[3] Christopher D. Manning, Prabhakar Raghavan, Hinrich Sch¨utze [Introduction to Information Retrieval], Cambridge University Press. 2008
https://nlp.stanford.edu/IR-book/html/htmledition/stemming
-and-lemmatization-1.html
[4] Sebastian Raschka [Naive Bayes and Text Classification], Oct 4, 2014
http://sebastianraschka.com/Articles/2014 naive bayes 1.html
