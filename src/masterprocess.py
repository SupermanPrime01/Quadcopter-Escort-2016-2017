#!/usr/bin/env python
#Uses scripts and calls upon functions within scripts
import rospy
from launch_drone import takeoff, land
import altitude_drone
#from rotatez_drone import ardrone
#from forward_drone import move
import time
from multiprocessing import Process

takeofftime = int(input("Enter Sleep Time After Takeoff Command"))
alttime = int(input("Enter Sleep Time After Altitude Command"))
# timeout = int(input("Enter Loop Time"))
if __name__ == '__main__':
    try:

        p1 = Process(target = takeoff)
        p1.start() #launches drone ~1m
        time.sleep(takeofftime) #seconds
        ardrone = altitude_drone.ardrone()
#        ardrone.move2alt()
        p2 = Process(target = ardrone.move2alt)
        p2.start()
        time.sleep(alttime) #seconds
        p3 = Process(target = land)
        p3.start()
        time.sleep(5)
        p1.terminate()
#        p3.terminate()
#        ardrone = ardrone()
#        ardrone.move2alt() #mm in height
#        time.sleep(alttime) #seconds

    except rospy.ROSInterruptException: pass


'''
while time.time() < timeout:
    qc.rotate2goal()
    time.sleep(2)
    move()
    time.sleep(2)
'''

land() #decreases the drone altitude and lands
