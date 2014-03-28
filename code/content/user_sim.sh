#!/bin/bash

root=/home/yipei/Twitter/FeatureExtraction

tool=$root/code/content/UserSimilarity.py

dataPath=/home/haoyuw/twitter/v2
userinfo=$dataPath/sub_v2.txt

topicPath=$root/data/content/UserInterest/RawFreq

output=$root/data/content/Similarity/user.txt

$tool $userinfo $topicPath $output
