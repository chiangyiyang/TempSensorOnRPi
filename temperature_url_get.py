#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import time, RPi.GPIO as GPIO
import urllib
import time, datetime
from time import strftime


# Post and Get function
def fetch_thing(url, params, method):
    params = urllib.urlencode(params)
    if method == 'POST':
        f = urllib.urlopen(url, params)
    else:
        f = urllib.urlopen(url + '?' + params)
    return (f.read(), f.code)


# now = strftime('%H:%M:%S')
# print now
# 
# file = open("/sys/bus/w1/devices/28-0115b220c8ff/w1_slave")
# text = file.read()
# file.close()
# 
# secondline = text.split("\n")[1]
# tempdata = secondline.split(" ")[9]
# temp = float(tempdata[2:]) / 1000
# 
# print "now:" + now + "  temperature=" + str(temp)
# 
# content, response_code = fetch_thing(
#     'http://192.168.43.233:8081/iot/get_api.php',
#     {'userid':1, 'temperature':temp},
#     'GET'
# )


def getLocalTime(utc_time):
    from datetime import datetime
    import calendar
    import os
    
    os.environ['TZ'] = 'Asia/Taipei'
    d = datetime.strptime(utc_time, "%Y-%m-%d %H:%M:%S")
    utc_ts = calendar.timegm(d.utctimetuple())
    return datetime.fromtimestamp(utc_ts).replace(microsecond=d.microsecond)



while(True):
    now = getLocalTime(strftime("%Y-%m-%d %H:%M:%S"))
    print now
    
    file = open("/sys/bus/w1/devices/28-0115b220c8ff/w1_slave")
    text = file.read()
    file.close()
    
    secondline = text.split("\n")[1]
    tempdata = secondline.split(" ")[9]
    temp = float(tempdata[2:]) / 1000
    
    print "now:" + now.strftime('%H:%M:%S') + "  temperature=" + str(temp)
    
    content, response_code = fetch_thing(
        'http://192.168.43.233:8081/iot/get_api.php',
        {'userid': 1, 'temperature': temp},
        'GET'
    )
    time.sleep(5)
