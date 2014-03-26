#!/bin/bash

root=/home/yipei/Twitter

tool=$root/FeatureExtraction/code/content/TFIDF.py

filelist=$root/FeatureExtraction/test.list

dict=$root/FeatureExtraction/data/content/test.dict

outputPath=$root/FeatureExtraction/data/content/BOW
mkdir -p $outputPath

$tool $filelist $dict $outputPath
