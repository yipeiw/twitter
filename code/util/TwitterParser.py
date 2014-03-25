#!/usr/bin/env python

def GetText(entry):
    start = entry.find("text='") + len("text='")
    end = entry.find("', source=")
    return entry[start:end]
