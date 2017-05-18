#!/usr/bin/env python

import rospy
import message_filters
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import String, Float32
from geometry_msgs.msg  import Twist
import time


class Forward():

    def __init__(self):
        rospy.Subscriber("gps_dist", Float32, self.callback)
        self.data = Float32()
        self.rate = rospy.Rate(10)

    def callback(self, data):
#       rospy.loginfo(rospy.get_caller_id() + "I heard %s", self.data.data)
        while True:
            rospy.loginfo_throttle(10, self.data.data)
        hyp_ft = self.data

'''Moving Average

history = []

def callback(msg):
    global history
    history.append(msg.data)
    if len(history) > 60:
        history = history[-60:]
    average = sum(history) / float(len(history))
    rospy.loginfo('Average of most recent {} samples: {}'.format(len(history), average))


n = rospy.init_node('moving_average')
s = rospy.Subscriber('/numbers', Int32, callback)
rospy.spin()
        
'''
        
    def move(self, velocity_publisher):
        vel_msg = Twist()
        hyp_ft = self.data.data

        #Receiveing the user's input
#       print("Let's move your robot")
        speed = 1 #input("Input your speed:")
    #    distance = input("Type your distance:")
    #    isForward = input("Foward?: ")#True or False
        if hyp_ft >= 20:
            distance = 1.5
            isForward = True
        elif hyp_ft <= 10:
            distance = 1.5
            isForward = False
        else:
            distance = 0
            isForward = True

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
    # Starts a new node
    rospy.init_node('qc_forward', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    try:
        print("Let's move your robot")
        timeout =  time.time() + 600
        while time.time() < timeout:
            x = Forward()
            x.move(velocity_publisher)
            time.sleep(30)
            print("Aquiring GPS")
        else:
            rospy.spin()
    except rospy.ROSInterruptException:
        pass
