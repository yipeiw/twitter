#!/usr/bin/env python

import sys
import os.path as path
import os
import time
import numpy as np


import Reader
import Writer
import Processor
import Collect

"""
EdgeFeature:
mutual retweets, mutual followers, mutual following, who follows who ([0 0]smaller node--smaller idx 1)

node_idx1_node_idx2.txt
<instance> feature1, feature2...

Node Feature and label, for all users in the network:
user_ID.txt
<instance> feature1, feature2, ...
feature set: same with LR classifier
"""

networkfile='/home/haoyuw/twitter/v3/sub_v3.txt'
labelfile = '/home/yipei/Twitter/FeatureExtraction/data/label/29087161_s2.csv'
graphfile = '/home/yipei/Twitter/ExtractGraph/graphs/29087161_s2.csv'
nodefile = '/home/yipei/Twitter/FeatureExtraction/data/label/29087161_s2.csv.node'

tweet_info_path = '/home/yipei/Twitter/FeatureExtraction/data/tweets'
user_path = '/home/yipei/Twitter/FeatureExtraction/data/user_v3'
mutual_path = '/home/yipei/Twitter/FeatureExtraction/data/mutual'

#construct data directory
name = path.splitext(path.basename(labelfile))[0]
dataPath='/home/yipei/Twitter/FeatureExtraction/data/trainfile/CRFbase/'
trainPath = path.join(dataPath, name)
nodeFeatPath = path.join(trainPath, 'node_feat')
edgeFeatPath = path.join(trainPath, 'edge_feat')
if not path.exists(trainPath):
    os.mkdir(trainPath)
    os.mkdir(nodeFeatPath)
    os.mkdir(edgeFeatPath)

follow_dict, follower_dict = Reader.LoadNetwork(networkfile)
tweet_list = Reader.LoadLabel(labelfile)
relations = Reader.LoadGraph(graphfile)

print "complete preparation, start node feature extraction"

nodes = [int(line.strip()) for line in open(nodefile)]
#user only feature are static, other features are associated with instance
tag=''
for node in nodes:
    pool = []
    node_feat_file = path.join(nodeFeatPath, str(node)+'.txt')
    start = time.time()
    for ID in tweet_list:
        tag, node_feat = Collect.GetTrainData(node, ID, tag, follow_dict, tweet_info_path, user_path, mutual_path)
        pool += [node_feat]
    Writer.outputFeature(node_feat_file, pool)
    print "complete %s " % (node), time.time()-start 
