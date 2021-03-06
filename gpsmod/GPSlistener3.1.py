#!/usr/bin/env python
import rospy
import message_filters
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import String, Float32
import time


def calc_distance(gps1, gps2):
    gps1_lat = round(gps1.latitude, 6)
    gps1_lon = round(gps1.longitude, 6)
    gps2_lat = round(gps2.latitude, 6)
    gps2_lon = round(gps2.longitude, 6)
    delta_lat = (gps1_lat*(108000) - gps2_lat*(108000))
    delta_lon = (gps1_lon*(108000) - gps2_lon*(108000))
    hyp_m = (delta_lat**2 + delta_lon**2)**0.5
    hyp_ft = (hyp_m*3.2800839)

    f = open( 'hyp_ft.txt', 'a' )
    f.write(str(hyp_ft) + '\n' )
    f.close()

    while True:
        time.sleep(60)
        with open('hyp_ft.txt') as fh:
            sum = 0 # initialize here, outside the loop
            count = 0 # and a line counter

            for line in fh:
                count += 1 # increment the counter
                if count == 59
                    sum += float(line) #convert the lines to floats
                    break # to come out of the for loop

           average = sum / (count + 1) # as your count is still 59 not 60 what you actually want
           print average

        fh.truncate()
        fh.close()


    pub = rospy.Publisher("gps_dist", Float32, queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        rospy.loginfo("Distance is %s in ft.", hyp_ft)
#        rospy.loginfo(hyp_ft)
        pub.publish(hyp_ft)
        rate.sleep()


def listener():
    rospy.init_node('gps_monitor', anonymous=True)
    gps1 = message_filters.Subscriber('/fix', NavSatFix)
    gps2 = message_filters.Subscriber('/fix1', NavSatFix)
    ts = message_filters.ApproximateTimeSynchronizer([gps1, gps2], 10, 5)
    ts.registerCallback(calc_distance)
    rospy.spin()


if __name__ == '__main__':
    listener()
