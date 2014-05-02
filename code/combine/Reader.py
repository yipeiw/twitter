#!/usr/bin/env python

from collections import defaultdict

def LoadGraph(filepath):
    relations = []
    for line in open(filepath):
        node1, node2 = line.strip().split(',')
        relations += [(int(node1), int(node2))]
    return relations

def LoadLabel(filepath):
    return [int(line.strip().split(',')[0]) for line in open(filepath)]

def LoadID(filepath):
    return [int(line.strip().split()[0]) for line in open(filepath)]

def LoadNetwork(filepath):
    follower_dict = defaultdict(list)
    follow_dict = defaultdict(list)
    for line in open(filepath):
        linelist = line.strip().split()
        user = int(linelist[0])
        if len(linelist)<2:
            continue

        followers = [int(item) for item in linelist[1].split(',')]
        follower_dict[user] = followers
   
        for item in followers:
            follow_dict[item] += [user]

    return follow_dict, follower_dict

