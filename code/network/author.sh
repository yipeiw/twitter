#!/bin/bash

root=/home/yipei/Twitter

tool=$root/FeatureExtraction/code/network/ExtractAuthorInfo.py

dataPath=/home/haoyuw/twitter/v2/subnetwork_v2

outputPath=$root/FeatureExtraction/data/network/author
mkdir -p $outputPath

for authorfile in $dataPath/*.txt;
do
    $tool $authorfile $outputPath
done
