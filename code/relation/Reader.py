#!/usr/bin/env python

from collections import defaultdict

def LoadRetweet(filepath):
    record_retweet = defaultdict(list)
    mutual_retweet = defaultdict(list)
    id_list = []
                    
    for line in open(filepath):
        ID, author, num, retweet_list = line.strip().split()
        id_list += [(ID, author)]

        user_list = sorted([int(item) for item in retweet_list.split(',')])

        for i in range(0, len(user_list)-1):
            for j in range(i+1, len(user_list)):
                 mutual_retweet[(user_list[i], user_list[j])] += [ID]
        
        for user in user_list:                                                             
            record_retweet[user] += [ID]
    
    return record_retweet, mutual_retweet, id_list

def LoadNetwork(filepath):
    follow_dict = defaultdict(list)
    follower_dict = defaultdict(list)
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
    
    return follow_dict, follower_dict

