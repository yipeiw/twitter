#!/usr/bin/env python

def GetText(entry):
    subString = entry[0:entry.find('userMentionEntities')]
    start = entry.find(", text='") + len("text='")
    end = entry.find("', source=")
    #print start, end
    #print entry[start:end]
    return entry[start:end]
