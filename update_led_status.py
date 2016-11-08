#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time
import urllib, urllib2
import json

GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

while (1):
    while (1):
        try:
            response = urllib2.urlopen(
                'http://192.168.43.233:8081/iot/led_status.php',
                timeout=10
            )
        except:
            print "failed to open"
            time.sleep(10)
        else:
            break
    try:
        decoded = json.load(response)
        id = decoded[0]['ID']
        status = decoded[0]['status']
        print "Status is : ", status
        if status == '1':
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(2)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(2)
    except ValueError:
        print "json load error"
        time.sleep(10)
    
    except KeyboardInterrupt:
        print "\n\rprogram ended"
        break

GPIO.cleanup()



