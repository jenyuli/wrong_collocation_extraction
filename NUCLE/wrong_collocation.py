# -*- coding: utf-8 -*-
import csv
import nltk
import pdb
import pickle
from nltk.stem import WordNetLemmatizer

def addBigram(cntBigram,strBigram):
    if strBigram in cntBigram:
        cntBigram[strBigram]=cntBigram[strBigram]+1
    else:
        cntBigram[strBigram]=1
    return cntBigram

lemmatizer = WordNetLemmatizer()

# WRITE FILE
with open("final.txt","w",encoding='utf_8') as f: #open an output file
    # READ CSV FILE for sentences with wrong collocation (Wci) error tag
    filename = "wci.csv"
    #dictWrgVbNn={}
    with open(filename,'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile,delimiter='\t')
        for line in csvreader:
            p1=int(line[2]) # the start position of the marked error
            p2=int(line[3]) # the end position of the marked error
            sentence=line[5]
            # split the sentence into tokens and add pos tags
            words=sentence.split(' ')
            tagged_words = nltk.pos_tag(words)
            # find Verb-Noun Bigram Wrong collocation
            flagVerb=False
            flagNoun=False
            for word_pos in tagged_words[p1:p2]:
                if word_pos[1].startswith('V'): # if there is a Verb within the marked error
                    lemma0=lemmatizer.lemmatize(word_pos[0].lower(),'v')
                    word0=word_pos[0].lower()
                    if lemma0 == 'be': # exclude 'be'
                        lemma0=[]
                        word0=[]
                        flagVerb=False
                        #pdb.set_trace()
                    else:
                        flagVerb=True
                elif (flagVerb and word_pos[0].isalpha() and word_pos[1].startswith('N')): # find the Noun after the Verb
                    flagNoun=True
                    lemma1=lemmatizer.lemmatize(word_pos[0].lower(),'n')
                    word1=word_pos[0].lower()
                    break
            
            if flagVerb:
                if flagNoun: # Have found a Noun in the marked error
                    #dictWrgVbNn=addBigram(dictWrgVbNn,lemma0+' '+lemma1)
                    #pdb.set_trace()
                    f.write(word0+' '+word1+'\n')
                else: # find a Noun in the following words until reach the end of sentence
                    for word_pos in tagged_words[p2:]:
                        if (word_pos[0].isalpha() and word_pos[1].startswith('N')):
                            flagNoun=True
                            lemma1=lemmatizer.lemmatize(word_pos[0].lower(),'n')
                            word1=word_pos[0].lower()
                            #dictWrgVbNn=addBigram(dictWrgVbNn,lemma0+' '+lemma1)
                            #pdb.set_trace()
                            f.write(word0+' '+word1+'\n')
                            break
                        

# WRITE FILE
##f = open("final.txt","w",encoding='utf_8') #open an output file
##for ngram in dictWrgVbNn.keys(): #iterate over each ngram
##    words=ngram.split(' ')
##    for word in words:
##       #pdb.set_trace()
##       f.write(word)
##       f.write("\t")
##    f.write(str(dictWrgVbNn[ngram])) #then print the score
##    f.write("\n") #print a new line
##f.close() #close the output file
##
##    # open a file to store the data
##file = open('dictWrgVbNn', 'wb')
##data=dictWrgVbNn
##pickle.dump(data, file)
##file.close()
