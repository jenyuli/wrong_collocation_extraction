# -*- coding: utf-8 -*-
import pdb
import pickle
from nltk.stem import WordNetLemmatizer

# Create a map between Treebank and WordNet 
from nltk.corpus import wordnet as wn

# WordNet POS tags are: NOUN = 'n', ADJ = 's', VERB = 'v', ADV = 'r', ADJ_SAT = 'a'
# Descriptions (c) https://web.stanford.edu/~jurafsky/slp3/10.pdf
tag_map = {
        'CC':None, # coordin. conjunction (and, but, or)  
        'CD':wn.NOUN, # cardinal number (one, two)             
        'DT':None, # determiner (a, the)                    
        'EX':wn.ADV, # existential ‘there’ (there)           
        'FW':None, # foreign word (mea culpa)             
        'IN':wn.ADV, # preposition/sub-conj (of, in, by)   
        'JJ':[wn.ADJ, wn.ADJ_SAT], # adjective (yellow)                  
        'JJR':[wn.ADJ, wn.ADJ_SAT], # adj., comparative (bigger)          
        'JJS':[wn.ADJ, wn.ADJ_SAT], # adj., superlative (wildest)           
        'LS':None, # list item marker (1, 2, One)          
        'MD':None, # modal (can, should)                    
        'NN':wn.NOUN, # noun, sing. or mass (llama)          
        'NNS':wn.NOUN, # noun, plural (llamas)                  
        'NNP':wn.NOUN, # proper noun, sing. (IBM)              
        'NNPS':wn.NOUN, # proper noun, plural (Carolinas)
        'PDT':[wn.ADJ, wn.ADJ_SAT], # predeterminer (all, both)            
        'POS':None, # possessive ending (’s )               
        'PRP':None, # personal pronoun (I, you, he)     
        'PRP$':None, # possessive pronoun (your, one’s)    
        'RB':wn.ADV, # adverb (quickly, never)            
        'RBR':wn.ADV, # adverb, comparative (faster)        
        'RBS':wn.ADV, # adverb, superlative (fastest)     
        'RP':[wn.ADJ, wn.ADJ_SAT], # particle (up, off)
        'SYM':None, # symbol (+,%, &)
        'TO':None, # “to” (to)
        'UH':None, # interjection (ah, oops)
        'VB':wn.VERB, # verb base form (eat)
        'VBD':wn.VERB, # verb past tense (ate)
        'VBG':wn.VERB, # verb gerund (eating)
        'VBN':wn.VERB, # verb past participle (eaten)
        'VBP':wn.VERB, # verb non-3sg pres (eat)
        'VBZ':wn.VERB, # verb 3sg pres (eats)
        'WDT':None, # wh-determiner (which, that)
        'WP':None, # wh-pronoun (what, who)
        'WP$':None, # possessive (wh- whose)
        'WRB':None, # wh-adverb (how, where)
        '$':None, #  dollar sign ($)
        '#':None, # pound sign (#)
        '“':None, # left quote (‘ or “)
        '”':None, # right quote (’ or ”)
        '(':None, # left parenthesis ([, (, {, <)
        ')':None, # right parenthesis (], ), }, >)
        ',':None, # comma (,)
        '.':None, # sentence-final punc (. ! ?)
        ':':None # mid-sentence punc (: ; ... – -)
    }


lemmatizer = WordNetLemmatizer() 

# READ PRE-PROCESSED FILES
file = open('wds_tgwds_scored', 'rb')
data = pickle.load(file)
words = data[0]
tagged_words = data[1]
scored = data[2]
file.close()

# WRITE FILE
##f = open("final.txt","w",encoding='utf_8') #open an output file
##for ngram in scored: #iterate over each ngram
##   for word_pos in ngram[0]: #since the ngram is a tuple
##       #pdb.set_trace()
##       #print(lemmatizer.lemmatize(word_pos[0],tag_map[word_pos[1]]))
##       f.write(word_pos[0])
##       f.write("\t")
##       f.write(lemmatizer.lemmatize(word_pos[0],tag_map[word_pos[1]]))
##       f.write("\t")
##       f.write(word_pos[1])
##       f.write("\t")
##   f.write(str(ngram[1])) #then print the score
##   f.write("\n") #print a new line
##f.close() #close the output file

# UNIQUE and AVERAGE SCORE
cntBigram={}
scrBigram={}
for ngram in scored: #iterate over each ngram
   #pdb.set_trace()
   list_word_pos = ngram[0]
   word_pos0 = list_word_pos[0]
   word_pos1 = list_word_pos[1]
   lemma0=lemmatizer.lemmatize(word_pos0[0],tag_map[word_pos0[1]])
   lemma1=lemmatizer.lemmatize(word_pos1[0],tag_map[word_pos1[1]])
   strBigram=lemma0+' '+lemma1
   if strBigram in cntBigram:
      #pdb.set_trace()
      cntBigram[strBigram]=cntBigram[strBigram]+1
      scrBigram[strBigram]=scrBigram[strBigram]+ngram[1]
   else:
      cntBigram[strBigram]=1
      scrBigram[strBigram]=ngram[1]

with open('unique_cnt_avgScr.txt', 'w', encoding='utf-8') as txtfile:
    for strBigram in cntBigram:
        #pdb.set_trace()
        words=strBigram.split(' ')
        avg=scrBigram[strBigram]/cntBigram[strBigram]
        txtfile.write(words[0]+'\t'+words[1]+'\t'+str(cntBigram[strBigram])+'\t'+str(avg)+'\n')
