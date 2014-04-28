#!/usr/bin/env python

import sys
from collections import defaultdict


filelist = sys.argv[1]
output = sys.argv[2]

def LoadSim(filepath):
    global SimDict
    for line in open(filepath):
        user, val = line.strip().split()
        SimDict[user] += [float(val)]

SimDict = defaultdict(list)
for line in open(filelist):
    filepath = line.strip()
    LoadSim(filepath)

fout = open(output, 'w')
for user, ftrlist in SimDict.items():
    ftrline = ",".join([str(item) for item in ftrlist])
    fout.write("%s,%s\n" % (user, ftrline))
fout.close()
