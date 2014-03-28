#!/usr/bin/env python

from collections import defaultdict

def LoadBOW(filepath):
    bof_list = []
    for line in open(filepath):
        bof_dict = {}
        for item in line.strip().split():
            idx, val = item.split(':')
            bof_dict[int(idx)] = float(val)
        bof_list += [bof_dict]

    return bof_list

def LoadFreq(filepath):
    bof_dict = defaultdict(float)
    for line in open(filepath):
        word, val = line.strip().split()
        bof_dict[word] = float(val)
    return bof_dict
