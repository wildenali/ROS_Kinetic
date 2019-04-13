#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64


if __name__ == '__main__':
    rospy.init_node("number_publisher", anonymous=True)     # kalau ada anonymous=True, maka ntar node nya bisa jadi banyak, jadi angka dibelakang node nya
                                                            # jadi misalnya si number_publisher ini di rosrun dua kali di beda terminal, maka tidak akan nge terminate si node yang aktif sebelumnya
                                                            # dengan kata lain, akan ada dua number_publisher_***** dan number_publisher_######, dan kalau nge run banyak, akan banyak juga hasilnya

    pub = rospy.Publisher("/number", Int64, queue_size=10)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        msg = Int64()
        msg.data = 2    # msg.data dari mana, cek nya di  http://docs.ros.org/api/std_msgs/html/msg/Int64.html
        pub.publish(msg)
        rate.sleep()
