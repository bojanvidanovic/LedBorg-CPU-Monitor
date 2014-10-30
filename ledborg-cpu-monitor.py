#!/usr/bin/env python
# coding: latin-1

# Libraries
import time
import wiringpi2 as wiringpi
import psutil

# WiringPi setup
wiringpi.wiringPiSetup()

# Setup the LedBorg GPIO pins
PIN_RED = 0
PIN_GREEN = 2
PIN_BLUE = 3

wiringpi.pinMode(PIN_RED, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_GREEN, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_BLUE, wiringpi.GPIO.OUTPUT)

# Led Colors
colors = ['001','002','012','022','021','020','120','220','210','100','200']


# Infinite Loop
while True:
    # Current CPU usage
    current = int(psutil.cpu_percent(interval=0) / 10)

    # LedBorg
    color = colors[current]
    wiringpi.digitalWrite(PIN_RED, int(color[0]))
    wiringpi.digitalWrite(PIN_GREEN, int(color[1]))
    wiringpi.digitalWrite(PIN_BLUE, int(color[2]))
                       
    time.sleep(1)                                    
