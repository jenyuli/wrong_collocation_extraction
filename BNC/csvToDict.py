# -*- coding: utf-8 -*-
import pdb
import pickle

filename='uniqueSorted.txt'
cntBigram={}
with open(filename,'r') as f:
    for line_of_text in f:
        tokens=line_of_text[:-1].split('\t') # remove the last '\n' and split by '\t'
        strBigram=tokens[0]+' '+tokens[1]
        cntBigram[strBigram]=int(tokens[2])

# open a file to store the data
file = open('BNC_allVbNn', 'wb')
data=cntBigram
pickle.dump(data, file)
file.close()
