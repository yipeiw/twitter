#!/bin/bash

root=/home/yipei/Twitter/FeatureExtraction

tool=$root/code/user/ExtractInfo.py

filelist=$root/v3.test.list
outputPath=$root/data/user_v3
mkdir -p $outputPath

$tool $filelist $outputPath
