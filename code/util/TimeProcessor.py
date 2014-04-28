#!/usr/bin/env python

def parse(timestamp):
    #Wed Mar 12 19:29:02 EDT 2014
    #assume in the same year, same time zone 
    weekday, month, date, clock, timezone, year = timestamp.split()
    month_map = {"Jan":1,"Feb":2, "Mar":3, "April":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
    return {'date':int(date), 'month':month_map[month], 'clock':clock}

#unit:sec
def Calculate(time1, time2):
    month_diff = time1['month']-time2['month']
    date_diff = time1['date']-time2['date']
    time_diff = TransformToSec(time1['clock'])-TransformToSec(time2['clock'])
    return (month_diff*30+date_diff)*24*3600+time_diff

def TransformToSec(clock):
    hours, mins, secs = clock.split(':')
    return int(hours)*3600 + int(mins)*60+int(secs)

def Compare(time1, time2):
    if Calculate(time1, time2) <= 0:
        return 1
    else:
        return -1
