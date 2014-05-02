#!/usr/bin/env python

import sys
from collections import defaultdict

"""
feature from the users relation and retweet behavior:
follower relation
*mutual follower (yes/no)
*mutual retweets number
user_ID.txt followers, retweets

positive sample of retweet for each user
"""

retweetfile='/home/haoyuw/twitter/v3/retweets.txt'
networkfile = '/home/haoyuw/twitter/v3/sub_v3.txt'

def LoadNetwork(filepath):
    follow_dict = defaultdict(list)
    follower_dict = {}

    all_followers = []

    for line in open(filepath):
        linelist = line.strip().split()
        user = int(linelist[0])
        if len(linelist)<2:
            continue

        follower_list = linelist[1]
        followers = [int(item) for item in follower_list.split(',')]
        for follower in followers:
            follow_dict[follower] += [user]
        follower_dict[user] = followers
    
        all_followers += followers

    network = set(all_followers)
    print len(network)

    common = list(set(follower_dict.keys()) & network)
    print len(common)
    return follow_dict, follower_dict


follow_dict, follower_dict = LoadNetwork(networkfile)


