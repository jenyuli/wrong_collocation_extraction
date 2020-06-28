# -*- coding: utf-8 -*-
import pdb
import pickle

filename='unique_cnt_avgScr.txt'
#filename='PARSEME_VerbNoun.csv'
cntBigram={}
with open(filename,'r') as f:
    for line_of_text in f:
        tokens=line_of_text[:-1].split('\t') # remove the last '\n' and split by '\t'
        strBigram=tokens[0]+' '+tokens[1]
        cntBigram[strBigram]={}
        cntBigram[strBigram]['count']=int(tokens[2])
        cntBigram[strBigram]['score']=float(tokens[3])

# open a file to store the data
file = open('NUCLE_allVbNn', 'wb')
data=cntBigram
pickle.dump(data, file)
file.close()
