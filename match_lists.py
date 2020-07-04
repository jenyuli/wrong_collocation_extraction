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

with open('./NUCLE/sortedList.txt', 'r', encoding='utf_8') as fin:
    f = open("final.txt","w",encoding='utf_8') #open an output file
    cntTotal=0
    cntRgt=0
    cntWrg=0
    #print('Score:\t\tRight collocation:\t\tWrong collocation:\r\n')
    for line_of_text in fin:
        #pdb.set_trace()
        tokens=line_of_text[:-1].split('\t') # remove the last '\n' and split by '\t'
        score=tokens[0]
        count=int(tokens[1])
        element=tokens[2]
        #cntTotal=cntTotal+count # not use count 
        cntTotal=cntTotal+1 # because just compare list, so increase 1
        flagRgt=False
        flagWrg=False
        if (element in dictBNCallVbNn.keys()) or (element in dictPARSEMEgold.keys()):
            #print(score+'\t\t'+element+'\n')
            flagRgt=True
            #cntRgt=cntRgt+count
            cntRgt=cntRgt+1
        elif (element in dictNUCLEwrgVbNn.keys()):# both True is not included
            #print(score+'\t\t\t\t'+element+'\n')
            flagWrg=True
            #cntWrg=cntWrg+count
            cntWrg=cntWrg+1
        # write file : Score / Right colloc / Wrong colloc / TF Right colloc / TF Wrong Colloc / Cnt Right colloc / Cnt Wrong colloc / Cnt Total
        if (flagRgt or flagWrg):
            f.write(score)
            if (flagRgt and flagWrg): # note: both True but set 0 for Wrg
                f.write('\t'+element+'\t'+element+'\t'+'1'+'\t'+'0'+'\t'+str(cntRgt)+'\t'+str(cntWrg)+'\t'+str(cntTotal)+'\n')
            elif flagRgt and not flagWrg:
                f.write('\t'+element+'\t'+'\t'+'1'+'\t'+'0'+'\t'+str(cntRgt)+'\t'+str(cntWrg)+'\t'+str(cntTotal)+'\n')
            elif (not flagRgt) and flagWrg:
                f.write('\t'+'\t'+element+'\t'+'0'+'\t'+'1'+'\t'+str(cntRgt)+'\t'+str(cntWrg)+'\t'+str(cntTotal)+'\n')
            else:
                print('Something wrong!')
                break
    f.close()

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

