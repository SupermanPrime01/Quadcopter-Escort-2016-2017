#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time
from std_msgs.msg import String, Float32
from nmea_msgs.msg import Sentence

class Forward():

    def __init__(self):
        self.distance_subscriber = rospy.Subscriber("/gps_dist", Float32, self.callback)
        self.float32 = Float32()
        self.rate = rospy.Rate(10)

    def callback(self, data, goal_dist):
        self.float32 = data.float32
        self.float32.gps_dist = round(self.float32.gps_dist, 4)
        distance = goal_dist - self.float32.gps_dist
        return distance

#    def get_distance(self, goal_dist):
#        distance = goal_dist - self.float32.gps_dist
#        return distance

    def move(self, velocity_publisher):
        vel_msg = Twist()

        #Receiveing the user's input
        print("Let's move your robot")
        speed = 1 #input("Input your speed:")
    #   distance = input("Type your distance:")
    #    isForward = input("Foward?: ")True or False
        #GPS distance in feet
        if self.gps_dist >= 20:
            distance = 1.5
            isForward = True
        elif self.gps_dist <= 10:
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
            self.velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        #Force the robot to stop
        self.velocity_publisher.publish(vel_msg)


if __name__ == '__main__':
    # Starts a new node
#    rospy.init_node('robot_cleaner', anonymous=True)
#    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
#    distance_subscriber = rospy.Subscriber("/gps_dist", Float32, callback)
    rospy.init_node('qc_foward', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    '''
    self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    self.distance_subscriber = rospy.Subscriber("/gps_dist", Float32, self.callback)
    self.float32 = Float32()
    self.rate = rospy.Rate(10)
    '''
    try:
     timeout =  time.time() + 60
     while time.time() < timeout:
         x = Forward()
         x.move(velocity_publisher)
         time.sleep(30)

    except rospy.ROSInterruptException:
     pass
