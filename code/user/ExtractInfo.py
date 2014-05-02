#!/usr/bin/env python

import sys
import os.path as path
from collections import defaultdict
import time

import Reader
import Writer

"""
user information
profile: num_follower, num_friends
history:num_tweet, num_retweet
        freq_url_in_retweet, freq_mention_in_retweet, freq_hashtag_in_retweet

generate tweet file for tweet in retweet list:
id, content, author, timestamp
has mention/url/hashtag
"""

filelist = sys.argv[1]
outputPath = sys.argv[2]

recordPath='/home/yipei/Twitter/FeatureExtraction/data/author'
tweetPath='/home/yipei/Twitter/FeatureExtraction/data/tweets'

for line in open(filelist):
    filepath = line.strip()
    filename = path.basename(filepath)
    author = path.splitext(filename)[0]

    retweetfile = path.join(recordPath, filename)
    retweet_list = []
    if path.exists(retweetfile):
        retweet_list = [int(line.strip()) for line in open(retweetfile)]
    
    #print "retweetfile: ", retweetfile, len(retweet_list)

    user_info, history = Reader.CollectInfo(filepath)
    if len(user_info.items())==0:
        print "skip ", line.strip()
        continue

    tweet_dict = {}
    if len(retweet_list)>0:
        tweet_dict = Reader.CollectTweet(filepath, retweet_list)

    outputfile = path.join(outputPath, filename)
    Writer.outputInfo(user_info, history, outputfile)

    if len(tweet_dict.items())>0:
        Writer.outputTweet(tweet_dict, author, tweetPath)
