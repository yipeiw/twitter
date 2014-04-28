#!/bin/bash

root=/home/yipei/Twitter/FeatureExtraction

tool=$root/code/analysis/UserInterest.py

filelist=$root/tweet100.list
output=$root/tweet100.user.interest.txt

$tool $filelist $output
