#!/usr/bin/env python

import rospy
from ah_iot_sub_pub_sample.msg import IoTSensor

def iot_sensor_callback(iot_sensor_message):
    rospy.loginfo("data IoT diterima: (%d, %s, %.2f, %.2f)", iot_sensor_message.id, iot_sensor_message.name, iot_sensor_message.temperature, iot_sensor_message.humidity)

rospy.init_node('iot_sensor_subscriber', anonymous=True)

rospy.Subscriber("iot_sensor_topic", IoTSensor, iot_sensor_callback)

# spin() simply keeps python from exiting until this node is stopped
rospy.spin()
