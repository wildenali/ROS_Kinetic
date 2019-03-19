#!/usr/bin/env python

import sys
import rospy

from ai_service_client_server_python.srv import AddTwoInts
from ai_service_client_server_python.srv import AddTwoIntsRequest
from ai_service_client_server_python.srv import AddTwoIntsResponse

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        respon1 = add_two_ints(x, y)
        return respon1.sum

    except rospy.ServiceException, e:
        print "Service GAGAL di panggil: %s" %e

def usage():
    return "%s [x y]" %sys.argv[0]


if __name__ == '__main__':
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)

    print "Rekues in %s + %s" %(x,y)
    print "%s + %s = %s"%(x, y, add_two_ints_client(x, y))
