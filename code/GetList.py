#!/usr/bin/env python

retweet = '/home/haoyuw/twitter/v2/retweets.txt'

import sys

select = int(sys.argv[1])
output = sys.argv[2]

fout = open(output, 'w')
count = 0

for line in open(retweet):
    ID = line.strip().split()[0]
    fout.write("%s\n" % (ID))
    count += 1
    if count > select:
        break

fout.close()
