#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    print(data.data)

def subscribing():
    rospy.init_node('Serving_coffe', anonymous=True)
    rospy.Subscriber('Your_Coffe', String, callback)
    rospy.spin()

if __name__ == '__main__':
    subscribing()
