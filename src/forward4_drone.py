#!/usr/bin/env python
import rospy
from std_msgs.msg       import String, Empty
import time
from geometry_msgs.msg import Twist
from ardrone_autonomy.msg import Navdata
from nav_msgs.msg       import Odometry #This is where the QC's positional data is located
from multiprocessing import Process
from nmea_msgs import Sentence
from math import * #pow,atan2,sqrt
PI = 3.1415926535897

class QC():

    def __init__(self):
        #Creating our node,publisher and subscriber
        rospy.init_node('qc_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1000)
        #Need to replace with GPS node
        self.navdata_subscriber = rospy.Subscriber('/fix', Sentence, self.callback)
        #Change this to GPS node
        self.navdata = Sentence()
        self.rate = rospy.Rate(10)

    #Callback function implementing the pose value received
    #Change callback function to QC GPS
    def callback(self, data):
        self.pose = data
        self.odometry.x = round(self.odometry.x, 4)
        self.odometry.y = round(self.odometry.y, 4)

    # Will put GV GPS as goals
    def get_distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        return distance

    def move2goal(self):
        goal_pose = Odometry()
        #Set goals to GV GPS
        goal_pose.x = input("Set your x goal:")
        goal_pose.y = input("Set your y goal:")
        distance_tolerance = 0.5
        vel_msg = Twist()

        while sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2)) >= distance_tolerance:

            #Porportional Controller
            #linear velocity in the x-axis:
            if sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2)) <= 6:
                vel_msg.linear.x = -1.5 * sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
            elif sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2)) >= 10:
                vel_msg.linear.x = -1.5 * sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
            else:
                vel_msg.linear.z = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            #angular velocity in the z-axis:
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0

            #Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        #Stopping our robot after the movement is over
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

        rospy.spin()

if __name__ == '__main__':
    try:
        timeout = time.time() + 60
        while time.time() < timeout:
            #Testing our function
            x = QC()
            x.move2goal()

    except rospy.ROSInterruptException:
        pass

'''
def rotate():
    #Starts a new node
    rospy.init_node('qc_rotate', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1000)
    vel_msg = Twist()

    # Receiveing the user's input
    print("Let's rotate your robot")
    speed = 45 #input("Input your speed (degrees/sec):")
    angle = input("Type your distance (degrees):")
    clockwise = input("Clockwise?: ") #True or false

    #Converting from angles to radians
    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360

    #We wont use linear components
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    # Checking if our movement is CW or CCW
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)


    #Forcing our robot to stop
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    rospy.spin()

if __name__ == '__main__':
    try:
        # Testing our function
        rotate()
    except rospy.ROSInterruptException:
        pass
'''
