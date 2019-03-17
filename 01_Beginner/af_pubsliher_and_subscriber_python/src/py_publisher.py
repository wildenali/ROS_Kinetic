#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    # membuat publisher baru, dengan spesifik nama 'py_gosip', dan queue_size = 10
    pub = rospy.Publisher('py_gosip', String, queue_size = 10)

    # inisialisasi node dulu dengan nama 'py_publisher'
    rospy.init_node('py_publisher', anonymous = True)

    # set the loop rate
    rate = rospy.Rate(1)    # 10 Hz

    i = 0
    while not rospy.is_shutdown():
        # hello_str = "hey world kamu %s" % rospy.get_time()
        # atau
        hello_str = "hey world kamu %s" % i
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        i += 1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
