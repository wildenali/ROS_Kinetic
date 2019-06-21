#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton

def button_1_Click():
    # form.close()
    msg = String()
    msg.data = "1"
    pub.publish(msg)

def button_2_Click():
    msg = String()
    msg.data = "2"
    pub.publish(msg)

def button_3_Click():
    # form.close()
    msg = String()
    msg.data = "3"
    pub.publish(msg)

def button_4_Click():
    # form.close()
    msg = String()
    msg.data = "4"
    pub.publish(msg)
    

if __name__ == '__main__':
    rospy.init_node('bb_publisher_py_node')
    pub = rospy.Publisher("/bb_pub_py", String, queue_size=10)   # queue_size untuk buffer, kalau misalnya data yg dikirim banyaaaaaak banget, dan si subscriber tidak bisa membaca semua, maka perlu queue_size
    
    a = QApplication(sys.argv)

    form = QWidget()
    form.resize(500, 300)
    form.move(200, 200)
    form.setWindowTitle('Percobaan User Interface AGV')

    label = QLabel('Silahkan Pilih Tujuan')
    label.move(180, 30)
    label.setParent(form)

    button_1 = QPushButton('Waypoint 1')
    button_1.move(280,80)
    button_1.setParent(form)

    button_2 = QPushButton('Waypoint 2')
    button_2.move(120,80)
    button_2.setParent(form)

    button_3 = QPushButton('Waypoint 3')
    button_3.move(120,170)
    button_3.setParent(form)

    button_4 = QPushButton('Waypoint 4')
    button_4.move(280,170)
    button_4.setParent(form)
    
    button_1.clicked.connect(button_1_Click)
    button_2.clicked.connect(button_2_Click)
    button_3.clicked.connect(button_3_Click)
    button_4.clicked.connect(button_4_Click)

    form.show()

    a.exec_()