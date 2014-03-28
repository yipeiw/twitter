#!/usr/bin/env python

import sys
sys.path.append('/home/yipei/Twitter/FeatureExtraction/code/util')

import os.path as path

import TwitterParser as Tparse
import Processor

filelist=sys.argv[1]
outputPath=sys.argv[2]

track = {}
for line in open(filelist):
    filename = line.strip()
    print "processing %s" % filename
    for l in open(filename):
        l = l.strip()
        text = Tparse.GetText(l)
        tweetID, follow_num, friend_num = Tparse.GetCreditInfo(l)
        track[tweetID] = text

for ID, content in track.items():
    outputfile = path.join(outputPath, ID+'.txt')
    fout = open(outputfile, 'w')
    fout.write("%s\n" % (content))
    fout.close()
