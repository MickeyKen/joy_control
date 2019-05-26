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
        self.cmd_pub.publish(self.cmd_msg)

    def pan_make(self, p):
        self.pan_msg = p
        self.pan_pub.publish(self.pan_msg)

    def tilt_make(self, t):
        self.tilt_msg = t
        self.tilt_pub.publish(self.tilt_msg)

class Subscribe(Publishsers):
    def __init__(self):

        self.cmd_msg = Twist()
        self.pan_msg = Float64()
        self.tilt_msg = Float64()

        self.pantilt_lock = 0

        self.cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 10)
        self.pan_pub = rospy.Publisher("/pan_controller/command", Float64, queue_size = 10)
        self.tilt_pub = rospy.Publisher("/tilt_controller/command", Float64, queue_size = 10)

        self.ptm_sub = rospy.Subscriber('joy', Joy, self.callback)


    def callback(self, msg):
        angular = 0.0

        if msg.buttons[8] == 1.0:
            self.cmd_make(0.0, 0.0, 0.0)

        ### /cmd_vel ###
        if msg.axes[2] < 0.0 and msg.axes[5] < 0.0:
            angular = abs(msg.axes[2]) - msg.axes[5]
            self.cmd_make(-msg.axes[0], msg.axes[1], -angular / 2.0)

        elif msg.axes[2] < 0.0 and msg.axes[5] >= 0.0:
            self.cmd_make(-msg.axes[0], msg.axes[1], abs(msg.axes[2]) / 2.0)
        elif msg.axes[5] < 0.0 and msg.axes[2] >= 0.0:
            self.cmd_make(-msg.axes[0], msg.axes[1], msg.axes[5] / 2.0)
        else:
            self.cmd_make(-msg.axes[0], msg.axes[1], 0.0)


        if msg.buttons[4] == 1.0:
            self.pantilt_lock = 1
        if msg.buttons[5] == 1.0:
            self.pantilt_lock = 0

        if self.pantilt_lock == 0:
	    ### /pan /tilt ###
	    self.pan_make(msg.axes[3])
	    self.tilt_make(-msg.axes[4])

        if msg.buttons[2] == 1.0:
            rospy.set_param("projector/switch", 1)
        else:
            rospy.set_param("projector/switch", 0)






if __name__ == '__main__':
    rospy.init_node('joy_control_frame')

    Subscribe = Subscribe()

    rospy.spin()
