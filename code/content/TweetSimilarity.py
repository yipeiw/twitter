#!/usr/bin/env python

import sys
sys.path.append('/home/yipei/Twitter/FeatureExtraction/code/util')
import os.path as path
from collections import defaultdict
from stemmer import PorterStemmer
import re

stemmer = PorterStemmer()

import Loader
import Calculator

tweetfile = sys.argv[1]
userinfo = sys.argv[2]
topicPath = sys.argv[3]
output = sys.argv[4]

def TweetFreq(tweet):
    wordDict = defaultdict(int)
    tokens = re.split('\s+|_', tweet)
    for token in tokens:
        word = re.sub("[^a-z]", "", token.lower())
        word = stemmer.stem(word)
        if len(word)>0:
            wordDict[word] += 1

    total = sum([item for index, item in wordDict.items()])
    for idx, count in wordDict.items():
        wordDict[idx] = float(count)/float(total)
    return wordDict

user_list = [line.strip().split()[0] for line in open(userinfo)]

fin = open(tweetfile)
tweet = fin.readline().strip()
fin.close()
tweet_freq = TweetFreq(tweet)

fout = open(output, 'w')
for user in user_list:
    userfile = path.join(topicPath, user+'.bof')
    user_freq = Loader.LoadFreq(userfile)
    val = Calculator.SimilarityCos(user_freq, tweet_freq)
    #print "%s %s" % (user, val)
    fout.write("%s %.6f\n" % (user, val))
fout.close()
