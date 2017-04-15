#!/usr/bin/env python
from math import *
import time
import rospy
from std_msgs.msg import String

def alpha(d_lat,d_long):
    GVlat = float((input("Input the GV Latitude:")))
    GVlong = float((input("Input the GV Longitude:")))

    QClat = float((input("Input the QC Latitude:")))
    QClong = float((input("Input the QC Longitude:")))

    # delta longitutde and delta latitude
    d_lat = float((GVlat - QClat))
    d_long = float((GVlong - QClong))

    global theta
    #Quadrant 1
    if d_lat > 0 and d_long > 0:
       theta = degrees(atan(d_long/d_lat))
    elif d_long > 0 and d_lat == 0:
        theta = 90
    elif d_lat > 0 and d_long == 0:
       theta = 0

    #Quadrant 2
    elif d_lat < 0 and d_long > 0:
        theta = 180 - degrees(atan(d_long/abs(d_lat)))
    elif d_long > 0 and d_lat == 0:
        theta = 90
    elif d_lat < 0 and d_long == 0:
        theta = 180

    #Quadrant 3
    elif d_lat < 0 and d_long < 0:
        theta = 180 + degrees(atan(d_long/d_lat))
    elif d_long < 0 and d_lat == 0:
        theta = 270
    elif d_lat < 0  and d_long == 0:
        theta = 180

    #Quadrant 4
    elif d_lat > 0 and d_long < 0:
        theta = 360-degrees(atan(abs(d_long)/d_lat))
    elif d_long < 0 and d_lat == 0:
        theta = 270
    elif d_lat > 0 and d_long == 0:
        theta = 0

    print(theta)


#def rotZ(theta):
    #Quadrant I, II, III
    if theta >= 0 and theta <= 270:
       spin = theta - 90

    #Quadrant IV
    elif theta >= 271 and theta <= 360:
        spin = -90 - (360-theta)

    print(spin)
    return spin

    pub = rospy.Publisher('spin_topic', String, queue_size=10)
    rospy.init_node('spin_node', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo(theta)
        pub.publish(theta)
        rate.sleep()

while not rospy.is_shutdown():
    if __name__ == '__main__':
        # Starts a new node
        try:
            alpha(d_lat, d_long)
        except rospy.ROSInterruptException:
            pass


'''        pub = rospy.Publisher('spin_topic', String, queue_size=20)
        rospy.init_node('spin_node')
        r = rospy.Rate(1) # 1hz
        alpha(d_lat,d_long)
        pub.publish(spin)
#    rotZ(theta)
'''


'''Code to get theta to rotZ format
Quadrant I
for theta in range (0, 90):
    rotZ = theta - 90

Quadrant II
for theta in range (91, 180):
    rotZ = theta - 90

Quadrant III
for theta in range (181, 270):
    rotZ = theta - 90

Quadrant IV
for theta in range (360, 271, -1):
    rotZ = -90 - (360 - theta)
'''
