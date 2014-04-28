#!/usr/bin/env python

networkfile = '/home/haoyuw/twitter/v2/sub_v2.txt'
dataPath='./data/network'
output='network_distribution.txt'

from collections import defaultdict

import os.path as path

def GetHistogram(bins, max_num, ranked):
    interval = max_num/bins
    print max_num, bins, interval

    histogram = defaultdict(int)
    bin_idx = 0
    total = len(ranked)
    for n in range(0, total):
        user, num = ranked[total-1-n]
        if num > bin_idx*interval:
            bin_idx += 1
        histogram[bin_idx] += 1
    return histogram.items()


neighbor_dict = {}
size_dict = {}
for line in open(networkfile):
    linelist = line.strip().split()
    user = linelist[0]
    neighbor_list = []
    if len(linelist)>1:
        neighbor_list = linelist[1].split(',')
    size_dict[user] = len(neighbor_list)
    neighbor_dict[user] = neighbor_list

ranked = sorted([(user, num) for user, num in size_dict.items()], key=lambda item:item[1], reverse=True)

max_num = ranked[0][1]
bins = 20
histogram = GetHistogram(bins, max_num, ranked)
f = open(output, 'w')
for idx, num in histogram:
    f.write("%s,%s\n" % (idx, num))
f.close()


for i in range(0, 10):
    user = ranked[i][0]
    name = "%s_%s.txt" % (user, size_dict[user])
    idfile = path.join(dataPath, name)
    fout = open(idfile, 'w')
    fout.write("%s\n" % (user))
    for node in neighbor_dict[user]:
        fout.write("%s\n" % (node))
    fout.close()
