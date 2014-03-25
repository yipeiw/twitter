#!/bin/bash

root=/home/yipei/Twitter

tool=$root/FeatureExtraction/code/content/CollectDict.py

filelist=$root/FeatureExtraction/test.list

outputPath=$root/FeatureExtraction/data/content
mkdir -p $outputPath

output=$outputPath/test.dict

$tool $filelist $output
