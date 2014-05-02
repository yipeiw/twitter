#!/usr/bin/env python

import os.path as path

def outputInfo(user_info, history, outputfile):
    fout = open(outputfile, 'w')
    for name, val in user_info.items():
        fout.write("user_%s,%s\n" % (name, val))
    for name, val in history.items():
        fout.write("history_%s,%s\n" % (name, val))
    fout.close()

def outputTweet(tweet_dict, author, tweetPath):
    for ID, info in tweet_dict.items():
        tweetfile = path.join(tweetPath, str(ID)+'.txt')
        fout = open(tweetfile, 'w')
        text, tweet_info, timestamp = info
        text = " ".join(text.split()) #to avoid new line in tweet

        fout.write("%s\n" % ( text.encode('ascii','ignore') ) )
        fout.write("%s\n" % (author))
        fout.write("%s\n" % (timestamp))
        for name, val in tweet_info.items():
            fout.write("%s:%s\n" % (name, val))
        fout.close()
