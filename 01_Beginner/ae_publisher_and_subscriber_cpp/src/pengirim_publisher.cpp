#include "ros/ros.h"              // header2 yang dibutuhkan oleh sistem ROS
#include "std_msgs/String.h"      //
#include <sstream>

// mendemokan cara mudah mengirim pesan dengan system ROS
int main(int argc, char **argv) {

  // initialize ROS, dengan remapping nama
  ros::init(argc, argv, "sipengirim");

  // jalur komunikasi utama dengan sistem ROS
  ros::NodeHandle n;

  // The advertise() function is how you tell ROS that you want to publish on a given topic name.
  // nilai 1000 adalah size of message queue used for publishing messages
  ros:: Publisher chatter_pub = n.advertise<std_msgs::String>("obrolan", 1000);
  ros::Rate loop_rate(10);

  // ini untuk ngitung udah berapa banyak message yang telah dikirimkan
  int count = 0;

  while (ros::ok()) {

    // message object
    std_msgs::String msg;

    std::stringstream ss;
    ss << "hay worldddd " << count;
    msg.data = ss.str();

    ROS_INFO("%s", msg.data.c_str());

    // cara ngirim pesan adalah dengan menggunakan fungsi publish()
    chatter_pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();

    ++count;

  }


  return 0;
}
