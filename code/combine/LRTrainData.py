#!/usr/bin/env python

import sys
import os.path as path

import Reader
import Writer
import Processor

"""
user.txt
<instance> retweet_tag, features
user.log  instance source (tweet_ID)

feature set:
(The popularity and activity of the author)
-author number of followers, friends, number of tweets, retweets

(charateristic of the tweet)
-has mention, has hashtag, has url link

not useful for local classifier
#(user preference based on history)
#-freq of mention/url/hashtag in retweets

(user, author relation)
-follower?
-number of mutual retweets
*number of mutual mentions
"""

userID=sys.argv[1]

retweet_list_file = '/home/yipei/Twitter/FeatureExtraction/data/retweets/'+userID+'.txt'
all_retweet_file='/home/yipei/Twitter/FeatureExtraction/data/retweets.list'

networkfile='/home/haoyuw/twitter/v3/sub_v3.txt'

tweet_info_path = '/home/yipei/Twitter/FeatureExtraction/data/tweets'
user_path = '/home/yipei/Twitter/FeatureExtraction/data/user_v3'
mutual_path = '/home/yipei/Twitter/FeatureExtraction/data/mutual'

#userID = '110445334'

trainPath='/home/yipei/Twitter/FeatureExtraction/data/trainfile/LRbase/'
trainfile = path.join(trainPath, userID+'.txt')


def GetTrainData(sample_list, tag):
    global tweet_info_path, user_path, mutual_path
    global follow_dict, follower_dict

    train_pool = []
    for ID in sample_list:
        #print ID
        tweetfile = path.join(tweet_info_path, str(ID)+'.txt')
        tweet_feat, authorID = Processor.GetTweetFeature(tweetfile)

        authorfile = path.join(user_path, str(authorID)+'.txt')
        author_feat = Processor.GetAuthorFeature(authorfile)

        userfile = path.join(user_path, str(userID)+'.txt')
        user_feat = Processor.GetUserFeature(userfile)

        relation_feat = Processor.GetRelationFeature(int(userID), int(authorID), follower_dict, follow_dict, mutual_path)
        #instance: label, feat_list
        train_pool += [(tag, tweet_feat+author_feat+user_feat+relation_feat[0:2])]

    return train_pool

if path.exists(retweet_list_file):
    positive_list = Reader.LoadID(retweet_list_file)
    all_list = Reader.LoadID(all_retweet_file)
    negative_list = list(set(all_list)-set(positive_list))

    follow_dict, follower_dict = Reader.LoadNetwork(networkfile)

    print "%s positive: %s, negative: %s" % (userID, len(positive_list), len(negative_list))

    pos_pool = GetTrainData(positive_list, '1')
    neg_pool = GetTrainData(negative_list, '0')
    print len(pos_pool), len(neg_pool)

    Writer.outputData(trainfile, pos_pool+neg_pool)
else:
    print "no retweets ", userID
