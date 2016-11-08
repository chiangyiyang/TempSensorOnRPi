#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import time, datetime
from time import strftime

temperature = file("Temp.txt", "w")
for num in range(5):
    now = strftime('%H:%M:%S')
    # print now
    file = open("/sys/bus/w1/devices/28-0115b220c8ff/w1_slave")
    text = file.read()
    file.close()
    
    # print text     //all
    
    secondline = text.split("\n")[1]
    # print secondline
    
    tempdata = secondline.split(" ")[9]
    # print tempdata
    temp = float(tempdata[2:]) / 1000
    # print temp
    print "now:" + now + "  temperature=" + str(temp) + "    fffff rui"
    temperature.write(str(now) + " " + str(temp) + "\n")
    
    time.sleep(1)
