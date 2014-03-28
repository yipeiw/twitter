#!/bin/bash

root=/home/yipei/Twitter

tool=$root/FeatureExtraction/code/content/RawFreq.py

filelist=$root/FeatureExtraction/v2.list

outputPath=$root/FeatureExtraction/data/content/UserInterest/RawFreq
mkdir -p $outputPath

$tool $filelist $outputPath
