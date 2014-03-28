#!/usr/bin/env python

import numpy as np

def SimilarityCos(freq1_dict, freq2_dict):
    freq1_array = []
    freq2_array = []
    c1_array = []
    c2_array = []
    for word in freq1_dict.keys():
        freq1_array += [freq1_dict[word]]
    for word in freq2_dict.keys():
        freq2_array += [freq2_dict[word]]
        if freq1_dict[word] > 0:
            c1_array += [freq1_dict[word]]
            c2_array += [freq2_dict[word]]

    n1 = np.linalg.norm(freq1_array)
    n2 = np.linalg.norm(freq2_array)
    if n1==0 or n2==0 or len(c1_array)==0:
        return 0
    else:
        return np.dot(c1_array, c2_array)/n1/n2

