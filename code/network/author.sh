#!/bin/bash

root=/home/yipei/Twitter

tool=$root/FeatureExtraction/code/network/ExtractAuthorInfo.py

dataPath=/home/haoyuw/twitter/v2/subnetwork_v2
#authorfile=$dataPath/101614739.txt 
authorfile=$dataPath/46831674.txt
outputPath=$root/FeatureExtraction/data/network/author
mkdir -p $outputPath

$tool $authorfile $outputPath
