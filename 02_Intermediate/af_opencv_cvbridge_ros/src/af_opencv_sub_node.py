#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys
import numpy as np
import time

bridge = CvBridge()

def image_callback(ros_image):
    print('got an image')
    global bridge

    try:
        cv_image = bridge.imgmsg_to_cv2(ros_image,"bgr8")
    except CvBridgeError as e:
        print(e)
    
    detect_ball_in_a_frame(cv_image)
    cv2.waitKey(3)

def filter_color(rgb_image, lower_bound_color, upper_bound_color):
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv image", hsv_image)

    mask = cv2.inRange(hsv_image, lower_bound_color, upper_bound_color)
    return mask

def getContours(binary_image):
    _, contours, hierarchy = cv2.findContours(binary_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def draw_ball_contours(binary_image, rgb_image, contours):
    black_image = np.zeros([binary_image.shape[0], binary_image.shape[1],3], 'uint8')

    for c in contours:
        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, True)
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        if area>3000:
            cv2.drawContours(rgb_image, [c], -1, (150, 250, 150), 1)
            cv2.drawContours(black_image, [c], -1, (150, 250, 150), 1)
            cx, cy = get_contour_center(c)
            cv2.circle(rgb_image, (cx,cy), (int)(radius), (0,0,255), 1)
            cv2.circle(black_image, (cx,cy), (int)(radius), (0,0,255), 1)
            cv2.circle(black_image, (cx,cy), 5, (150,150,255), -1)
        cv2.imshow("RGB Image Contours", rgb_image)
        cv2.imshow("Black Image Contours", black_image)

def get_contour_center(contour):
    M = cv2.moments(contour)
    cx = -1
    cy = -1
    if (M['m00'] != 0):
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
    return cx, cy

def detect_ball_in_a_frame(image_frame):
    yellowLower = (30, 100, 50)
    yellowUpper = (60, 255, 255)
    rgb_image = image_frame
    binary_image_mask = filter_color(rgb_image, yellowLower, yellowUpper)
    contours = getContours(binary_image_mask)
    draw_ball_contours(binary_image_mask, rgb_image, contours)

def main(args):
    rospy.init_node('ball_listener', anonymous=True)
    
    #for turtlebot3 waffle
    #image_topic="/camera/rgb/image_raw/compressed"
    
    #for usb cam
    #image_topic="/usb_cam/image_raw"

    image_sub = rospy.Subscriber("/ball_image", Image, image_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main(sys.argv)