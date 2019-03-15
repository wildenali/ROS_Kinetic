#include "ros/ros.h"
#include "std_msgs/String.h"

// ini program untuk menerima pesan dari pengirim (publisher)

// fungsi callback yang akan di panggil ketika si publisher ngirim message
void obrolanCallback(const std_msgs::String::ConstPtr& msg) {
  ROS_INFO("I heard:[%s]", msg->data.c_str());
}

int main(int argc, char **argv) {

  ros::init(argc, argv, "sipenerima");  // usahakan buat nama si remapping nya sesuai dengan nama file nya, karena supaya mudah memanggilnya, contoh ros::init(argc, argv, "penerima_subscriber");

  ros::NodeHandle n;

  // 1000 adalah queue size, jika queue mencapai 1000 pesan, we will start throwing away old messages as new ones arrive
  ros::Subscriber sub = n.subscribe("obrolan", 1000, obrolanCallback);

  ros::spin();


  return 0;
}
