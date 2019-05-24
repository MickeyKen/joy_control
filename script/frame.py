#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64


class Publishsers():
    def cmd_make(self, x, y, ang):
        ### make ###
        self.cmd_msg.linear.x = x
        self.cmd_msg.linear.y = y
        self.cmd_msg.angular.z = ang
        ### publish ###
        self.cmd_pub.publish(cmd_msg)
    
    def pt_make(self, pan, tilt):
        self        


class Subscribe(Publishsers):
    def __init__(self):
        
        self.cmd_msg = Twist()
        self.pan_msg = Float64()
        self.tilt_msg = Float64()

        self.cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 10)

        self.ptm_sub = rospy.Subscriber('joy', Joy, self.callback)


    def callback(self, msg):



if __name__ == '__main__':
    rospy.init_node('joy_control_frame')

    Subscribe = Subscribe()

    rospy.spin()
