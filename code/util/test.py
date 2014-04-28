#!/usr/bin/env python

import json

userfile='/home/haoyuw/twitter/v3/json/15846407.txt'

count = 0
for line in open(userfile):
    data = json.loads(str(line.strip()))
    print data['id']
    print data['text']
    print data.keys()
    #for k, v in data['user'].items():
     #   print k, v

    count += 1
    if count > 0:
        break
