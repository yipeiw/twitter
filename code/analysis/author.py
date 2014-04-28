#!/usr/bin/env python

authorfile = '/home/yipei/Twitter/FeatureExtraction/data/network/author.log'
output='active'

from collections import defaultdict

import os.path as path

def GetHistogram(bins, max_num, ranked):
    interval = max_num/bins
    print max_num, bins, interval

    histogram = defaultdict(int)
    bin_idx = 0
    total = len(ranked)
    for n in range(0, total):
        user, num = ranked[total-1-n]
        if num > bin_idx*interval:
            bin_idx += 1
        histogram[bin_idx] += 1
    return histogram.items()


total_dict = {}
tweet_dict = {}
retweet_dict = {}
for line in open(authorfile):
    user, tweet, retweet = line.strip().split()
    tweet_dict[user] = int(tweet)
    retweet_dict[user] = int(retweet)
    total_dict[user] = int(tweet) + int(retweet)

ranked_tweet = sorted([(user, num) for user, num in tweet_dict.items()], key=lambda item:item[1], reverse=True)
ranked_retweet = sorted([(user, num) for user, num in retweet_dict.items()], key=lambda item:item[1], reverse=True)
ranked_total = sorted([(user, num) for user, num in total_dict.items()], key=lambda item:item[1], reverse=True)

max_num = ranked_tweet[0][1]
bins = 20
histogram = GetHistogram(bins, max_num, ranked_tweet)
f = open(output+'_tweet.txt', 'w')
for idx, num in histogram:
    f.write("%s,%s\n" % (idx, num))
f.close()

max_num = ranked_retweet[0][1]
histogram = GetHistogram(bins, max_num, ranked_retweet)
f = open(output+'_retweet.txt', 'w')
for idx, num in histogram:
    f.write("%s,%s\n" % (idx, num))
f.close()

max_num = ranked_total[0][1]
histogram = GetHistogram(bins, max_num, ranked_total)
f = open(output+'_total.txt', 'w')
for idx, num in histogram:
    f.write("%s,%s\n" % (idx, num))
f.close()


