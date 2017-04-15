#!/usr/bin/env python
import rospy
from geometry_msgs.msg  import Twist
import time
from std_msgs.msg       import String, Empty
from nav_msgs.msg       import Odometry

'''
#Code for AR 2.0 stopping based off goal_pose
class GPS():

    def __init__(self):
        #Creating our node, publisher & Subscriber
        rospy.init_node('gps_pub', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1000)
        self.gps_subscriber = rospy.Subscriber('/gps/gpsnode', )
'''
#For positional data and will replace with GPS information
def callback(msg):
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    rospy.loginfo('x: {}, y: {}'.format(x,y))

def move(velocity_publisher):
    # Starts a new node
    vel_msg = Twist()

    #Receiveing the user's input
    print("Let's move your robot")
    speed = 1
    distance = input("Type your distance:")
#   distance = hypotenuse variable
    isForward = input("Forward?: ")#True or False

    #Checking if the movement is forward or backwards
#   if(isForward):
    if distance > 10:
        vel_msg.linear.x = abs(speed)
    elif distance < 6:
        vel_msg.linear.x = -abs(speed)
    else:
        vel_msg.linear.x = 0
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
#   rospy.Subscriber("/odom",Odometry, callback)
    rospy.spin()
    try:
        timeout = time.time() + 60
        while time.time() < timeout:
            move(velocity_publisher)
    except rospy.ROSInterruptException:
        pass

        #Testing our function
#         for i in range(3): // Failed multiple function command
#    [move() for m in range(3)] // Failed multiple function command
# def repeat_fun(times, f):
#    for i in range(times): f()
