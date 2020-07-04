# -*- coding: utf-8 -*-
import pickle
'''
ERROR NOTE:
        sentence: 'email-enronsent28_01-0019'
        tokens[0]=='24.1', which is not an INT 
MANUAL CORRECTION:
    change to '25', also modify the index of following tokens
'''
                    
#MAIN                
#filename='test.txt'
filename='train.cupt'
try:
    with open(filename,'r',encoding='utf_8') as f:
        mycorpus={} # set 'mycorpus' as a dictionary, each 'sentence_id' is a key
        for i,row in enumerate(f):
            if (i==0):
                columns=row[19:-1].split(' ') # extract the feature titles for each token
            elif ('# source_sent_id' in row):
                source_sent_id=row[23:-1] # extract the 'sentence_id'
            elif ('# text' in row):
                text=row[9:-1] # extract the text
                mycorpus[source_sent_id]={} # set each sentence as a dictionary
                mycorpus[source_sent_id]['text']=text # each sentence contains a text
                mycorpus[source_sent_id]['tokens']={} # and a dictionary of tokens
            elif (len(row)==1) or ('# newdoc' in row):
                continue
            elif (len(row)>1) and (row[0].isdigit()):
                tokens=row[:-1].split('\t') # extract the features of each token
                #if tokens[0]=='24.1': break # an exception -> manually removed from original corpus
                i = int(tokens[0])
                mycorpus[source_sent_id]['tokens'][i]={}
                for j,element in enumerate(tokens):
                    mycorpus[source_sent_id]['tokens'][i][columns[j]]=element
            else:
                print("Error in Line: "+str(i))
except:
    print("Error in Line: "+str(i))

words=[]
tagged_words=[]
gold=[]
for sentence_id in mycorpus:
    for i in mycorpus[sentence_id]['tokens']:
        form = mycorpus[sentence_id]['tokens'][i]['LEMMA']
        upos = mycorpus[sentence_id]['tokens'][i]['UPOS']
        anno = mycorpus[sentence_id]['tokens'][i]['PARSEME:MWE']
        words.append(form.lower())
        tagged_words.append((form.lower(),upos))
        if '*'!=anno:
            index = len(words)-1
            gold.append((index,anno))

data=[words, tagged_words, gold, mycorpus]

# open a file to store the data
#file = open('corpus_test', 'wb')
file = open('train_cupt', 'wb')

# dump information to that file
pickle.dump(data, file)

# close the file
file.close()
