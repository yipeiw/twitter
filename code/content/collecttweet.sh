#!/bin/bash

root=/home/yipei/Twitter

tool=$root/FeatureExtraction/code/content/cleanText.py

filelist=$root/FeatureExtraction/v2.list

outputPath=$root/FeatureExtraction/data/content/tweets
mkdir -p $outputPath

$tool $filelist $outputPath
