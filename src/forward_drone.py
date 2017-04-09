#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time
from launch_drone import takeoff

def move():
    # Starts a new node
    rospy.init_node('qc_forward', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1000)
    vel_msg = Twist()

    #Receiveing the user's input
    print("Let's move your robot")
    speed = 1
    distance = input("Type your distance:")
    isForward = True#True or False

    #Checking if the movement is forward or backwards in mm/second
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

    while not rospy.is_shutdown():

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

def land():
    pub = rospy.Publisher("ardrone/land", Empty, queue_size=10 )
    rospy.init_node('land', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()


if __name__ == '__main__':

#    takeoff()

    rospy.Duration(60*5)
    while rospy.Time.now() <= rospy.Duration(60*5):
        move()


#land()


        #Testing our function
#         for i in range(3): // Failed multiple function command
#    [move() for m in range(3)] // Failed multiple function command
# def repeat_fun(times, f):
#    for i in range(times): f()
