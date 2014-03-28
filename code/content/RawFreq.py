#!/usr/bin/env python

import sys
sys.path.append('/home/yipei/Twitter/FeatureExtraction/code/util')

from collections import defaultdict
import os.path as path
from stemmer import PorterStemmer
import re

import TwitterParser as Tparse

stemmer = PorterStemmer()

filelist = sys.argv[1]
outputdir = sys.argv[2]

for line in open(filelist):
    line = line.strip()
    fin = open(line, 'r')
    clip = path.basename(line).split(".")[0]
    print "process ", clip 

    boffile = path.join(outputdir, clip+'.bof')
    fout=open(boffile, 'w')
    
    wordDict=defaultdict(int)
    wordDict.clear()

    #go through all tweets and count for the number of each term
    while True:
        line = fin.readline()
        if not line:
            break

        text = Tparse.GetText(line.strip())
        tokens = re.split('\s+|_', text)
        for token in tokens:
            word = re.sub("[^a-z]", "", token.lower())
            word = stemmer.stem(word)
            if len(word)>0:
                wordDict[word] += 1
   
    #calculate frequency and output result
    output_vector = []
    total = sum([item for index, item in wordDict.items()])
    output_vector = [(index, float(val)/float(total)) for index, val in wordDict.items()]
    output_vector = sorted(output_vector, key=lambda item:item[0])
    
    for index, value in output_vector:
        fout.write("%s %s\n" % (index, value))

    fout.close()
    
