#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback_penerima(data):
    rospy.loginfo(rospy.get_caller_id() + "I mendengar %s", data.data)

def si_pendengar():
    rospy.init_node('ini_penerima', anonymous=True)     # usahakan buat nama si remapping nya sesuai dengan nama file nya, karena supaya mudah memanggilnya, contoh rospy.init_node('sub_penerima', anonymous=True)
    rospy.Subscriber("obrolan", String, callback_penerima)

    rospy.spin()

if __name__ == "__main__":
    si_pendengar()
