#!/usr/bin/env python
# coding: latin-1

# Libraries
import time
import psutil

# Led Colors
colors = ['001','002','012','022','021','020','120','220','210','100','200']


# Main function
while True:

    # Current CPU usage
    current = int(psutil.cpu_percent(interval=0))
    if current < 10:
        current = 0
    elif current >= 10:
        current = int(current / 10)

    # LedBorg
    LedBorg = open('/dev/ledborg', 'w')
    LedBorg.write(colors[current])
    LedBorg.close()
    time.sleep(1)
