# -*- coding: utf-8 -*-
import pdb
import pickle

def myFunc(e):
    return e['score']

filename='NUCLE_List.txt'
lstBigram=[]
with open(filename,'r') as f:
    for line_of_text in f:
        tokens=line_of_text[:-1].split('\t') # remove the last '\n' and split by '\t'
        strBigram=tokens[0]+' '+tokens[1]
        lstBigram.append({'bigram':strBigram,'count':int(tokens[2]),'score':float(tokens[3])})

lstBigram.sort(reverse=True,key=myFunc)

filename='sortedList.txt'
with open(filename,'w',encoding='utf_8') as f:
    for entry in lstBigram:
        f.write("{0:.4f}".format(entry['score'])+'\t'+str(entry['count'])+'\t'+entry['bigram']+'\n')


