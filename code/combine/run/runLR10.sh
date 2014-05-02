#!/bin/bash

root=/home/yipei/Twitter/FeatureExtraction

tool=$root/code/combine/LRTrainData.py

userlist=$root/filelist/v3_10.txt

for user in $(cat $userlist);
do
    echo "$tool $user"
    time $tool $user
done
