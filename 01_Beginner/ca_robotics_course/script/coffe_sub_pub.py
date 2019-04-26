#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def callback(data):
    data=data.data + " cup a cup"
    pub=rospy.Publisher('Your_Coffe', String, queue_size=10)
    pub.publish(data)

def subscribing():
    rospy.init_node('Preparing_hot_coffe', anonymous=True)         # listener adalah nama node nya
    rospy.Subscriber('ingredients', String, callback)       # chatter adalah topic
    rospy.spin()

if __name__ == '__main__':
    subscribing()
