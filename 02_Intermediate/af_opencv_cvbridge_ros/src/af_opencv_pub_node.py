#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys
import time


def main(args):
    rospy.init_node('ball_publisher', anonymous=True)
    bridge = CvBridge()

    # for turtlebot3 waffle
    # image_topic = "/camera/rgb/image_raw/compressed"

    # for usb cam
    image_topic = "/usb_cam/image_raw"
    image_pub = rospy.Publisher("ball_image", Image, queue_size=10)

    video_capture = cv2.VideoCapture(0)
    # video_capture = cv2.VideoCapture('video/ping_pong.mp4')

    rate = rospy.Rate(10)
    while True:
        ret, frame = video_capture.read()
        try:
            ros_image = bridge.cv2_to_imgmsg(frame, "bgr8")
        except CvBridgeError as e:
            print(e)
        image_pub.publish(ros_image)
        rate.sleep()

if __name__ == "__main__":
    main(sys.argv)
