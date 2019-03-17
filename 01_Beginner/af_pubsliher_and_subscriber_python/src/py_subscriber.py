#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(pesan):
    # get caller id(): Get fully resolve name of local node
    rospy.loginfo(rospy.get_caller_id() + "apa ya... %s", pesan.data)

def listener():
    # in ROS,nodes are uniquely name. If two nodes with the same node are launched
    # the previous one is kicked off.

    # the anonymous=True flag means that rospy will choose a unique name for out 'listener' node
    # so that multiple listener cans can run simultaneously
    rospy.init_node('py_subscriber', anonymous=True)
    rospy.Subscriber("py_gosip", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
