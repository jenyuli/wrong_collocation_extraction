import csv

with open('corpus.txt', 'w', encoding='utf-8') as txtfile:
    filename='conll14st-preprocessed.m2'
    with open(filename,'r') as f:
         for line_of_text in f:
             if('S'==line_of_text[0]):
                 sentence = line_of_text[2:-1]
                 txtfile.write(sentence+' ')
             else:
                 continue

                 

