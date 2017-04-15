#!/usr/bin/env python

import rospy
import math
import time

def range():
    timeout = time.time() + 60
        while time.time() < timeout:
            #QC too close to GV
            if distance < 6ft:
                vel_msg.linear.x = -value
                until distance is > 6ft
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0
            #QC too far from GV
            elif distance > 10ft:
                vel_msg.linear.x = +value
                until distance is < 10ft
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0
            #QC is just right from GV
            elif distance > 6ft and distance < 10ft:
                vel_msg.linear.x = 0
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0


