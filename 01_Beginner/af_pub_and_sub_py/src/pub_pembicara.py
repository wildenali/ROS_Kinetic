#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def si_pembicara():
    pub = rospy.Publisher('obrolan', String, queue_size = 10)
    rospy.init_node('ini_pembicara', anonymous=True)         # usahakan buat nama si remapping nya sesuai dengan nama file nya, karena supaya mudah memanggilnya, contoh rospy.init_node('pub_pembicara', anonymous=True)
    rate = rospy.Rate(10)   # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello ini python %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        si_pembicara()
    except rospy.ROSInterruptException:
        pass
