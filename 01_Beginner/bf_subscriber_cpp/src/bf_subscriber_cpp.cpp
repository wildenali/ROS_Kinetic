#include <ros/ros.h>
#include <std_msgs/String.h>

void callback_terima_dari_be_pub_cpp(const std_msgs::String& msg) {
  ROS_INFO("Pesan diterima: %s", msg.data.c_str());
}

int main(int argc, char **argv) {

  ros::init(argc, argv, "be_subscriber_cpp_node");
  ros::NodeHandle nh;

  ros::Subscriber sub = nh.subscribe("/be_pub_cpp", 1000, callback_terima_dari_be_pub_cpp);

  ros::spin();
}
