#!/usr/bin/env python

import sys
sys.path.append('/home/yipei/Twitter/FeatureExtraction/code/util')
import TwitterParser as Tparse

import os.path as path

userfile = sys.argv[1]
outputPath = sys.argv[2]

name = path.basename(userfile)
outputfile = path.join(outputPath, name)
fout = open(outputfile, 'w')
for line in open(userfile):
    line = line.strip()
    text = Tparse.GetText(line)
    tweet_id, followers, friends = Tparse.GetCreditInfo(line)
    tag = False
    if text.find('RT ')!=-1:
        tag = True
    fout.write("%s %s %s %s\n" % (tweet_id, followers, friends, tag))

fout.close()
