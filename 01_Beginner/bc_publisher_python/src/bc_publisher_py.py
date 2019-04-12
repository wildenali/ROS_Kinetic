#!/usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('bb_publisher_py_node')

    pub = rospy.Publisher("/bb_pub_py", String, queue_size=10)   # queue_size untuk buffer, kalau misalnya data yg dikirim banyaaaaaak banget, dan si subscriber tidak bisa membaca semua, maka perlu queue_size

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = String()
        msg.data = "hiii, ini dari publisher"
        pub.publish(msg)
        rate.sleep()

    rospy.loginfo("Node dihentikan")
