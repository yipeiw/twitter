#!/usr/bin/env python

from stemmer import PorterStemmer
import re

stemmer = PorterStemmer()

def process_word(word, strategy=0):
        word = word.lower()
        if strategy==1:
            [w, score] = MapWord(word)
            if score>0:
                return w
            else:
                return normalize(word)
        else:
            return normalize(word)

def normalize(word):
    if CheckSpecial(word):
        return ""
    word = re.sub("[^a-z]", "", word)
    return stemmer.stem(word)

def CheckSpecial(word):
    special_list = ['~','@', '#', '$', '%', '^', '&', '*', '+']
    for special in special_list:
        if word.find(special)!=-1: 
            return True

    return False


def MapWord(word):
    if word.find('http')==0:
        return ["URL", 1]
    if word.find('#')==0:
        return ["Hash", 1]
    if word.find('@')==0:
        return ["User", 1]
    return ["", -1]
