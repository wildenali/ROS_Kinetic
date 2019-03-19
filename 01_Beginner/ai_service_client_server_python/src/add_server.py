#!/usr/bin/env python

from ai_service_client_server_python.srv import AddTwoInts
from ai_service_client_server_python.srv import AddTwoIntsRequest
from ai_service_client_server_python.srv import AddTwoIntsResponse

import rospy

def handle_add_two_ints(rekues):
    print "Hasilnya adalah: %s + %s = %s" %(rekues.a, rekues.b, (rekues.a + rekues.b))
    return AddTwoIntsResponse(rekues.a + rekues.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print "Ready to add two ints"
    rospy.spin()

if __name__ == '__main__':
    add_two_ints_server()
