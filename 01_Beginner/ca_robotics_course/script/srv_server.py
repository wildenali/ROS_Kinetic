#!/usr/bin/env python

import rospy
from ca_robotics_course.srv import *

def Concatine_name(req):
    result = req.name1 + req.name2
    return result

def Security_server():
    rospy.init_node('Security')
    s = rospy.Service('Name_confirmation', baru, Concatine_name)
    rospy.spin()

if __name__ == '__main__':
    Security_server()
