#!/usr/bin/env python

import sys
sys.path.append('/home/yipei/Twitter/FeatureExtraction/code/util')

import Loader
import Writer

from collections import defaultdict
import os.path as path

boffile = sys.argv[1]
outputPath = sys.argv[2]

def AveBof(bof_list):
    total_dict = defaultdict(int)
    for bof_dict in bof_list:
        for idx, val in bof_dict.items():
            total_dict[idx] += val
    total = len(bof_list)
    for idx in total_dict.keys():
        total_dict[idx] = total_dict[idx]/total
    return total_dict


#calculate global and individual interest based on the term frequency of each tweet/retweet
name = path.basename(boffile)
outputfile = path.join(outputPath, name)

bof_list = Loader.LoadBOW(boffile)
bof_dict = AveBof(bof_list)
Writer.WriteBOF(outputfile, bof_dict)
