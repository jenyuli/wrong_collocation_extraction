1: build a csv file (eggs.csv) with the error tag, positions, correction, and context sentence
2: extract DOC nid (add.csv) to be manually added in the previous file to make a complet file (all.csv)
3: put all sentences into a corpus file
collocations: find collocations in the corpus
lammatizing: lammatize found ngram and merge identical ones
wrong_collocations: read sentences with wrong collocation (Wci) error tag (manually selection from all.csv), then find Verb-Noun Bigram Wrong collocation
csvToDict: convert the scored collocations csv file to a Python dictionary
scoreDist: sort the scored collocations in descending order 
