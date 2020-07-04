# -*- coding: utf-8 -*-
import pdb

#filename='Top10BigrambySub.txt'
filename='PARSEME_VerbNoun.csv'
cntBigram={}
with open(filename,'r') as f:
    for line_of_text in f:
        words=line_of_text[:-1].split('\t') # remove the last '\n' and split by '\t'
        strBigram=words[0]+' '+words[1]
        #pdb.set_trace()
        if strBigram in cntBigram:
            #pdb.set_trace()
            cntBigram[strBigram]=cntBigram[strBigram]+1
        else:
            cntBigram[strBigram]=1

with open('PARSEME_LVC_List.txt', 'w', encoding='utf-8') as txtfile:
    for strBigram in cntBigram:
        #pdb.set_trace()
        words=strBigram.split(' ')
        txtfile.write(words[0]+'\t'+words[1]+'\t'+str(cntBigram[strBigram])+'\n')
