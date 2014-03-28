#!/bin/bash

root=/home/yipei/Twitter/FeatureExtraction

tool=$root/code/content/TweetSimilarity.py

tweetPath=$root/data/content/tweets
dataPath=/home/haoyuw/twitter/v2
userinfo=$dataPath/sub_v2.txt

topicPath=$root/data/content/UserInterest/RawFreq

listfile=$root/code/tweet.list

for ID in $(cat $listfile);
do
    tweetfile="$tweetPath/$ID.txt"
    output="$root/data/content/Similarity/tweet/$ID.txt"

    echo "$tool $tweetfile $userinfo $topicPath $output"
    $tool $tweetfile $userinfo $topicPath $output
done
