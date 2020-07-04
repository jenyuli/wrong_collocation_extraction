import csv

with open('eggs.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t')
    #filename='test.txt'
    filename='conll14st-preprocessed.m2'
    with open(filename) as f:
         for line_of_text in f:
             if('S'==line_of_text[0]):
                 sentence = line_of_text[2:-1]
                 flag=0
             elif('A'==line_of_text[0]):
                 flag=1
                 tokens = line_of_text.split('|||')
                #token 0:
                 pts = tokens[0].split(' ')
                 ptA=pts[1]
                 ptB=pts[2]
                #token 1:
                 errType=tokens[1]
                #token 2:
                 crrt=tokens[2]
             else:
                 flag=0
                 
             if(1==flag):
                 #import pdb; pdb.set_trace()
                 csvwriter.writerow([errType, ptA, ptB, crrt, sentence])
                 
                 

