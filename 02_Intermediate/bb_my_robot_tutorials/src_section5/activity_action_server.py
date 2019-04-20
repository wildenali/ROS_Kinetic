#!/usr/bin/env python

import threading
import rospy
import actionlib

from ba_my_robot_msgs.msg import CountUntilAction
from ba_my_robot_msgs.msg import CountUntilGoal
from ba_my_robot_msgs.msg import CountUntilResult
from ba_my_robot_msgs.msg import CountUntilFeedback


class CountUntilServer:

    def __init__(self):
        self._as = actionlib.ActionServer('/count_until', CountUntilAction, self.on_goal, self.on_cancel, auto_start=False)
        self._as.start()
        rospy.loginfo("Action Server has been started.")
        self._cancel_request = False

    def process_goal(self, goal_handle):
        rospy.loginfo("Processing goal")
        goal = goal_handle.get_goal()
        max_number = goal.max_number
        wait_duration = goal.wait_duration

        # rospy.sleep(1)
        # goal_handle.set_succeeded()

        # Validate parameters
        if max_number > 6:      # 6 ini tergantung si count_until_client.py, cek dulu berapa maksimal nilainya
            goal_handle.set_rejected()
            return
        goal_handle.set_accepted()

        counter = 0
        rate = rospy.Rate(1.0/wait_duration)

        success = False
        preempted = False

        while not rospy.is_shutdown():
            counter +=  1
            rospy.loginfo(counter)
            #todo cancel
            if self._cancel_request:
                self._cancel_request = False
                preempted = True
                break
            if counter >= max_number:
                success = True
                break
            feedback = CountUntilFeedback()
            feedback.percentage = float(counter) / float(max_number)
            goal_handle.publish_feedback(feedback)
            rate.sleep()

        result = CountUntilResult()
        result.count = counter
        rospy.loginfo("Send result to client")

        if preempted:
            rospy.loginfo("Preempted")
            goal_handle.set_canceled(result)
        elif success:
            rospy.loginfo("Succeeded")
            goal_handle.set_succeeded(result)
        else:
            rospy.loginfo("Aborted")
            goal_handle.set_aborted(result)
        rospy.loginfo("--- Finished to process the goal")


    def on_goal(self, goal_handle):
        rospy.loginfo("Received new goal")
        rospy.loginfo(goal_handle.get_goal())

        w = threading.Thread(name="worker", target=self.process_goal, args=(goal_handle,))
        w.start()
        # self.process_goal(goal_handle)

    def on_cancel(self, goal_handle):
        rospy.loginfo("Received cancel request")
        self._cancel_request = True



if __name__ == '__main__':
    rospy.init_node('count_until_server')

    server = CountUntilServer()

    rospy.spin()
