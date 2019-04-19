#!/usr/bin/env python

import rospy
import actionlib
from std_msgs.msg import Empty
from ba_my_robot_msgs.msg import MoveRobotAction
from ba_my_robot_msgs.msg import MoveRobotGoal

class MoveRobotClient:

    def __init__(self):
        self._ac = actionlib.SimpleActionClient('/move_robot', MoveRobotAction)
        self._ac.wait_for_server()
        rospy.loginfo("Server is up, let's send a goal")

        self.sub = rospy.Subscriber('/cancel_move', Empty, self.cancel_move_callback)

    def cancel_move_callback(self, req):
        rospy.loginfo("Received message to cancel goal")
        self._ac.cancel_goal()

    def send_goal(self):
        goal = MoveRobotGoal()
        goal.position = 1             # coba angka berapa aja 27, 3, 5, dll
        goal.velocity = 2             # coba angka berapa aja 27, 3, 5, dll
        self._ac.send_goal(goal, done_cb=self.done_callback, feedback_cb=self.feedback_callback)
        rospy.loginfo("Goal has been sent")

        # ini buat nyoba nge test aja sebelum ke cancel_goal
        # rospy.sleep(5)
        # self._ac.cancel_goal()

    def done_callback(self, status, result):
        rospy.loginfo("Status: " + str(status))
        rospy.loginfo("Result: " + str(result))

    def feedback_callback(self, feedback):
        rospy.loginfo(feedback)

if __name__ == '__main__':
    rospy.init_node('move_robot_client')

    client = MoveRobotClient()
    client.send_goal()

    rospy.spin()
