#!/usr/bin/env python

from collections import defaultdict

def GetDiffusion(author, follower_dict, retweet_set):
    f1_list = follower_dict[author]
    f1_num = len(f1_list)
    connect_author = list(set(f1_list) & retweet_set)
    r1_num = len(connect_author)

    f2_list = []
    for u in f1_list:
        f2_list += follower_dict[u]
    f2_list = list(set(f2_list))
    f2_num = len(f1_list+f2_list)
    r2_num = len(set(f1_list+f2_list) & retweet_set)

    f3_list = []
    for u in f2_list:
        f3_list += follower_dict[u]
    f3_list = list(set(f3_list))
    f3_num = len(f1_list+f2_list+f3_list)
    r3_num = len(set(f1_list+f2_list+f3_list) & retweet_set)
    
    pattern=[(r1_num, f1_num), (r2_num, f2_num), (r3_num, f3_num)]
    
    retweet_list = list(retweet_set)
    rpattern = GetRelations(retweet_list, follower_dict)

    return pattern, rpattern


def GetRelations(retweet_list, follower_dict):
    retweet_dict = defaultdict(bool)
    for r in retweet_list:
        retweet_dict[r] = True

    connect_dict = defaultdict(bool)
    for i in range(0, len(retweet_list)-1):
        for j in range(i+1, len(retweet_list)):
            complete = False
            u1=retweet_list[i]
            u2=retweet_list[j]
            for u in follower_dict[u1]:
                if retweet_dict[u]:
                    connect_dict[u1]=True
                    connect_dict[u2]=True
                    complete = True
                    break

            if not complete:
                for u in follower_dict[u2]:
                    if retweet_dict[u]:
                        connect_dict[u1]=True
                        connect_dict[u2]=True
                        break

    pattern = []
    for u in retweet_list:
        pattern += [(u, connect_dict[u])]
    
    return pattern




