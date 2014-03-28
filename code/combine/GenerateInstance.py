#!/usr/bin/env python

import sys

tweet = sys.argv[1]
contentfile = sys.argv[2]
authorfile = sys.argv[3]
featurefile = sys.argv[4]

Global, user_dict = LoadSim(contentfile)
author_feat = LoadAuthor(authorfile)

fout = open(featurefile, 'w')
Writer.WriteFeat(fout, author_feat)
Writer.WriteFeat(fout, Global)
Writer.WriteFeat(fout, user_dict)
fout.close()
