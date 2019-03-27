#!/usr/bin/env python

from ar_ros_service_assignment.srv import RectangleAreaService
from ar_ros_service_assignment.srv import RectangleAreaServiceRequest
from ar_ros_service_assignment.srv import RectangleAreaServiceResponse

# ar_ros_service_assignment/RectangleAreaService

import rospy

def rectangle_callback(rekues):
    print "Hasilnya adalah: %s * %s = %s" %(rekues.width, rekues.height, (rekues.width * rekues.height))
    return RectangleAreaServiceResponse(rekues.width * rekues.height)

def rectangle_server():
    rospy.init_node('rectangle_server')
    s = rospy.Service('rectangle_server', RectangleAreaService, rectangle_callback)
    print "calculate rectangle"
    rospy.spin()

if __name__ == '__main__':
    rectangle_server()
