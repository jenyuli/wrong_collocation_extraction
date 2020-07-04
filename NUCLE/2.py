import csv

with open('adds.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t')
    #filename='test1.txt'
    filename='conll14st-preprocessed.conll.ann'
    with open(filename) as f:
         for line_of_text in f:
             i=line_of_text.find('nid')
             if(0<=i):
                 sentence = line_of_text.split(' ')
                 token = sentence[1].split('\"')
                 nid = int(token[1])
                 csvwriter.writerow([nid])
