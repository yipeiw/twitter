#!/usr/bin/env python

import os.path as path
from collections import defaultdict

retweet_path = '/home/yipei/Twitter/FeatureExtraction/data/retweets'
relationfile = '/home/yipei/Twitter/ExtractGraph/graphs/29087161_s2.csv'
all_list = '/home/yipei/Twitter/FeatureExtraction/data/retweets.list'
tweet_dict = {int(line.strip().split()[0]): int(line.strip().split()[1]) for line in open(all_list)}

labelPath='/home/yipei/Twitter/FeatureExtraction/data/label'
filename = path.basename(relationfile)
labelfile = path.join(labelPath, filename)
nodefile =path.join(labelPath, filename+'.node')

#get all nodes in the network
node_dict = defaultdict(bool)
for line in open(relationfile):
    node1, node2 = line.strip().split(',')
    node_dict[int(node1)] = True
    node_dict[int(node2)] = True

f = open(nodefile, 'w')
for node in sorted(node_dict.keys()):
    f.write("%s\n" % (node))
f.close()

#collect instance label
label_dict = defaultdict(list)
for node in sorted(node_dict.keys()):
    retweetfile = path.join(retweet_path, str(node)+'.txt')
    if not path.exists(retweetfile):
        print "no retweets ", node
        continue
    retweet_list = [int(line.strip()) for line in open(retweetfile)]
    for tweet_ID in retweet_list:
        label_dict[tweet_ID] += [node]

#distribution of how many retweet happend for each one, filter if necessary
print len(label_dict.keys())
for tweet_ID, retweeters in sorted(label_dict.items(), key=lambda item:len(item[1]), reverse=True):
    tag = node_dict[tweet_dict[tweet_ID]] 
    print tweet_ID, len(retweeters), tag

#output label
f = open(labelfile, 'w')
for tweet_ID, retweeters in sorted(label_dict.items(), key=lambda item:len(item[1]), reverse=True):
        tag = node_dict[tweet_dict[tweet_ID]]
        if tag:
            output = ",".join(str(item) for item in [tweet_ID]+retweeters)
            f.write("%s\n" % (output))
f.close()


