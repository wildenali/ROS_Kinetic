#!/usr/bin/env python

import sys
import rospy

from ar_ros_service_assignment.srv import RectangleAreaService
from ar_ros_service_assignment.srv import RectangleAreaServiceRequest
from ar_ros_service_assignment.srv import RectangleAreaServiceResponse

# ar_ros_service_assignment/RectangleAreaService

def request_rectangle_area(x, y):
    rospy.wait_for_service('rectangle_server')
    try:
        add_two_ints = rospy.ServiceProxy('rectangle_server', RectangleAreaService)
        server_response = add_two_ints(x, y)
        return server_response.area
    except rospy.ServiceException, e:
        print "Panggil service gagal: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Request width %s and height %s"%(x, y)
    print "rectangle of width %s and height %s = %s"%(x, y, request_rectangle_area(x, y))
