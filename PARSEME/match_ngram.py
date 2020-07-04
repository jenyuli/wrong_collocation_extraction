# -*- coding: utf-8 -*-
import pdb
import pickle
import re

# load the pickled corpus file
file = open('train_cupt', 'rb')
data = pickle.load(file)
words=data[0]
tagged_words=data[1]
gold=data[2]
mycorpus=data[3]
file.close()


# load the pickled ngram
file = open('ngram', 'rb')
ngram = pickle.load(file)
file.close()

##
window_size=4
flag=[]
for i,word in enumerate(words):
    for target in ngram:
        if word==target[0][0]: # if first element of ngram is detected
            ws=[]
            for j in range(len(target)): # word without pos
                ws.append(target[j][0]) 
            # if all following elements of ngram are detected
            if all(w in words[(i-window_size+1):(i+window_size)] for w in ws):
                # sarch and save positions
                for w in ws:
                    j = words[(i-window_size+1):(i+window_size)].index(w)
                    flag.append(i+j-window_size+1)
                    #pdb.set_trace()

# print gold standard
##with open("gold.txt", "w") as file:
##    for element in gold:
##        if (False==element[1].isdigit()):
##            file.write('\n'+element[1]+'\t'+str(element[0])+'\t'+words[element[0]])
##        else:
##            file.write('\t'+str(element[0])+'\t'+words[element[0]])

g=set()
f=set(flag)
tf_LVC=False
for element in gold:
    if (False==element[1].isdigit()): # if the annotation is not a digit
        #pdb.set_trace()
        if 'LVC' in element[1]:
            tf_LVC = True
            g.add(element[0]) # save this position
        else:
            tf_LVC = False
    elif tf_LVC: # if the annotation is a digit and previous annotation is LVC
        g.add(element[0])
    else:
        continue

# IF Only Trigram
##tri_list=[]
##tri_list.append([(3796,'make'),(3797,'a'),(3798,'tour')])
##tri_list.append([(19967,'put'),(19968,'on'),(19973,'smile')])
##tri_list.append([(22260,'have'),(22262,'great'),(22263,'weekend')])
##tri_list.append([(33196,'make'),(33198,'trot'),(33199,'step')])
##tri_list.append([(33430,'do'),(33434,'special'),(33435,'effect')])
##for row in tri_list:
##    for element in row:
##        g.add(element[0])

    
FN=len(g.difference(f))
FP=len(f.difference(g))
TP=len(g.intersection(f))

