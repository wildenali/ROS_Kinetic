#!/usr/bin/env python

import rospy
from ah_iot_sub_pub_sample.msg import IoTSensor
import random

# membuat publisher baru, dengan nama 'iot_sensor_topic'
pub = rospy.Publisher('iot_sensor_topic', IoTSensor, queue_size=10)

# inisialisasi node
rospy.init_node('iot_sensor_publisher_node',anonymous=True)

# set the loop rate
rate = rospy.Rate(1)    # 1Hz

i = 0
while not rospy.is_shutdown():
    iot_sensor = IoTSensor()
    iot_sensor.id = 1
    iot_sensor.name = "iot_parking_01"
    iot_sensor.temperature = 24.33 + (random.random()*2)
    iot_sensor.humidity = 33.41 + (random.random()*2)
    rospy.loginfo("Saya publish:")
    rospy.loginfo(iot_sensor)
    pub.publish(iot_sensor)
    rate.sleep()
    i=i+1
