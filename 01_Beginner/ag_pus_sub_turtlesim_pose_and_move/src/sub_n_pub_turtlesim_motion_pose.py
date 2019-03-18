#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

x = 0
y = 0
z = 0
yaw = 0

def posisiCallback(posisi_message):
    global x
    global y, z, yaw
    x = posisi_message.x
    y = posisi_message.y
    yaw = posisi_message.theta

def move(kecepatan, jarak):
    # deklarasi pesan Twist untuk ngirim perintah kecepatan
    kecepatan_message = Twist()

    # get current lokasi
    x0 = x
    y0 = y
    # z0 = z
    # yaw0 = yaw
    kecepatan_message.linear.x = kecepatan
    jarak_pergerakan = 0.0
    loop_rate = rospy.Rate(10)      # 10Hz (10 kali perdetik)
    cmd_vel_topic = '/cmd_vel'
    kecepatan_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

    while True:
        rospy.loginfo("Turtlesim moves forwards")
        kecepatan_publisher.publish(kecepatan_message)

        loop_rate.sleep()

        jarak_pergerakan = jarak_pergerakan + abs(0.5 * math.sqrt(((x-x0) ** 2) + ((y-y0)**2)))
        print jarak_pergerakan
        if not(jarak_pergerakan < jarak):
            rospy.loginfo("sampai")
            break

    # ini perintah supaya ketika sudah sampai, robot berhenti
    kecepatan_message.linear.x = 3
    kecepatan_publisher.publish(kecepatan_message)
    time.sleep(2)

if __name__ == '__main__':
    try:
        rospy.init_node('sub_n_pub_turtlesim_motion_pose', anonymous=True)

        # deklarasi publisher kecepatan
        cmd_vel_topic = '/cmd_vel'
        kecepatan_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        posisi_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(posisi_topic, Pose, posisiCallback)
        time.sleep(2)
        print 'gerak:'
        move(1.0, 50.0)
        time.sleep(2)
        print 'start reset: '
        rospy.wait_for_service('reset')
        reset_turtle = rospy.ServiceProxy('reset', Empty)
        reset_turtle()
        print 'end reset:'
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated")
