#include "ros/ros.h"
#include "aj_service_client_server_cpp/AddDuaInts.h"

bool add(aj_service_client_server_cpp::AddDuaInts::Request &rekues,
         aj_service_client_server_cpp::AddDuaInts::Response &respon)
{
  respon.sum = rekues.a + rekues.b;
  ROS_INFO("rekues: x = %ld, y = %ld", (long int)rekues.a, (long int)rekues.b);
  ROS_INFO("kirim balik responnya: %ld", (long int)respon.sum);
  return true;
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "add_dua_ints_server");
  ros::NodeHandle n;

  ros::ServiceServer service = n.advertiseService("add_dua_ints", add);
  ROS_INFO("Ready to add two ints");
  ros::spin();

  return 0;
}
