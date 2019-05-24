#!/usr/bin/python

import rospy
from sensor_msgs.msg import Joy


def callback(msg):
    #rospy.loginfo("I heard: message = [%s], count = [%d]" % (msg.message, msg.count));
    print msg
    print "=============="
    print msg.axes
    print msg.buttons


def subscriber():

    rospy.init_node('sample_py_subscriber', anonymous=True)
    rospy.Subscriber('joy', Joy, callback)

    rospy.spin()

if __name__ == '__main__':
    subscriber()
