#!/usr/bin/env python

def WriteBOF(filepath, bof_dict):
    item_list = []
    fout = open(filepath, 'w')
    for idx, val in sorted(bof_dict.items(), key=lambda item:item[0]):
        item_list += ["%s:%s" % (idx, val)]
    fout.write("%s\n" % (" ".join(item_list)))
    fout.close()

def WriteFeat(fout, feat_dict):
    

def WriteLabels(fout, decision):
    return
