#1 /usr/bin/env python

# Import transitions library
from transitions import Machine

# ROS imports
import rospy
from std_msgs.msg import String
from eagle_one_test.srv import State

class Smach(Machine):
    def __init__(self):
        # Define the different states of the machine
        states = ['secure', 'takeoff', 'follow', 'take_picture', \
                  'land', 'reacquisition', 'emergency']

        # Define the transitions between states
        # FORMAT: ['trigger_event', 'source_state', 'destination_state']
        transitions = [
            ['takeoff_command', 'secure', 'takeoff'],
            ['takeoff_alt_reached', 'takeoff', 'follow'],
            ['picture_command', 'follow', 'take_picture'],
            ['picture_taken', 'take_picture', 'land'],
            ['land_alt_reached', 'land', 'secure'],
            ['emergency_condition', ['takeoff', 'follow', 'take_picture', 'land'], 'emergency'],
            ['takeoff_tag_lost', 'takeoff', 'reacquisition'],
            ['follow_tag_lost', 'follow', 'reacquisition'],
            ['land_tag_lost', 'land', 'reacquisition'],
            ['take_picture_tag_lost', 'take_picture', 'reacquisition'],
            ['takeoff_tag_found', 'reacquisition', 'takeoff'],
            ['follow_tag_found', 'reacquisition', 'follow'],
            ['land_tag_found', 'reacquisition', 'land'],
            ['take_picture_tag_found', 'reacquisition', 'take_picture'],
            ['timed_out', 'reacquisition', 'emergency'],
            ['reset', 'emergency', 'secure']
        ]

        Machine.__init__(self, states=states, transitions=transitions, \
                         initial='secure')

    def handle_state_change(self, req):
        self.change_state(req.transition)
        return self.state

    def state_change_server(self):
        rospy.init_node('qc_smach_server')
        s = rospy.Service('qc_smach', State, self.handle_state_change)
        rospy.spin()

    def change_state(self, transition):
        if((self.is_secure()) and (transition == 'TAKEOFF_COMMAND')):
            self.takeoff_command()
        elif(self.is_takeoff()):
            if(transition == 'TAKEOFF_ALT_REACHED'):
                self.takeoff_alt_reached()
                print("Altitude Goal Reached")
            if(transition == 'TAKEOFF_TAG_LOST'):
                self.takeoff_tag_lost()
                print("Tag lost during takeoff")
            if(transition == 'EMERGENCY_CONDITION'):
                self.emergency_condition()
                print("Emergency During Takeoff")
        elif(self.is_follow()):
            if(transition == 'PICTURE_COMMAND'):
                self.picture_command()
                print("Set to Take Picture")
            if(transition == 'FOLLOW_TAG_LOST'):
                self.follow_tag_lost()
                print("Tag lost during follow")
            if(transition == 'EMERGENCY_CONDITION'):
                self.emergency_condition()
                print("Emergency During Follow")
        elif(self.is_take_picture()):
            if(transition == 'PICTURE_TAKEN'):
                self.picture_taken()
                print("Picture Saved")
            if(transition == "EMERGENCY_CONDITION"):
                self.emergency_condition()
                print("Emergency During Picture Attempt")
        #this can be taken out, transition from taking picture to reacquisition if tag is lost
        #during picture taking
            if(transition == "TAKE_PICTURE_TAG_LOST"):
                self.take_picture_tag_lost()
                print("Tag Lost After Picture Taking")
        elif(self.is_land()):
            if(transition == 'LAND_ALT_REACHED'):
                self.land_alt_reached()
                print("Prepare to Land")
            if(transition == 'LAND_TAG_LOST'):
                print("Tag lost during landing")
                self.land_tag_lost()
            if(transition == 'EMERGENCY_CONDITION'):
                self.emergency_condition()
                print("Emergency During Landing")
        elif((self.is_emergency()) and (transition == 'RESET')):
            print("Return to secure mode")
            self.reset()
        elif(self.is_reacquisition()):
            if(transition == 'TAKEOFF_TAG_FOUND'):
                self.takeoff_tag_found()
                print("Tag Found, Returning to Takeoff mode")
            if(transition == 'FOLLOW_TAG_FOUND'):
                self.follow_tag_found()
                print("Tag Found, Returning to Follow Mode")
            if(transition == 'LAND_TAG_FOUND'):
                self.land_tag_found()
                print("Tag Found, Returning to Land Mode")
            if(transition == 'TAKE_PICTURE_TAG_FOUND'):
                self.take_picture_tag_found()
                print("Tag Found, Returning to Take Picture Mode")
            if(transition == 'TIMED_OUT'):
                self.timed_out()
                print("Reacquisition Timer Expired, Entering Emergency Mode")
