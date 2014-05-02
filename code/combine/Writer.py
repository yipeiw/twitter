#!/usr/bin/env python

def outputData(trainfile, pool):
    fout = open(trainfile, 'w')
    for sample in pool:
        label, feature_list = sample
        featureline = ",".join([str(item)for item in feature_list])
        fout.write("%s,%s\n" % (label, featureline))
    fout.close()

def outputFeature(featfile, pool):
    fout = open(featfile, 'w')
    for feat_list in pool:
        featureline = ",".join([str(item)for item in feat_list])
        fout.write("%s\n" % (featureline))
    fout.close()

