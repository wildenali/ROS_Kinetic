#!/usr/bin/env python

import rospy
# from bi_service_server_python.srv import AddTwoInts
from rospy_tutorials.srv import AddTwoInts                  # ini adalah contoh service bawaan si ros

def handle_add_two_ints(req):
    result = req.a + req.b
    rospy.loginfo("Penjumlahan dari "+ str(req.a) + " dan " + str(req.b) + " adalah " + str(result))
    return result

if __name__ == '__main__':
    rospy.init_node("add_two_ints_server")
    rospy.loginfo("Add two ints server node created")

    service = rospy.Service("/add_two_ints", AddTwoInts, handle_add_two_ints)
    rospy.loginfo("Service server has been started")

    rospy.spin()
