# -*- coding: utf-8 -*-
import pdb
import pickle

# load the pickled files
file = open('./BNC/BNC_allVbNn', 'rb')
dictBNCallVbNn = pickle.load(file)
file.close()

file = open('./NUCLE/NUCLE_allVbNn', 'rb')
dictNUCLEallVbNn = pickle.load(file)
file.close()

file = open('./NUCLE/NUCLE_WrgVbNn', 'rb')
dictNUCLEwrgVbNn = pickle.load(file)
file.close()

file = open('./PARSEME/PARSEME_gold_dictVbNn', 'rb')
dictPARSEMEgold = pickle.load(file)
file.close()

NUCLE_List=set(dictNUCLEallVbNn.keys())
NUCLE_Wrg_List=set(dictNUCLEwrgVbNn.keys())
BNC_List=set(dictBNCallVbNn.keys())
PARSEME_List=set(dictPARSEMEgold.keys())

print(len(NUCLE_List)) #51471
print(len(BNC_List)) #883
print(len(NUCLE_Wrg_List)) #1471
print(len(PARSEME_List)) #69

print(len(NUCLE_List.intersection(BNC_List))) #176
print(len(NUCLE_List.intersection(PARSEME_List))) # 36
print(len(NUCLE_List.intersection(NUCLE_Wrg_List))) #1225

print(len(NUCLE_Wrg_List.intersection(BNC_List))) #20
print(len(NUCLE_Wrg_List.intersection(PARSEME_List))) #11
print(len(NUCLE_Wrg_List.difference(BNC_List.union(PARSEME_List)))) #1444
print(len(NUCLE_List.intersection(NUCLE_Wrg_List.difference(BNC_List.union(PARSEME_List))))) #1198

print(len(NUCLE_Wrg_List.intersection(BNC_List.intersection(PARSEME_List)))) #4
print(len(NUCLE_List.intersection(NUCLE_Wrg_List.intersection(BNC_List.intersection(PARSEME_List))))) #4
#{'take care', 'make decision', 'pay attention', 'play part'}

print(len(BNC_List.intersection(PARSEME_List))) #10
print(len(NUCLE_List.intersection(BNC_List.intersection(PARSEME_List)))) #10
#{'take action', 'take look', 'take note', 'have effect', 'play part',
# 'do job', 'pay attention', 'take care', 'make decision', 'meet need'}

print(len(NUCLE_Wrg_List.intersection(BNC_List.union(PARSEME_List))))
#{'spend year', 'do time', 'play part', 'make use', 'cause explosion',
#'make profit', 'take care', 'take part', 'take place', 'have power',
#'make effort', 'make choice', 'make adjustment', 'address need',
#'pay attention', 'make decision', 'take account', 'pay debt', 'do effect',
#'take advantage', 'earn money', 'spend money', 'achieve goal', 'cause issue',
#'take responsibility', 'have problem', 'do research'}


#g=set()
#f=set(flag)
# IF Only Trigram
##tri_list=[]
##for row in tri_list:
##    for element in row:
##        g.add(element[0])

##FN=len(g.difference(f))
##FP=len(f.difference(g))
##TP=len(g.intersection(f))

