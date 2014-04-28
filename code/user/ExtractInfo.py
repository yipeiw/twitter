#!/usr/bin/env python

import sys
import os.path as path
import json
from collections import defaultdict
import time

sys.path.append('/home/yipei/Twitter/FeatureExtraction/code/util')
import TwitterParser as Tparser


"""
user information
profile: num_follower, num_friends
history:num_tweet, num_retweet
        freq_url_in_retweet, freq_mention_in_retweet, freq_hashtag_in_retweet
"""

filelist = sys.argv[1]
outputPath = sys.argv[2]

def Update(tweet_info, user_history):
    if tweet_info['origin']:
        user_history['tweet_num'] += 1
    else:
        user_history['retweet_num'] += 1
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
    print "valid ", count

    user_history['max_id'] = max(id_list)
    user_history['min_id'] = min(id_list)
    return user_info, user_history

def outputInfo(user_info, history, outputfile):
    fout = open(outputfile, 'w')
    for name, val in user_info.items():
        fout.write("user_%s,%s\n" % (name, val))
    for name, val in history.items():
        fout.write("history_%s,%s\n" % (name, val))
    fout.close()


for line in open(filelist):
    start = time.time()
    user_info, history = CollectInfo(line.strip())
    print "complete ", time.time()-start

    filename = path.basename(line.strip())
    outputfile = path.join(outputPath, filename)
    outputInfo(user_info, history, outputfile)
