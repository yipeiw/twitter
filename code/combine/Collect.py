#!/usr/bin/env python

import os.path as path
import Processor

def GetTrainData(userID, ID, tag, follower_dict, tweet_info_path, user_path, mutual_path):
    tweetfile = path.join(tweet_info_path, str(ID)+'.txt')
    tweet_feat, authorID = Processor.GetTweetFeature(tweetfile)
    
    authorfile = path.join(user_path, str(authorID)+'.txt')
    author_feat = Processor.GetAuthorFeature(authorfile)

    userfile = path.join(user_path, str(userID)+'.txt')
    user_feat = Processor.GetUserFeature(userfile)
    
    relation_feat = Processor.GetRelationFeature(userID, authorID, follower_dict, mutual_path)
    
    #instance: label, feat_list
    return (tag, tweet_feat+author_feat+user_feat+relation_feat)

