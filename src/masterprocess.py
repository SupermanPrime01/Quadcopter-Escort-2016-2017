#!/usr/bin/env python
#Uses scripts and calls upon functions within scripts
from launch_drone import takeoff, land
from altitude_drone import ardrone
#from rotatez_drone import ardrone
#from forward_drone import move
import time

takeofftime = int(input("Enter Sleep Time After Takeoff Command"))
alttime = int(input("Enter Sleep Time After Altitude Command"))
# timeout = int(input("Enter Loop Time"))

takeoff() #launches drone ~1m
time.sleep(takeofftime) #seconds
ardrone.move2alt() #mm in height
time.sleep(alttime) #seconds

'''
while time.time() < timeout:
    qc.rotate2goal()
    time.sleep(2)
    move()
    time.sleep(2)
'''

land() #decreases the drone altitude and lands
