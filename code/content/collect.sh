#!/bin/bash

root=/home/yipei/Twitter

tool=$root/FeatureExtraction/code/content/CollectDict.py

filelist=$root/FeatureExtraction/v2.list

outputPath=$root/FeatureExtraction/data/content
mkdir -p $outputPath

output=$outputPath/v2.dict

$tool $filelist $output
