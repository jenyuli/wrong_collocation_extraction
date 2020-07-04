# -*- coding: utf-8 -*-
import nltk
import nltk.data
import pdb
import pickle
import re
from nltk import PorterStemmer
from nltk.corpus import stopwords
from nltk.collocations import *
from nltk.collocations import BigramCollocationFinder , TrigramCollocationFinder, QuadgramCollocationFinder
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
           'again', ',', '.','!', '?','...','-',':','$','%','#','fig.','police','hyperlink','http'}

def myfilter_list(blacklist):
    #pdb.set_trace()
    def myfilter(word_pos):
        #pdb.set_trace()
        if word_pos[0].lower() in blacklist:
            return True
        elif word_pos[1].upper() in ['NNP','NNPS','CD','FW','PRP','PRP$','TO','UH',"NUM","PROPN","PUNCT","X","PRON","STOP","UNC"]:
            return True
        else:
            return False
    return myfilter

#function to filter for Verb/Noun bigrams
# Bigrams: (Verb, Noun), (Noun, Verb)
# The POS might be lower or upper case, therefore it needs upper()
def rightTypesBi(bigram0, bigram1):
    #pdb.set_trace()
    first_type = ('VB','VBG','VBD','VBN','VBP','VBZ','VERB','VBB', 'VBD', 'VBG', 'VBI', 'VBN', 'VBZ', 'VDB', 'VDD', 'VDG', 'VDI', 'VDN', 'VDZ', 'VHB', 'VHD', 'VHG', 'VHI', 'VHN', 'VHZ', 'VM0', 'VVB', 'VVD', 'VVG', 'VVI', 'VVN', 'VVZ', 'VVD-VVN', 'VVN-VVD')
    second_type = ('NN','NNS','NOUN','SUBST','NN0', 'NN1', 'NN2', 'ONE', 'ZZ0') #NP0, NN1-NP0, NP0-NN1
    if bigram0[1].upper() in first_type and bigram1[1].upper() in second_type:
        #pdb.set_trace()
        return False # keep this bigram
    else:
        return True # filter it out

# 1. READ CORPUS FILE
#filename = "test2.txt"
filename = "corpus.txt"
f = open(filename,'r',encoding='utf_8') #open the infile (the output generated from above)
raw = f.read()
f.close() #close the infile

raw_noURL = re.sub(r'\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', raw)
#pdb.set_trace()

# 2. or READ PRE-PROCESSED FILES (skip 3,4,5)
##file = open('wds_tgwds', 'rb')
##data = pickle.load(file)
##words = data[0]
##tagged_words = data[1]
##file.close()

# 3. TOKENIZATION
#tokens = nltk.wordpunct_tokenize(raw) #tokenize the raw text
tokens = nltk.wordpunct_tokenize(raw_noURL) #tokenize the raw text

porter=PorterStemmer()
# 4. Stemming (or not)
#words=[porter.stem(w.lower()) for w in tokens if w.isalpha()] #filter out all punctuation and numbers
words=[w.lower() for w in tokens if w.isalpha()] #filter out all punctuation and numbers

# 5. POS tagging
tagged_words = nltk.pos_tag(words)

# 6. COLLOCATIONS MEASURES
bigram_measures = nltk.collocations.BigramAssocMeasures()
#trigram_measures = nltk.collocations.TrigramAssocMeasures()
#quadgram_measures = nltk.collocations.QuadgramAssocMeasures()
#pdb.set_trace()

# 7. COLLOCATION FINDER
#finder = BigramCollocationFinder.from_words(tagged_words) #create a Bigram Collocation Finder
finder = BigramCollocationFinder.from_words(tagged_words,window_size = 4)
#finder = TrigramCollocationFinder.from_words(words)
#finder = TrigramCollocationFinder.from_words(words,window_size = 4)
#finder = QuadgramCollocationFinder.from_words(words)

# 8. FILTERING
#finder.apply_freq_filter(3) #filter out all words that appear less than 3 times
myfilter = myfilter_list(blacklist)
finder.apply_word_filter(myfilter)
finder.apply_ngram_filter(rightTypesBi)

# 9. SCORING
scored = finder.score_ngrams(bigram_measures.likelihood_ratio) #score them by raw frequency
#nbest=finder.nbest(bigram_measures.likelihood_ratio,10)

#scored = finder.score_ngrams(trigram_measures.raw_freq)
#scored = finder.score_ngrams(quadgram_measures.raw_freq)

# 10. SORTING
sorted(ngram for ngram, score in scored) #sort them by frequency
#pdb.set_trace()

# 11. WRITE FILE
f = open("final.txt","w",encoding='utf_8') #open an output file
for ngram in scored: #iterate over each ngram
   for word_pos in ngram[0]: #since the ngram is a tuple
       #pdb.set_trace()
       f.write(word_pos[0])
       f.write("\t")
       f.write(porter.stem(word_pos[0]))
       f.write("\t")
       f.write(word_pos[1])
       f.write("\t")
   f.write(str(ngram[1])) #then print the score
   f.write("\n") #print a new line
f.close() #close the output file

    # open a file to store the data
##file = open('wds_tgwds_scored', 'wb')
##data=[words,tagged_words,scored]    
##pickle.dump(data, file)
##file.close()
