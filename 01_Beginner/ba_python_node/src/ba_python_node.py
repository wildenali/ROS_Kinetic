#!/usr/bin/env python

import rospy

if __name__ == '__main__':
    rospy.init_node('python_node')
    rospy.loginfo("this node has been started")

    # rospy.sleep(1)
    # rospy.loginfo("Exit now")

    rate = rospy.Rate(10)   # 10 Hertz ->  send message 10 times per seconds

    while not rospy.is_shutdown():
        rospy.loginfo("caw")
        rate.sleep()
