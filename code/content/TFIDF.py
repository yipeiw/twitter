#!/usr/bin/env python

import sys
sys.path.append('/home/yipei/Twitter/FeatureExtraction/code/util')

from collections import defaultdict
import os.path as path
from stemmer import PorterStemmer
import re

import TwitterParser as Tparse

stemmer = PorterStemmer()

def process_word(word):
    word = word.lower()
    word = re.sub("[^a-z]", "", word)
    return stemmer.stem(word)

filelist = sys.argv[1]
dictfile = sys.argv[2]
outputdir = sys.argv[3]

#load dictionary
dict_idf={}
for line in open(dictfile):
    (index, word, idf) = line.strip().split(' ')
    dict_idf[word]=(int(index), float(idf))
    
for line in open(filelist):
    line = line.strip()
    fin = open(line, 'r')
    clip = path.basename(line).split(".")[0]
    print "process ", clip 
    boffile = path.join(outputdir, clip+'.bof')
    fout=open(boffile, 'w')

    while True:
        line = fin.readline()
        if not line:
            break

        text = Tparse.GetText(line.strip())
        wordDict=defaultdict(int)
        wordDict.clear()
        tokens = re.split('\s+|_', text)
        for token in tokens:
            word = process_word(token)
            wordDict[word] += 1
   
        #calculate tf-idf and output result
        output_vector = []
        for word, count in wordDict.items():
	        if word in dict_idf.keys():
                    output_vector += [(dict_idf[word][0], count * dict_idf[word][1])]
        total = sum([item for index, item in output_vector])
        if not total==0:
            output_vector = [(index, item/total) for index, item in output_vector]
            output_vector = sorted(output_vector, key=lambda item:item[0])
    
        outputlist = ["{0}:{1}".format(index, value) for index, value in output_vector]
        fout.write(" ".join(outputlist)+'\n')

    fout.close()
    
