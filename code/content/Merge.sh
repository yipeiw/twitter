#!/bin/bash

root=/home/yipei/Twitter/FeatureExtraction

tool=$root/code/content/merge.py

bofPath=$root/data/content/BOW

boffile=$bofPath/10073042.bof

outputPath=$root/data/content/UserInterest
mkdir -p $outputPath

$tool $boffile $outputPath
