#!/usr/bin/env python

def GetUserInfo(userjson):
    info = {}
    info['follow'] = userjson['followers_count']
    info['friend'] = userjson['friends_count']
    return info 

def GetTweetInfo(tweet):
    has_url = False
    has_mention = False
    has_hashtag = False
    origin = True

    if tweet.find('RT')!=-1:
        origin = False
    if tweet.find("http:")!=-1:
        has_url = True
    for word in tweet.split():
        if word[0]=="#":
            has_hashtag= True
        if word[0]=="@":
            has_mention = True
    info = {'origin':origin, 'has_url':has_url, 'has_mention':has_mention, 'has_hashtag':has_hashtag}
    return info

#below functions are all for text format
def GetText(entry):
    start = entry.find(", text='") + len(", text='")
    end = entry.find("', source=")
    #print start, end
    #print entry[start:end]
    return entry[start:end]

def GetTimeStamp(entry):
    start = entry.find('createdAt=') + len('createdAt=')
    end = entry.find(', id=')
    return entry[start:end]

def GetCreditInfo(entry):
    s0 = entry.find('id=') + len('id=')
    e0 = entry.find(', text=')
    tweet_id = entry[s0:e0]

    s1 = entry.find('followersCount=')+len('followersCount=')
    sub1 = entry[s1:len(entry)]
    e1 = sub1.find(',') + s1
    follow_num = int(entry[s1:e1])

    s2 = entry.find('friendsCount=') + len('friendsCount=')
    sub2 = entry[s2:len(entry)]
    e2 = sub2.find(',')+s2
    friend_num = int(entry[s2:e2])

    return tweet_id, follow_num, friend_num
