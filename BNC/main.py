# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join
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
           'again', ',', '.','!', '?','...','-',':','$','%','#','fig.','police'}

MWElist={'VID', 'LVC.full', 'LVC.cause', 'VPC.full', 'VPC.semi', 'IAV', 'MVC'}


def myfilter_list(blacklist):
    def myfilter(word_pos):
        #pdb.set_trace()
        if word_pos[0].lower() in blacklist:
            return True
        elif word_pos[1] in ["NUM","PROPN","PUNCT","X","PRON","STOP","UNC"]:
            return True
        else:
            return False
        
    return myfilter

#function to filter for Verb/Noun bigrams
#Bigrams: (Verb, Noun), (Noun, Verb)
def rightTypesBi(bigram0, bigram1):
    #pdb.set_trace()
    first_type = ('VERB','VBB', 'VBD', 'VBG', 'VBI', 'VBN', 'VBZ', 'VDB', 'VDD', 'VDG', 'VDI', 'VDN', 'VDZ', 'VHB', 'VHD', 'VHG', 'VHI', 'VHN', 'VHZ', 'VM0', 'VVB', 'VVD', 'VVG', 'VVI', 'VVN', 'VVZ', 'VVD-VVN', 'VVN-VVD')
    second_type = ('NOUN','SUBST','NN0', 'NN1', 'NN2', 'ONE', 'ZZ0') #NP0, NN1-NP0, NP0-NN1
    if bigram0[1] in first_type and bigram1[1] in second_type:
        return False # keep this bigram
    else:
        return True # filter it out

#function to filter for trigrams
#Trigrams: (Verb, Anything, Noun)
def rightTypesTri(trigram0,trigram1,trigram2):
    #pdb.set_trace()
    first_type = ('VERB','VBB', 'VBD', 'VBG', 'VBI', 'VBN', 'VBZ', 'VDB', 'VDD', 'VDG', 'VDI', 'VDN', 'VDZ', 'VHB', 'VHD', 'VHG', 'VHI', 'VHN', 'VHZ', 'VM0', 'VVB', 'VVD', 'VVG', 'VVI', 'VVN', 'VVZ', 'VVD-VVN', 'VVN-VVD')
    third_type = ('NOUN','SUBST','NN0', 'NN1', 'NN2', 'ONE', 'ZZ0') #NP0, NN1-NP0, NP0-NN1
    if trigram0[1] in first_type and trigram2[1] in third_type:
        return False
    else:
        return True

strPath='C:/mydesktop/BNC/myscripts/wds_tgwds_bySubDir/'
listFile = listdir(strPath)

for strFile in listFile:
    # open the pickled corpus file
    file = open(strPath+strFile, 'rb')
    data = pickle.load(file)
    all_tagged_words = data[1]
    file.close()
    print(strFile)
    #pdb.set_trace()

    tagged_words = [j for sub in all_tagged_words for j in sub]
    try:

        #pdb.set_trace()
        # set filter
        myfilter = myfilter_list(blacklist)
        #pdb.set_trace()
        
        VMWE=[]
        for i in [2]: # [2] [3] or [2,3]
            # get N-Best results
            if i==2:
                bigram_measures = nltk.collocations.BigramAssocMeasures() # NLTK COLLOCATIONS MEASURES
                bigram_collocation = BigramCollocationFinder.from_words(tagged_words,window_size = 4)# find Bigram collocations
                bigram_collocation.apply_word_filter(myfilter) # apply filters
                bigram_collocation.apply_freq_filter(2)
                bigram_collocation.apply_ngram_filter(rightTypesBi)
                nbest=bigram_collocation.nbest(bigram_measures.likelihood_ratio,10)
                #nbest=bigram_collocation.nbest(bigram_measures.pmi,100)
                #nbest=bigram_collocation.nbest(bigram_measures.raw_freq,300)
                #nbest=bigram_collocation.nbest(bigram_measures.chi_sq,200)
            elif i==3:
                trigram_measures = nltk.collocations.TrigramAssocMeasures()
                trigram_collocation = TrigramCollocationFinder.from_words(tagged_words,window_size = 4)
                trigram_collocation.apply_word_filter(myfilter)
                trigram_collocation.apply_freq_filter(2)
                trigram_collocation.apply_ngram_filter(rightTypesTri)
                nbest=trigram_collocation.nbest(trigram_measures.likelihood_ratio,10)
                #nbest=trigram_collocation.nbest(trigram_measures.raw_freq,300)
            else:
                break

            #print('\nCOLLOCATION NBest:\n')
            #print(nbest)
            VMWE.append(nbest)

            with open("final.txt", "a", encoding='utf-8') as file: 
                for ngram in nbest:
                    #pdb.set_trace()
                    if len(ngram)==2: 
                        print(ngram[0][0],ngram[1][0],';')
                        file.write(ngram[0][0]+'\t'+ngram[1][0]+'\n')
                    elif len(ngram)==3: 
                        print(ngram[0][0],ngram[1][0],ngram[2][0],';')
                        file.write(ngram[0][0]+'\t'+ngram[1][0]+'\t'+ngram[2][0]+'\n')
        #pdb.set_trace()         
    except:
        print("BREAK!")

    #pdb.set_trace()
    # open a file to store the data
##    file = open(strFile.replace('tgwds','ngram'), 'wb')
##    pickle.dump(VMWE, file)
##    file.close()
