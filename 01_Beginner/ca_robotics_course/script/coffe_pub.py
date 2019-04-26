#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publishing():
    pub = rospy.Publisher('ingredients', String, queue_size=10)
    rospy.init_node('Coffe_ingredients', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        data = "gula,susu,kopi"
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    publishing()
