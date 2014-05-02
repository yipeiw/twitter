#!/usr/bin/env python

import sys
import os.path as path
import json
from collections import defaultdict
import time

sys.path.append('/home/yipei/Twitter/FeatureExtraction/code/util')
import TwitterParser as Tparser

def Update(tweet_info, user_history):
    if tweet_info['origin']:
        user_history['tweet_num'] += 1
    else:
        user_history['retweet_num'] += 1
    if not tweet_info['origin']:
        if tweet_info['has_url']:
            user_history['url'] += 1
        if tweet_info['has_mention']:
            user_history['mention'] += 1
        if tweet_info['has_hashtag']:
            user_history['hashtag'] += 1
    return user_history

def CollectInfo(filepath):
    first = True
    user_history = defaultdict(int)
    user_info = {}

    id_list = []
    count = 0
    for line in open(filepath):
        try:jsonparse=json.loads(str(line.strip()))
        except:pass

        count += 1
        if first:
            user_info = Tparser.GetUserInfo(jsonparse['user'])
            first = False
       
        id_list.append(int(jsonparse['id']))

        tweet_info = Tparser.GetTweetInfo(jsonparse['text'])
        user_history = Update(tweet_info, user_history)

    print "%s %s" % (path.basename(filepath), count)

    if len(id_list)>0:
        user_history['max_id'] = max(id_list)
        user_history['min_id'] = min(id_list)

    return user_info, user_history

def CollectTweet(filepath, tweet_list):
    tweet_dict = {}
    for line in open(filepath):
        try:jsonparse=json.loads(str(line.strip()))
        except:pass

        if int(jsonparse['id']) in tweet_list:
            text = jsonparse['text']
            tweet_info = Tparser.GetTweetInfo(text)
            tweet_dict[jsonparse['id']] = (text, tweet_info, jsonparse['created_at'])
    return tweet_dict

