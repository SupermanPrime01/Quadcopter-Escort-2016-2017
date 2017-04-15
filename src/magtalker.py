#!/usr/bin/env python


# Python code to have subscribe to /ardrone/navdata and to publish magX and magY data

import rospy
from std_msgs.msg import String
from ardrone_autonomy.msg import Navdata, navdata_altitude
from std_msgs.msg import Float32
import math

import math
import normalize_position as norm

def magtalker():
    pub = rospy.Publisher('magchatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
