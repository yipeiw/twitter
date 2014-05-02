#!/usr/bin/env python

import os.path as path
from collections import defaultdict

def GetEdgeFeatStatic(node1, node2, follow_dict, follower_dict, mutual_path):
    f_num = len(set(follow_dict[node1]) & set(follow_dict[node2]))
    fer_num = len(set(follower_dict[node1]) & set(follower_dict[node2]))
    r_num = 0
    mutualfile = path.join(mutual_path, str(node1)+'.txt')
    if path.exists(mutualfile):
        mutual_info = {int(line.strip().split()[0]):line.strip().split() for line in open(mutualfile)}

        if node2 in mutual_info.keys():
            info = mutual_info[int(node2)]
            r_num = int(info[1])
    
    return [f_num, fer_num, r_num]

def GetEdgeFeat(node1, node2, authorID, mutual_path, tweet_path):
    co_num = 0

    mutualfile = path.join(mutual_path, str(node1)+'.txt')
    if path.exists(mutualfile):
        mutual_info = {int(line.strip().split()[0]):line.strip().split() for line in open(mutualfile)}

        if node2 in mutual_info.keys():
            info = mutual_info[int(node2)]
            r_num = int(info[1])
            for mID in info[2:len(info)]:
                tweetfile = path.join(tweet_path, mID+'.txt')
                tweet_author = GetAuthor(mID, tweet_path)
                if tweet_author==authorID:
                    co_num += r_num

    return [co_num]


def GetRelationFeature(userID, authorID, follower_dict, follow_dict, mutual_path):
    follow = 0
    connect = -1
    if int(userID) in follower_dict[int(authorID)]:
        follow = 1
        connect = 0
    else:
        source = follower_dict[int(authorID)]
        follow_set = set(follow_dict[int(userID)])
        for level in range(0, 4):
            if len(follow_set & set(source))>0:
                connect = level+1
                break
            new_source = []
            for u in source:
                new_source += follower_dict[u]
            source = new_source

    mutual_num = 0
    mutualfile = path.join(mutual_path, str(userID)+'.txt')
    if path.exists(mutualfile):
        mutual_info = {int(line.strip().split()[0]):int(line.strip().split()[1]) for line in open(mutualfile)}
    
        if int(userID) in mutual_info.keys():
            mutual_num = mutual_info[int(userID)]

    return [follow, connect, mutual_num]


def GetAuthor(tweetID, tweetPath):
    tweetfile = path.join(tweetPath, str(tweetID)+'.txt')
    f = open(tweetfile)
    text = f.readline()
    authorID = f.readline().strip()
    f.close()
    return int(authorID)

def GetTweetFeature(tweetfile):
    f = open(tweetfile)
    text = f.readline()
    authorID = f.readline().strip()
    timestamp = f.readline()
    origin = f.readline()
    
    mention = f.readline().strip().split(':')[1]
    mention_tag = int(mention=='True')
    
    url = f.readline().strip().split(':')[1]
    url_tag = int(url=='True')

    hashtag = f.readline().strip().split(':')[1]
    hashtag_tag = int(hashtag=='True')
    f.close()
    return [mention_tag, url_tag, hashtag_tag], authorID

def GetAuthorFeature(userfile):
    info_dict = defaultdict(int)
    for line in open(userfile):
        name, val = line.strip().split(',')
        info_dict[name] = int(val)
    return [ info_dict['user_follow'], info_dict['user_friend'], info_dict['history_tweet_num'], info_dict['history_retweet_num'] ]

def GetUserFeature(userfile):
    info_dict = defaultdict(int)
    for line in open(userfile):
        name, val = line.strip().split(',')
        info_dict[name] = int(val)
    return [ info_dict['history_mention'], info_dict['history_url'], info_dict['history_hashtag']]
