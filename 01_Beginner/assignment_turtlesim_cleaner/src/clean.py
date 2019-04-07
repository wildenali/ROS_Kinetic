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

def poseCallback(pose_message):
    global x, y, z, yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta

def move(speed, distance, isforward):
    velocity_message = Twist()
    global x, y
    print("move bro", distance)
    x0 = x
    y0 = y

    if isforward:
        velocity_message.linear.x = abs(speed)
    else:
        velocity_message.linear.x = -abs(speed)

    distance_moved = 0.0
    loop_rate = rospy.Rate(100)

    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    while True:
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()

        distance_moved = abs(math.sqrt(((x-x0) ** 2) + ((y-y0) ** 2)))

        if not (distance_moved <= distance):
            rospy.loginfo("reached")
            break
    
    velocity_message.linear.x = 0
    velocity_publisher.publish(velocity_message)

def rotate(angular_speed, angle, clockwise):    # angle in radians
    global yaw
    velocity_message = Twist()
    velocity_message.linear.x = 0
    velocity_message.linear.y = 0
    velocity_message.linear.z = 0
    velocity_message.angular.x = 0
    velocity_message.angular.y = 0
    velocity_message.angular.z = 0

    theta0 = yaw
    angular_speed_rad = math.radians(angular_speed)

    if clockwise:
        velocity_message.angular.z = -abs(angular_speed_rad)
    else:
        velocity_message.angular.z = abs(angular_speed_rad)
    
    angle_rotated = 0.0
    loop_rate = rospy.Rate(10000)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    t0 = rospy.Time.now().to_sec()

    while True:
        velocity_publisher.publish(velocity_message)
        t1 = rospy.Time.now().to_sec()
        current_ang_deg = (t1-t0)*angular_speed
        loop_rate.sleep()
        if (current_ang_deg > angle):
            print("\n angle", angle)
            rospy.loginfo("reached")
            break
    
    velocity_message.angular.z = 0
    velocity_publisher.publish(velocity_message)

def go_to_goal(x_goal, y_goal):
    global x, y, yaw
    print(x_goal, y_goal)

    velocity_message = Twist()
    dist = abs(math.sqrt( (y_goal-y)**2 + (x_goal-x)**2 ))
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)

    while dist>0.01:
        konstata_linear = 0.5
        dist = abs(math.sqrt( (y_goal-y)**2 + (x_goal-x)**2 ))
        linear_speed = dist * konstata_linear

        konstata_angular = 4
        d_angle = math.atan2(y_goal-y, x_goal-x)

        ang_speed = (d_angle-yaw) * konstata_angular

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = ang_speed

        velocity_publisher.publish(velocity_message)


def setDesiredOrientation(desired_angle_deg):
    global yaw
    if yaw<0:
        yaw_corrected = 2*math.pi+yaw
    else:
        yaw_corrected = yaw
    
    desired_angle_radians = math.radians(desired_angle_deg)

    rel_angle_rad = desired_angle_radians - yaw_corrected

    rel_angle_deg = math.degrees(rel_angle_rad)

    if rel_angle_deg < 0:
        clockwise = True
        rel_angle_deg = abs(rel_angle_deg)
        if rel_angle_deg > (360 - rel_angle_deg):
            clockwise = False
            rel_angle_deg = 360 - rel_angle_deg
    else:
        clockwise = False
        if rel_angle_deg > (360 - rel_angle_deg):
            clockwise = True
            rel_angle_deg = 360 - rel_angle_deg
    
    angle_speed_deg = 60
    rotate(angle_speed_deg, rel_angle_deg, clockwise)

def grid_cleaning():
    global yaw
    go_to_goal(1,1)
    setDesiredOrientation(0)
    move(1,9,True)
    setDesiredOrientation(90)
    flip = -1
    print("\n\n")
    
    c = 9
    d = [1,9]
    while c>0:
        print("here")
        if flip == -1:
            ang = [-90, 180]
            print("set 1")
        else:
            print("set 2")
            ang = [90, 180]

        move(1, d[1], True)
        setDesiredOrientation(ang[1])   # turn to 10, 10

        move(1, d[0], True)
        setDesiredOrientation(ang[0])   # turn to 9, 10
        flip = flip * -1
        print("\n\n")
        c = c - 1
    
def spiral_cleaning():
    global x, y
    velocoty_message = Twist()
    velocoty_message.linear.x = 0.5
    velocoty_message.linear.y = 0
    velocoty_message.linear.z = 0
    velocoty_message.angular.x = 0
    velocoty_message.angular.y = 0
    velocoty_message.angular.z = 1
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
    loop_rate = rospy.Rate(100)

    while True:
        velocity_publisher.publish(velocoty_message)
        loop_rate.sleep()
        print(x,y)
        if x < 0.5 or y < 0.5 or x > 10.5 or y > 10.5:
            break
        
        velocoty_message.linear.x = velocoty_message.linear.x+0.001
    
    velocoty_message.linear.x=0
    velocity_publisher.publish(velocoty_message)

if __name__ == "__main__":
    try:
        run = 0
        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        velocity_publisher = rospy.Publisher('/turle1/cmd_vel', Twist, queue_size=10)
        pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, poseCallback)

        time.sleep(2)
        choice = raw_input("selec cleaning method \n1. Grid cleaning\n2. Spiral cleaning\nEnter your choice (1 or 2):")
        try:
            test_choice = int(choice)
            if test_choice == 1:
                run = 1
                grid_cleaning()
            
            if test_choice == 2:
                run = 1
                spiral_cleaning()
            
            if run == 0:
                print("Invalid choice, terminating code")
            
        except ValueError:
            print("Invalid choice, terminating code")
        



    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated")
