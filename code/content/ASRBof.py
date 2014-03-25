#!/opt/python27/bin/python2.7

import sys
from collections import defaultdict
import os.path as path
from stemmer import PorterStemmer
import re

stemmer = PorterStemmer()

def process_word(word):
    word = word.lower()
    word = re.sub("[^a-z]", "", word)
    return stemmer.stem(word)

asr_file_list = sys.argv[1]
dictfile = sys.argv[2]
outputdir = sys.argv[3]

#load dictionary
dict_idf={}
for line in open(dictfile):
    (index, word, idf) = line.strip().split(' ')
    dict_idf[word]=(int(index), float(idf))
    
for line in open(asr_file_list):
    line = line.strip()
    fin = open(line, 'r')
    clip = path.basename(line).split(".")[0]
    clip = re.sub("H_","",clip)
    wordDict=defaultdict(int)
    print "process ", clip 
    while True:
        line = fin.readline()
        if not line:
            break
	line = line.strip()
        if line.find('-->')!=-1:
            line = fin.readline()
	    line = line.strip()
            tokens = re.split('\s+|_', line)
	    if clip == "HVC000965":
                print line
		print tokens
            for token in tokens:
                word = process_word(token)
                wordDict[word] += 1

    #calculate tf-idf and output result
    output_vector=[]
    for word, count in wordDict.items():
	if not word in dict_idf.keys():
		print "word not in dict:%s" % word
	else:
        	output_vector.append((dict_idf[word][0], count * dict_idf[word][1]))
    total = sum([item for index, item in output_vector])
    output_vector = [(index, item/total) for index, item in output_vector]

    output_vector = sorted(output_vector, key=lambda item:item[0])
    
    boffile = path.join(outputdir, clip+'.bof')
    fout=open(boffile, 'w')
    outputlist = ["{0}:{1}".format(index, value) for index, value in output_vector]
    fout.write(" ".join(outputlist))
    fout.close()
    
