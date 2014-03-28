#!/usr/bin/env python

import sys
sys.path.append('/home/yipei/Twitter/FeatureExtraction/code/util')
import os.path as path

import Loader
import Calculator

userinfo = sys.argv[1]
topicPath = sys.argv[2]
output = sys.argv[3]

user_list = [line.strip().split()[0] for line in open(userinfo)]
result = {}

for i in range(0, len(user_list)-1):
    for j in range(i+1, len(user_list)):
        user1 = path.join(topicPath, user_list[i]+'.bof')
        user2 = path.join(topicPath, user_list[j]+'.bof')
        freq1 = Loader.LoadFreq(user1)
        freq2 = Loader.LoadFreq(user2)
        val = Calculator.SimilarityCos(freq1, freq2)
        print "%s %s %s" % (user_list[i], user_list[j], val)
        result[(user_list[i], user_list[j])] = val

fout = open(output, 'w')
for u1, u2 in result.keys():
    val = result[(u1, u2)]
    fout.write("%s %s %.3f\n" % (u1, u2, val))
fout.close()
