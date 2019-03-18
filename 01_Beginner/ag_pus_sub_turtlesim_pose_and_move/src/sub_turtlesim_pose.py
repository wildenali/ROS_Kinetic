#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose

def posisiCallback(posisi_message):
    print "posisi si kura-kura:"
    print ('x = {}'.format(posisi_message.x))           # cara penulisan dengan python3
    print ('y = %f' % posisi_message.y)                 # cara penulisan dengan python2
    print ('theta = {}'.format(posisi_message.theta))   # cara penulisan dengan python3

    if posisi_message.theta < 0:
        print "muter kiri terus"

if __name__ == '__main__':
    try:
        rospy.init_node('sub_turtlesim_pose', anonymous=True)
        posisi_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(posisi_topic, Pose, posisiCallback)
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
