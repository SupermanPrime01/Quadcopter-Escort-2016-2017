#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time
from std_msgs.msg         import String, Empty
from nmea_msgs.msg import Sentence
from sensor_msgs.msg import NavSatFix
import math
#from gps_str_2_float_v7 import hyp_ft
#from document that has the average import average as avg_dis

'''
#Code for AR 2.0 stopping based off goal_pose
class GPS():

    def __init__(self):
        #Creating our node, publisher & Subscriber
        rospy.init_node('gps_pub', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1000)
        self.gps_subscriber = rospy.Subscriber('/gps/gpsnode', )
'''
#if distance is greater than 15 feet then move forward
#if distance is less than 10 feet then move back
'''
def distance_change():
    actual_distance = 14
    print actual_distance
    sleep(150)
    actual_distance = 18
    print actual_distance
    sleep(150)
'''
class Forward():
    def __init__(self):
        rospy.init_node('qc_forward', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1000)
        self.rospy.Subscriber("/fix", NavSatFix, callback)
        self.navsatfix = NavSatFix()
        self.rate = rospy.Rate(10)

    def callback(self, data):
        self.navsatfix = data
        self.navsatfix.latitude = round(self.navsatfix.latitude, 6)
        self.navsatfix.longitude = round(self.navsatfix.longitude, 6)

    def get_dist(self, goal_dist):
        distance = goal_dist - self.


    def move(self, velocity_publisher):
        # Starts a new node
        vel_msg = Twist()
        speed = 1
        #Receiveing the user's input
        print("Let's move your robot")
        #actual_distance = input("Enter the actual distance:")
        #input("Type your distance:")
    #    if avg_distance <= actual_distance: # If the GPS distance is less than or equal to the actual distance execute the following code
        hyp_ft = input("Enter hyp_ft")
        if hyp_ft >= 15:
            distance =  1.5 #avg_dis - 10
            isForward = True #input("Forward?: ")#True or False
        elif hyp_ft <= 10:
            distance = 1.5
            isForward = False
        else:
            distance = 0
            isForward = True
    #    elif avg_dis >= actual_distance: # If the GPS distance is less than or equal to the actual distance execute the following code
    #        pass


        #Checking if the movement is forward or backwards
        if(isForward):
            vel_msg.linear.x = abs(speed)
        else:
            vel_msg.linear.x = -abs(speed)
        #Since we are moving just in x-axis
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)


if __name__ == '__main__':
    rospy.init_node('qc_forward', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1000)
    try:
        timeout = time.time() + 300
        while time.time() < timeout:
            #distance_change*()
            move(velocity_publisher)
    except rospy.ROSInterruptException:
        pass

        #Testing our function
#         for i in range(3): // Failed multiple function command
#    [move() for m in range(3)] // Failed multiple function command
# def repeat_fun(times, f):
#    for i in range(times): f()
