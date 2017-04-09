#!/usr/bin/env python
import rospy
from std_msgs.msg       import String, Empty
import time
from geometry_msgs.msg  import Twist
from ardrone_autonomy.msg import Navdata
from multiprocessing import Process
from math import pow,atan2,sqrt
import launch_drone

class ardrone():

    def __init__(self):
        #Creating our node,publisher and subscriber
        rospy.init_node('ardrone_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1000)
        self.navdata_subscriber = rospy.Subscriber('/ardrone/navdata', Navdata, self.callback)
        self.navdata = Navdata()
        self.rate = rospy.Rate(10)

    #Callback function implementing the pose value received
    def callback(self, data):
        self.navdata = data
#        self.navdata.x = round(self.navdata.x, 4)
#        self.navdata.y = round(self.navdata.y, 4)
        self.navdata.altd = round(self.navdata.altd, 4)

#    def get_distance(self, goal_x, goal_y):
#        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
#        return distance

    def get_altitude(self, goal_alt):
        altitude = goal_alt - self.navdata.altd
        return altitude

#    def move2goal(self):
#        goal_pose = Pose()
#        goal_pose.x = input("Set your x goal:")
#        goal_pose.y = input("Set your y goal:")
#        distance_tolerance = input("Set your tolerance:")
#        vel_msg = Twist()

    def move2alt(self):
        #goal_alt = Navdata()
        goal_alt = input("Set your alt:")
        altitude_tolerance = 10
        vel_msg = Twist()

#    if(self.navdata.altd >= goal_alt):
#        vel_msg.linear.z = abs(vel_msg.linear.z)
#    else:
#        vel_msg.linear.z = -abs(vel_msg.linear.z)
#        while sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2)) >= distance_tolerance:
        while goal_alt - self.navdata.altd >= altitude_tolerance:
            #Porportional Controller
            #linear velocity in the x-axis:
#            vel_msg.linear.x = 1.5 * sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 1.5 * (goal_alt - self.navdata.altd)

            #angular velocity in the z-axis:
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
#            vel_msg.angular.z = 4 * (atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) - self.pose.theta)
            vel_msg.angular.z = 0
            #Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        #Stopping our robot after the movement is over
#        vel_msg.linear.x = 0
        vel_msg.linear.z = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

        while goal_alt - self.navdata.altd < altitude_tolerance:
            #Porportional Controller
            #linear velocity in the x-axis:
#            vel_msg.linear.x = 1.5 * sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = -abs(goal_alt - self.navdata.altd)

            #angular velocity in the z-axis:
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
#            vel_msg.angular.z = 4 * (atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) - self.pose.theta)
            vel_msg.angular.z = 0
            #Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        #Stopping our robot after the movement is over
#        vel_msg.linear.x = 0
        vel_msg.linear.z = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

        rospy.spin()
if __name__ == '__main__':
    try:
        launch_drone.takeoff()
        #Testing our function
        x = ardrone()
        x.move2alt
        time.sleep(300)
        launch_drone.land()

    except rospy.ROSInterruptException: pass
