#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I Heard %s", data.data)

def listener():
    rospy.init_node('lisneter', anonymous=True)         # listener adalah nama node nya
    rospy.Subscriber('chatter', String, callback)       # chatter adalah topic
    rospy.spin()

if __name__ == '__main__':
    listener()
