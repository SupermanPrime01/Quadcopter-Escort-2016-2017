#!/usr/bin/env python

import rospy
import message_filters
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import String, Float32
from geometry_msgs.msg  import Twist
import time

history = []

def callback(msg):
    x = msg.latitude
    y = msg.longitude
    global history
    history.append(x)
    average = sum(history) / float(len(history))
    except ZeroDivisionError:
            pass
#    history.append(msg.data)
    if len(history) > 60:
#        history = history[-60:]
        del history[:]
    while len(history) is 60:
        pub = rospy.Publisher("avg", Float32,queue_size=10)
        rate = rospy.Rate(1)
    rospy.loginfo("Distance Value after 60 is %s", average)
'''
    try:
        average = sum(history) / float(len(history))
    except ZeroDivisionError:
                pass
'''
#    rospy.loginfo('Average of most recent {} samples: {}'.format(len(history), average))

n = rospy.init_node('moving_average')
s = rospy.Subscriber('/fix', NavSatFix, callback)
rospy.spin()
