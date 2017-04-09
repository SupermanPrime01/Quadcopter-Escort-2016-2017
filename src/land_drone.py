#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Empty
import time

#Code used to land QC
def land():
    pub = rospy.Publisher("ardrone/land", Empty, queue_size=10 )
    rospy.init_node('land', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()

if __name__ == '__main__':
   try:
       time.sleep(1) #delays for 20 seconds
       land()
   except rospy.ROSInterruptException:
       pass
