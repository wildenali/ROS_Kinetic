#include "ros/ros.h"
#include "std_msgs/String.h"

// Topic message callback
void nge_gosipCallback(const std_msgs::String::ConstPtr& msg) {
  ROS_INFO("dia nge gosip: [%s]\n", msg->data.c_str());
}

int main(int argc, char **argv) {

  // inisialisasi ROS Node baru dengan nama "si_subscriber"
  ros::init(argc, argv, "si_subscriber");

  // create a node handle: it reference assign to a new node
  ros::NodeHandle node;

  // Subscribe to a given topic, in the case "nge_gosip"
  // nge_gosipCallback: is the name of the callback function that will be execute each time a message is received
  ros::Subscriber sub = node.subscribe("nge_gosip", 1000, nge_gosipCallback);

  // Enter a loop, pumping callbacks
  ros::spin();

  return 0;
}
