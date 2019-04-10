#include <ros/ros.h>

int main(int argc, char **argv) {

  ros::init(argc, argv, "ini_node_cpp");
  ros::NodeHandle nh;

  // ============ cara PERTAMA ============
  // ROS_INFO("Node has beed started");
  // ros::Duration(1.0).sleep();
  // ROS_INFO("Exit");

  // ============ cara KEDUA ============
  ros::Rate rate(10);
  while (ros::ok()) {
    ROS_INFO("hey tayo");
    rate.sleep();
  }
}
