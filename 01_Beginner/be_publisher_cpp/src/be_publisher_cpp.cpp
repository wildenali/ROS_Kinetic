#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char **argv) {

  ros::init(argc, argv, "be_publisher_cpp_node");
  ros::NodeHandle nh;

  ros::Publisher pub = nh.advertise<std_msgs::String>("/be_pub_cpp", 10);   // 10 adalah buffer, klo di python itu queue_size=10

  ros::Rate rate(3);

  while (ros::ok()) {
    std_msgs::String msg;
    msg.data = "Hi, ini publisher c++ looh";
    pub.publish(msg);
    rate.sleep();
  }


}
