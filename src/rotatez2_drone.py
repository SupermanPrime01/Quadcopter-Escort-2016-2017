#!/usr/bin/env python
import rospy
from std_msgs.msg       import String, Empty
import time
from geometry_msgs.msg import Twist
from ardrone_autonomy.msg import Navdata
from multiprocessing import Process
from math import pow,atan2,sqrt
PI = 3.1415926535897

GVlat = float(input("Input the GV Latitude:"))
GVlong = float(input("Input the GV Longitude:"))

QClat = float(input("Input the QC Latitude:"))
QClong = float(input("Input the QC Longitude:"))

#delta longitutde and delta latitude
d_lat = float(GVlat - QClat)
d_long = float(GVlong - QClong)

def theta(d_lat,d_long):
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


def rotZ(theta):
    #Quadrant I, II, III
    if theta >= 0 and theta <= 270:
       rotZ = theta - 90

    #Quadrant IV
    elif theta >= 271 and theta <= 360:
        rotZ = -90 - (360-theta)

    print(rotZ)

    return rotZ

class Ardrone():

    def __init__(self):
        #Creating our node,publisher and subscriber
        rospy.init_node('qc_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1000)
        self.navdata_subscriber = rospy.Subscriber('/ardrone/navdata', Navdata, self.callback)
        self.navdata = Navdata()
        self.rate = rospy.Rate(10)

    #Callback function implementing the pose value received
    def callback(self, data):
        self.navdata = data
        self.navdata.rotZ = round(self.navdata.rotZ, 4)


    def get_rotZ(self, goal_rotZ):
        rotation = goal_rotZ - self.navdata.rotZ
        return rotation

    def rotate2goal(self):
        #goal_rotZ = Navdata()
        goal_rotZ = rotZ #input("Set your rot Z goal:")
#        if goal_rotZ > 180:
#            goal_rotZ = input("Set your rot Z goal between +180 & -180:")
#        elif goal_rotZ < -180:
#            goal_rotZ = input("Set your rot Z goal between +180 & -180:")
        # The input should be from 180 to -180.
        rotation_tolerance = 10 #input("Set your tolerance:")
        # The tolerance should be about 10 degrees.
        vel_msg = Twist()

        while goal_rotZ - self.navdata.rotZ >= rotation_tolerance:

            #Porportional Controller
            #linear velocity in the x-axis:
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            #angular velocity in the z-axis:
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            #negative values move the QC clockwise, positive values move the QC counter clockwise
        if(goal_rotZ < 0):
            vel_msg.angular.z = -40 * abs(goal_rotZ - self.navdata.rotZ)
        else:
            vel_msg.angular.z = 40 * abs(goal_rotZ - self.navdata.rotZ)

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
        #Testing our function
        x = Ardrone()
        x.rotate2goal()
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
