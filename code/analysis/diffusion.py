#!/usr/bin/env python

"""
tweet diffusion patter through network
author
-> one step users retweet num:total num
-> two steps ...
-> threee steps

for each retweeter, whether they are connected with the author, whether connected with other retweeters
"""
import sys
sys.path.append('/home/yipei/Twitter/FeatureExtraction/code/relation')
import Reader
import Processor

def outputPattern(fout, tweetID, author, pattern, retweet_pattern, within):
    pline = "one %s %s, two %s %s, three %s %s" % (pattern[0][0], pattern[0][1], pattern[1][0], pattern[1][1], pattern[2][0], pattern[2][1])
    fout.write("tweet:%s, author:%s, %s, %s\n\n" % (tweetID, author, within, pline))
    rlist = ["%s:%s" % (u, tag) for u, tag in retweet_pattern]
    rline = ",".join(rlist)
    fout.write(rline+'\n\n')

networkfile='/home/haoyuw/twitter/v3/sub_v3.txt'
retweetfile='/home/haoyuw/twitter/v3/retweets.txt'

follow_dict, follower_dict = Reader.LoadNetwork(networkfile)

outputfile='diffusion_pattern.txt'
fout = open(outputfile, 'w')
count = 0
for line in open(retweetfile):
    tweetID, author, num, retweets = line.strip().split()
    retweet_set = set([int(u) for u in retweets.split(',')])
    #print "process ", tweetID

    pattern, retweet_pattern = Processor.GetDiffusion(int(author), follower_dict, retweet_set)
    if pattern[2][0]==len(retweet_set):
        within='yes'
        count += 1
    else:
        within='no'
    outputPattern(fout, tweetID, author, pattern, retweet_pattern, within)

fout.close()
print "within num ", count

