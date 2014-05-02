#!/usr/bin/env python

import sys
import os.path as path
import os
import time

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

print "complete preparation, start edge feature extraction"
#mutual retweets, follow relation are static feature
edge_feat_static_file = path.join(trainPath, 'edge_static.csv')
fout = open(edge_feat_static_file, 'w')
for node1, node2 in relations:
    edge_feat = Processor.GetEdgeFeatStatic(node1, node2, follow_dict, follower_dict, mutual_path)
    featline = ",".join([str(item) for item in edge_feat]) 
    fout.write("%s,%s,%s\n" % (node1, node2, featline))
fout.close()
print "static finish"

#mutual retweets of the author of the tweet is instance related
start = time.time()
edge_feat_file = path.join(trainPath, 'edge_cotreweet.csv')
f = open(edge_feat_file, 'w')
for node1, node2 in relations:
    feat_list = []
    for ID in tweet_list:
        authorID = Processor.GetAuthor(ID, tweet_info_path)
        edge_feat = Processor.GetEdgeFeat(node1, node2, authorID, mutual_path, tweet_info_path)
        if edge_feat > 0:
            feat_list += ["%s:%s" % (ID, edge_feat)]
    f.write("%s,%s,%s\n" % (node1, node2, ",".join(feat_list)))
f.close()

