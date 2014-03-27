#!/usr/bin/env python

def GetText(entry):
    start = entry.find(", text='") + len("text='")
    end = entry.find("', source=")
    #print start, end
    #print entry[start:end]
    return entry[start:end]

def GetCreditInfo(entry):
    s0 = entry.find('id=') + len('id=')
    e0 = entry.find(', text=')
    tweet_id = entry[s0:e0]

    s1 = entry.find('followersCount=')+len('followersCount=')
    sub1 = entry[s1:len(entry)]
    e1 = sub1.find(',') + s1
    print entry[s1:s1+10]
    follow_num = int(entry[s1:e1])

    s2 = entry.find('friendsCount=') + len('friendsCount=')
    sub2 = entry[s2:len(entry)]
    e2 = sub2.find(',')+s2
    friend_num = int(entry[s2:e2])

    return tweet_id, follow_num, friend_num
