#!/usr/bin/env python

import sys
sys.path.append('/home/yipei/Twitter/FeatureExtraction/code/util')

import TwitterParser as Tparse

filelist=''

for line in open(filelist):
    filename = line.strip()
    print "processing %s" % filename
    documentNum += 1
    clip = path.basename(filename).split('.')[0]
    time_list = []
    for l in open(filename):
        timestamp = Tparse.GetTimeStamp(l.strip())
        time_list += [timestamp]

