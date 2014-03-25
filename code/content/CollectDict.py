#!/usr/bin/env python

import sys
sys.path.append('/home/yipei/Twitter/FeatureExtraction/code/util')

from collections import defaultdict
from functools import partial
import os.path as path
from stemmer import PorterStemmer
import math
import re

import TwitterParser as Tparse

stemmer = PorterStemmer()

def process_word(word):
    word = word.lower()
    word = re.sub("[^a-z]", "", word)
    #word = re.sub("\(d+\)", "", word)
    return stemmer.stem(word)

filelist=sys.argv[1]
output=sys.argv[2]

cut=1
if len(sys.argv) > 3:
	cut = int(sys.argv[3])

word_clip_dict=defaultdict(partial(defaultdict, int))

documentNum=0
for line in open(filelist):
    filename = line.strip()
    print "processing %s" % filename
    documentNum += 1
    clip = path.basename(filename).split('.')[0]
    fin = open(filename, 'r')
    while True:
        l = fin.readline()
        if not l:
            break
        #print Tparse.GetText(l.strip())
        text = Tparse.GetText(l.strip())
        tokens = re.split("\s+|_", text)
        for token in tokens:
            word = process_word(token)
            word_clip_dict[word][clip] += 1

#calculate dictionary
IDF_dict = {}
for word in word_clip_dict.keys():
        if len(word_clip_dict[word].keys())<cut:
                continue
        IDF_dict[word] = math.log(documentNum) - math.log(len(word_clip_dict[word].keys()))

fout = open(output, 'w')
idx=1
for word, idf in sorted(IDF_dict.items(), key=lambda item:item[1]):
        fout.write("%d %s %.3f\n" % (idx, word, idf))
        idx += 1
fout.close()
