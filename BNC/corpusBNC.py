# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join
import pdb
import pickle
from nltk.corpus.reader.bnc import BNCCorpusReader

strPath='C:/mydesktop/BNC/download/Texts/'
bnc_reader = BNCCorpusReader(root=strPath, fileids=r'[A-K]/\w*/\w*\.xml', lazy=False)

listDir=listdir(strPath)
#list_of_fileids=[]
all_words=[]
all_tagged_words=[]
try:
    for strDir in listDir: # DIR [A-K]
        listSubDir = listdir(strPath+strDir)
        for strSubDir in listSubDir: # SUBDIR [A0-AY]
            #pdb.set_trace()
            listFile = listdir(strPath+strDir+'/'+strSubDir)
            for strFile in listFile: # FILES [A00.xml-A0Y.xml]
                print(strFile)
                strFileID = strDir+'/'+strSubDir+'/'+strFile
                words = bnc_reader.words(stem=True, fileids=strFileID) 
                all_words.append(words)
                tagged_words = bnc_reader.tagged_words(stem=True, c5=True, fileids=strFileID) # C5 Tag
                all_tagged_words.append(tagged_words)
                #pdb.set_trace()

            # SAVE DATA HERE BY SUBDIR
            file = open('wds_tgwds_'+strDir+'_'+strSubDir, 'wb')
            pickle.dump([all_words, all_tagged_words], file)
            file.close()
            all_words.clear()
            all_tagged_words.clear()
                    
 
except:
    print("Error!")

print('End')
