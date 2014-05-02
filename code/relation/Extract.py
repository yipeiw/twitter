#!/usr/bin/env python

import sys
from collections import defaultdict
import os.path as path

import Reader

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

outputPath = '/home/yipei/Twitter/FeatureExtraction/data/retweets'
retweet_list_file = '/home/yipei/Twitter/FeatureExtraction/data/retweets.list'

mutualPath ='/home/yipei/Twitter/FeatureExtraction/data/mutual'

authorPath = '/home/yipei/Twitter/FeatureExtraction/data/author'

record_retweet, mutual_retweet, id_list = Reader.LoadRetweet(retweetfile)
#follow_dict, follower_dict = LoadNetwork(networkfile)

#output all retweets ID
author_dict = defaultdict(list)
f = open(retweet_list_file, 'w')
for ID, author in id_list:
    f.write("%s %s\n" % (ID, author))
    author_dict[author] += [ID]
f.close()

for author, id_list in author_dict.items():
    filepath = path.join(authorPath, author+'.txt')
    fout = open(filepath, 'w')
    for ID in id_list:
        fout.write("%s\n" % (ID))
    fout.close()


#output retweets positive cases ID for each user
for user, retweets in record_retweet.items():
    outputfile = path.join(outputPath, str(user)+'.txt')    
    fout = open(outputfile, 'w')
    for retweet in retweets:
        fout.write("%s\n" % (retweet))
    fout.close()

#output mutual
mutual_record = defaultdict(list)  
for user1, user2 in mutual_retweet.keys():
    num = len(mutual_retweet[(user1, user2)])
    mutual_record[user1] += [(user2, num, mutual_retweet[(user1, user2)])]
    mutual_record[user2] += [(user1, num, mutual_retweet[(user1, user2)])]

for userID, mutuallist in mutual_record.items():
    outputfile = path.join(mutualPath, str(userID)+'.txt')
    fout = open(outputfile, 'w')
    for user, num, ID_list in sorted(mutuallist, key=lambda item:item[1], reverse=True):
        idline = " ".join(ID_list)
        fout.write("%s %s %s\n" % (user, num, idline))
    fout.close()
