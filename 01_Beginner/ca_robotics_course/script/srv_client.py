#!/usr/bin/env python

import sys
import rospy
from ca_robotics_course.srv import *
from geometry_msgs.msg import Twist

def concate_name_client(x, y):
    rospy.wait_for_service('Name_confirmation')
    concat_name = rospy.ServiceProxy('Name_confirmation', baru)
    resp1 = concat_name(x, y)
    return resp1

def usage():
    return "%s [x y]" %sys.argv[0]

def security_verifying():
    # pub = rospy.Publisher('/turtle1/cmd_vel', Twist)          # ini pakai turtlesim
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)     # ini pakai turtlebot3
    rospy.sleep(1)
    r = rospy.Rate(5)
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 0.3
        for i in range(10):
            pub.publish(twist)
            r.sleep()

        twist = Twist()
        twist.angular.z = 0.85
        for i in range(10):
            pub.publish(twist)
            r.sleep()

if __name__ == '__main__':
    rospy.init_node("mover_after_security")
    if len(sys.argv) == 3:
        x = sys.argv[1]
        y = sys.argv[2]
    else:
        print(usage())
        sys.exit(1)
    print("%s + %s = %s" %(x, y, concate_name_client(x, y)))
    result = concate_name_client(x, y)
    if result.fullname == "WildenAli":
        security_verifying()
    else:
        print("Salah orang lu")
