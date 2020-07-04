# -*- coding: utf-8 -*-
import pdb
import pickle
import nltk

from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder, QuadgramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures, QuadgramAssocMeasures

blacklist={'she', 'an', 'our', 'ours', 'both', "to", "ca", "n't", 'should', "weren't",
           'where', 'his', "'s", "'ll", "'d", "'m", 'when', "shouldn't", 'don','yourself',
           'its', "didn't", 'yours', 'shan', 'which', 'themselves',
           'isn', 'of', 'a', 'couldn', 'doesn', 'ma', 'my', 'herself',
           'more', 'hers', 'was', 'it', 'him', 'there',
           'ourselves', 'being', "mightn't", 'why', 'before', 'but',
           'by', 'they', 'most', 'you', 'while', 'and', 'were', 'needn',
           "you've", 'only', 'wouldn', "she's", 'yourselves', 'no', 'very',
           'now', 'will', 'll', 'wasn', "aren't", 'shouldn',
           'the', 'ain', 'their', 'or', 'we', 'i', "mustn't", 'myself',
           'your', 'because', 'any', 'same', 'too', "wouldn't",
           'those', 'all', 'her', 'them', 'how', 'd', "you're", 'this', 'didn',
           'am', 'can', 'what', 'once', 'whom', 'is', 'few', 'mustn', 'are',
           "it's", 'himself', "wasn't", 'off', 'if',
           'm', "isn't", 'for', "you'd", 'so', 'that', "you'll", 'aren', 's',
           're', 'won', "that'll", 'y', 'been', 'these', "couldn't", 'some',
           'own', 'he', "needn't", 'me', "won't", 'weren', 'mightn', 'who',
           'itself', 'other', 'theirs', 'be', 'just', 'not', "should've",
           'again', ',', '.','!', '?','...','-',':','$','%','#'}

MWElist={'VID', 'LVC.full', 'LVC.cause', 'VPC.full', 'VPC.semi', 'IAV', 'MVC'}


def myfilter_list(blacklist):
    def myfilter(word_pos):
        #pdb.set_trace()
        if word_pos[0].lower() in blacklist:
            return True
        elif word_pos[1] in ["NUM","PROPN","PUNCT","X"]:
            return True
        else:
            return False
        
    return myfilter

#function to filter for Verb/Noun bigrams
#Bigrams: (Verb, Noun), (Noun, Verb)
def rightTypesBi(bigram0, bigram1):
    #pdb.set_trace()
    first_type = ('VERB')
    second_type = ('NOUN')
    if bigram0[1] in first_type and bigram1[1] in second_type:
        return False # keep this bigram
    else:
        return True # filter it out

#function to filter for trigrams
#Trigrams: (Verb, Anything, Noun)
def rightTypesTri(trigram0,trigram1,trigram2):
    #pdb.set_trace()
    first_type = ('VERB')
    third_type = ('NOUN')
    if trigram0[1] in first_type and trigram2[1] in third_type:
        return False
    else:
        return True



# open the pickled corpus file
#file = open('corpus_test', 'rb')
file = open('train_cupt', 'rb')

# load information from that file
data = pickle.load(file)
words=data[0]
tagged_words=data[1]
gold=data[2]
mycorpus=data[3]

# close the file
file.close()

try:

    #pdb.set_trace()
    # set filter
    myfilter = myfilter_list(blacklist)

    # NLTK COLLOCATIONS MEASURES
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    trigram_measures = nltk.collocations.TrigramAssocMeasures()

    # find Bigram collocations
    bigram_collocation = BigramCollocationFinder.from_words(tagged_words,window_size = 4)
    trigram_collocation = TrigramCollocationFinder.from_words(tagged_words,window_size = 4)
    
    # apply filters
    bigram_collocation.apply_word_filter(myfilter)
    bigram_collocation.apply_freq_filter(2)

    trigram_collocation.apply_word_filter(myfilter)
    trigram_collocation.apply_freq_filter(2)
    
    #pdb.set_trace()
    
    VMWE=[]
    for i in [2,3]:
        # get N-Best results
        if i==2:
            bigram_collocation.apply_ngram_filter(rightTypesBi)
            nbest=bigram_collocation.nbest(bigram_measures.likelihood_ratio,10)
            #nbest=bigram_collocation.nbest(bigram_measures.pmi,100)
            #nbest=bigram_collocation.nbest(bigram_measures.raw_freq,300)
            #nbest=bigram_collocation.nbest(bigram_measures.chi_sq,200)
        elif i==3:
            trigram_collocation.apply_ngram_filter(rightTypesTri)
            nbest=trigram_collocation.nbest(trigram_measures.likelihood_ratio,10)
            #nbest=trigram_collocation.nbest(trigram_measures.raw_freq,300)
        else:
            break

        #print('\nCOLLOCATION NBest:\n')
        print(nbest)
        VMWE.append(ngram)
##        print('\nVERBAL MWEs:\n')
##        # select verbal MWE in the nbest
##        for ngram in nbest:
##            #pdb.set_trace()
##            if len(ngram)==2 and rightTypesBi(ngram): 
##                print(ngram[0][0],ngram[1][0],';')
##                VMWE.append(ngram)
##            elif len(ngram)==3 and rightTypesTri(ngram): 
##                print(ngram[0][0],ngram[1][0],ngram[2][0],';')
##                VMWE.append(ngram)
            
except:
    print("BREAK!")


### open a file to store the data
##file = open('ngram', 'wb')
##
##data=VMWE
##
### dump information to that file
##pickle.dump(data, file)
##
### close the file
##file.close()
