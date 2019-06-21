#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback_terima_dari_bb_pub_py(msg):
    # rospy.loginfo("Message received: ")
    # rospy.loginfo(msg)
    print(msg.data)
    # int_x = int(msg.data)
    # print(int_x)

if __name__ == '__main__':
    rospy.init_node('bb_subscriber_py_node')

    # nge subscriber si /bb_pub_py
    sub = rospy.Subscriber("/bb_pub_py", String, callback_terima_dari_bb_pub_py)   # queue_size untuk buffer, kalau misalnya data yg dikirim banyaaaaaak banget, dan si subscriber tidak bisa membaca semua, maka perlu queue_size

    rospy.spin()
