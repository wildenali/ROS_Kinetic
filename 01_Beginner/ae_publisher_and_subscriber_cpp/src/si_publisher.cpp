#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char **argv) {

  // menginisiasi ROS node baru dengan nama "si_publisher"
  ros::init(argc, argv, "si_publisher");

  // membuat node handle, referensi kepada node baru
  ros::NodeHandle n;

  // membuat publisher dengan nama TOPIC "nge_gosip" yang akan mengirimkan pesan bertipe String
  ros::Publisher chatter_publisher = n.advertise<std_msgs::String>("nge_gosip", 1000);

  // Rate adalah class yang digunakan untuk mendefinisikan frekuensi untuk loop, program disini akan mengirimkan data setiap detiknya
  ros::Rate loop_rate(1.0);  // 1 pesan per detik

  int count = 0;
  while (ros::ok()) {
    // membuat pesan String ROS baru
    std_msgs::String msg;

    // membuat string nya
    std::stringstream ss;
    ss << "hey kamuuu... " << count;

    // menetapkan data string ke dalam ROS message data field
    msg.data = ss.str();

    // cetak data
    ROS_INFO("si publisher %s\n", msg.data.c_str());

    // publish pesan
    chatter_publisher.publish(msg);

    // need to call this function often to allow ROS to process incoming messages
    ros::spinOnce();

    // Sleep for the rest of cycle, to enforce the loop rate
    loop_rate.sleep();
    count++;
  }


  return 0;
}
