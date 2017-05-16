#!/usr/bin/env python
import rospy
from std_msgs.msg         import String, Empty
import time
from geometry_msgs.msg    import Twist
from ardrone_autonomy.msg import Navdata
from multiprocessing import Process

#Code used to takeoff QC
def takeoff():
   pub = rospy.Publisher("ardrone/takeoff", Empty, queue_size=10 )
   rospy.init_node('takeoff', anonymous=True)
   rate = rospy.Rate(10) # 10hz
   while not rospy.is_shutdown():
       pub.publish(Empty())
       rate.sleep()


#Code used to land QC
def land():
    pub = rospy.Publisher("ardrone/land", Empty, queue_size=10 )
    rospy.init_node('land', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()


if __name__ == '__main__':

    takeoff()
'''
    p1 = Process(target = takeoff)
    p1.start()
#p2 = Process(target = move2goal)
#p2.start()
#   p3 = Process(target = move2goal)
#   p3 = start()
    time.sleep(300)
    p2 = Process(target = land)
    p2.start()
    time.sleep(10)
    p1.shutdown()

'''
'''
#Code that pulls QC odometry information and passes the info as a changing value
class ardrone():

    def __init__(self):
        #Creating our node,publisher and subscriber
        rospy.init_node('ardrone_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.navdata_subscriber = rospy.Subscriber('/ardrone/navdata', Navdata, self.callback)
        self.navdata = Navdata()
        self.rate = rospy.Rate(10)

    #Callback function implementing the pose value received
    def callback(self, data):
        self.navdata = data
        self.navdata.x = round(self.navdata.x, 4)
        self.navdata.y = round(self.navdata.y, 4)
        self.navdata.z = round(self.navdata.z, 4)
    def get_altitude(goal_z):
        altitude = goal_z - self.navdata.z
        return altitude

#Code for Distance & will be used with GPS Data
'''
'''
    def get_distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.navdata.x), 2) + pow((goal_y - self.navdata.y), 2))
        return distance


def move2goal(self):
        goal_pose = Navdata()
#       goal_pose.x = input("Set your x goal:")
#       goal_pose.y = input("Set your y goal:")
        goal_pose.z = input("Set your z goal:")
        altitude_tolerance = input("Set your tolerance:")
#       distance_tolerance = input("Set your tolerance:")
        vel_msg = Twist()


#       while sqrt(pow((goal_pose.x - self.navdata.x), 2) + pow((goal_pose.y - self.navdata.y), 2)) >= distance_tolerance:
        while goal_pose.z >= altitude_tolerance:

            #Porportional Controller
            #linear velocity in the x-axis:
#           vel_msg.linear.x = 1.5 * sqrt(pow((goal_pose.x - self.navdata.x), 2) + pow((goal_pose.y - self.navdata.y), 2))
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = goal_pose.z - self.navdata.z

            #angular velocity in the z-axis:
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
#           vel_msg.angular.z = 4 * (atan2(goal_pose.y - self.navdata.y, goal_pose.x - self.navdata.x) - self.navdata.theta)
            vel_msg.angular.z = 0

            #Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        #Stopping our robot after the movement is over
        vel_msg.linear.x = 0
        vel_msg.linear.z = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

        rospy.spin()
'''
'''
def rise():
    # Starts a new node
    rospy.init_node('qc_rise', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Receiveing the user's input
    print("Let's move your robot")
    speed = 1
    altitude = input("Type your distance:")
    isRise = input("Rise?: ")#True or False

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    if(isRise):
        vel_msg.linear.z = abs(speed)
    else:
        vel_msg.linear.z = -abs(speed)
    #Since we are moving just in the z-axis
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_altitude = 0

        #Loop to move the turtle in an specified altitude
        while(current_altitude < altitude):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_altitude= speed*(t1-t0)
        #After the loop, stops the robot
        vel_msg.linear.z = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)

        #Loop to move the turtle in an specified altitude
        while (current_altitude > altitude):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_altitude= speed*(t1-t0)
        #After the loop, stops the robot
        vel_msg.linear.z = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)
'''

#        try:
        #Testing our function
#    x = ardrone()
#    x.move2goal()
'''
#    except rospy.ROSInterruptException: pass
   p1 = Process(target = takeoff)
   p1.start()
   p2 = Process(target = ardrone)
   x.move2goal
   p2.start()
#   p3 = Process(target = move2goal)
#   p3 = start()
   time.sleep(120)
   p3 = Process(target = land)
   p3.start()
'''




'''
import sys
from Navdata import navdata_info
from ardrone_autonomy.msg import Navdata, navdata_altitude
from Navdata import navdata_info

class Mode(object):
    def __init__(self, node_name):
        # Initialize the node and rate
        self.node = rospy.init_node(node_name)

        # Subscribers
        # self.sub_navdata = rospy.Subscriber('/ardrone/navdata', \
        #                                      Navdata, self.navdata_cb)
        self.sub_state = rospy.Subscriber('/smach/state', \
                                       String, self.state_cb)

        self.sub_altitude = rospy.Subscriber('/ardrone/navdata_altitude', \
                                       navdata_altitude, self.altitude_cb)

        self.sub_pwm = rospy.Subscriber('/ardrone/navdata', \
                                       Navdata, self.pwm_cb)

        self.sub_tag = rospy.Subscriber('/ardrone/navdata', \
                                       Navdata, self.has_tag_cb)

        # Initialize member variables
        self.transition = String()
        self.state = 'nada'
        self.mode = 0
        self.roll = 0
        self.pitch = 0
        self.altitude = 0
        self.pwm = 0

        self.tag_acquired = False

    def navdata_cb(self, msg):
        """
        Retrieves necessary information about the QC from the /ardrone/navdata
        topic.
        """
        # Mode of the QC, NOT the state of the state machine
        self.mode = msg.state
        self.roll = math.radians(data.rotY)
        self.pitch = math.radians(data.rotX)
        if data.tags_count > 0:
            self.theta = self.navdata.tags_orientation[0]
            # These are actually switched for the controller purposes
            self.tag_x = self.navdata.tags_yc[0]
            self.tag_y = self.navdata.tags_xc[0]

    def pwm_cb(self, msg):
        self.pwm = msg.motor1
        # # faking data, change this to get real data
        # self.pwm = 1

    def altitude_cb(self, msg):
        self.altitude = msg.altitude_raw/1000.0

class Takeoff(Mode):
                       # m/s  mm		        seconds
    def __init__(self, speed, max_altitude, tag_timeout):
        # Initialize the node which is inherited from the Mode super class
        super(self.__class__, self).__init__('takeoff_mode')

        # Subscribers
        # self.sub_state = rospy.Subscriber('/smach/state', \
                                            #  String, self.handle_timer_cb)

        # Publishers
        self.pub_altitude = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.pub_takeoff = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=1000)

        # Initialize member variables
        # self.timer = rospy.Timer(rospy.Duration(tag_timeout), self.goto_reacquisition)

        self.altitude_command = Twist()
        self.altitude_command.linear.z = speed

        self.max_altitude = max_altitude
        self.speed = speed
        self.state = 'nada'

    def navdata_cb(self, msg):
        # Mode of the QC, NOT the state of the state machine
        self.mode = msg.state
        if(msg.tags_count > 0):
            self.tag_acquired = True
            # If we do have the tag we need to stop the timer
            self.turn_off_timer(self.timer, 'Takeoff')
        else:
            self.tag_acquired = False
            # If we don't have the tag we need to start the timer
            self.turn_on_timer(self.timer, 'Takeoff')


    def launch(self):
        self.pub_takeoff.publish(Empty())
        rospy.loginfo("Moving on up!")

    # If we're above the max altitude don't increase the altitude,
    # otherwise go up!
    def change_altitude(self):
        self.pub_altitude.publish(self.altitude_command)
        rospy.loginfo("Change altitude")


# TODO only works when altitude_goal is 3.0 m or lower, need to fix
def main():
    speed = 0.75	 # m/s
    altitude_goal = 2.5 # meters
    tag_timeout = 10 # seconds
    takeoff = Takeoff(speed, altitude_goal, tag_timeout)
    rate = rospy.Rate(200) # 100Hz

    # To let us know that the mode is working
    rospy.loginfo("Started Takeoff Mode")

    while((takeoff.state != 'takeoff')):
        # print takeoff.state
        rate.sleep()

    # To get this guy to take off! For some reason just calling this function
    # once does not work. This value (50) was determined experimentally
    i = 0
    while i < 50:
        takeoff.launch()
        i += 1
        rate.sleep()

    while not rospy.is_shutdown():
        # We only want to execute these manuevers if we're in takeoff mode
        if takeoff.state == 'takeoff':
            if(takeoff.altitude < altitude_goal):
                rospy.loginfo("Go up!")
                takeoff.change_altitude()
            elif(takeoff.altitude >= altitude_goal):
                speed = 0
                rospy.loginfo("Stop!")
                # takeoff.change_altitude(speed)
                # To change states, we publish the fact that we've
                # reached our takeoff altitude
                # Let's change the launch file and then we can
                # break
                # out from the loop
        # else:
        #     continue
        rate.sleep()


if __name__=='__main__':
    main()
'''


'''
#Code used to land QC
def land():
    pub = rospy.Publisher("ardrone/land", Empty, queue_size=10 )
    rospy.init_node('land', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()

if __name__ == '__main__':
    try:
        land()
    except rospy.ROSInterruptException:
        pass

#Code used to land QC
def forward():
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=10 )
    rospy.init_node('forward', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()

if __name__ == '__main__':
    try:
        forward()
    except rospy.ROSInterruptException:
        pass

# time.sleep(5) #delays for 20 seconds
#   try:
#       takeoff()
#       break
#       land()
#   except rospy.ROSInterruptException:
#       pass
# print("chicken")


#Trash Code
def forward():
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=10 )
    rospy.init_node('forward', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()

'''
