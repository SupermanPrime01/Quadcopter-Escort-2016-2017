#!/usr/bin/env python

import rospy
import message_filters
from sensor_msgs.msg import NavSatFix


def calc_distance(gps1, gps2):
    gps1_lat = round(gps1.latitude, 6)
    gps1_lon = round(gps1.longitude, 6)
    gps2_lat = round(gps2.latitude, 6)
    gps2_lon = round(gps2.longitude, 6)
    delta_lat = (gps1_lat*(108000) - gps2_lat*(108000))
    delta_lon = (gps1_lon*(108000) - gps2_lon*(108000))
    hyp_m = (delta_lat**2 + delta_lon**2)**0.5
    hyp_ft = (hyp_m*3.2800839)
    rospy.loginfo("Distance is %s in ft.", hyp_ft)



def listener():
    rospy.init_node('gps_monitor', anonymous=True)
    gps1 = message_filters.Subscriber('/fix', NavSatFix)
    gps2 = message_filters.Subscriber('/fix1', NavSatFix)
    ts = message_filters.ApproximateTimeSynchronizer([gps1, gps2], 10, 5)
    ts.registerCallback(calc_distance)
    rospy.spin()


if __name__ == '__main__':
    listener()
