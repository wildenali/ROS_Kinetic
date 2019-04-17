#!/usr/bin/env python

import rospy
import actionlib
from ba_my_robot_msgs.msg import CountUntilAction
from ba_my_robot_msgs.msg import CountUntilGoal


class CountUntilClient:
    def __init__(self):
        self._ac = actionlib.SimpleActionClient('/count_until', CountUntilAction)
        self._ac.wait_for_server()
        rospy.loginfo("Action serves is up,we can send new goals!")

    def send_goal_and_get_result(self):
        goal = CountUntilGoal(max_number=6, wait_duration=1.2)     # max_number=7 ,, untuk coba coba ubah aja angkanya

        # ====== yg ini masih syncronous ======
        # self._ac.send_goal(goal)
        # ====== yg ini masih syncronous ======

        # self._ac.send_goal(goal, done_cb=self.done_callback)
        self._ac.send_goal(goal, done_cb=self.done_callback, feedback_cb=self.feedback_callback)
        rospy.loginfo("Goal has been sent.")

        # ====== yg ini masih syncronous ======
        # self._ac.wait_for_result()                 # self._ac -> action clien (_ac)
        # success = self._ac.wait_for_result(rospy.Duration(3.0))                 # self._ac -> action clien (_ac)
        # if not success:
        #     rospy.logwarn("TIMEOUT")
        # rospy.loginfo(self._ac.get_result())
        # ====== yg ini masih syncronous ======


        # ========== Cancel Goal ==========
        rospy.sleep(2)
        self._ac.cancel_goal()



    # ====== cara supaya ada callback dari server =======
    def done_callback(self, status, result):
        rospy.loginfo("Status is : " + str(status))     # nanti ini hasil hasilnya status is : 3 misalnya, angka 3 itu dari mana, dari sini     http://docs.ros.org/kinetic/api/actionlib_msgs/html/msg/GoalStatus.html
        rospy.loginfo("Result is : " + str(result))


    # feedback persentase dari si server
    def feedback_callback(self, feedback):
        rospy.loginfo(feedback)




if __name__ == '__main__':
    rospy.init_node('count_until_client')

    client = CountUntilClient()

    client.send_goal_and_get_result()

    # tambah ini untuk asyncronous
    rospy.spin()
