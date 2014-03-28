#!/bin/bash

root=/home/yipei/Twitter

tool=$root/FeatureExtraction/code/content/TFIDF.py

filelist=$root/FeatureExtraction/v2.list

dict=$root/FeatureExtraction/data/content/v2.dict

outputPath=$root/FeatureExtraction/data/content/BOW
mkdir -p $outputPath

$tool $filelist $dict $outputPath
