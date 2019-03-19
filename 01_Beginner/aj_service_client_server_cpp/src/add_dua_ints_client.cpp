#include "ros/ros.h"
#include "aj_service_client_server_cpp/AddDuaInts.h"
#include <cstdlib>

int main(int argc, char **argv) {
  ros::init(argc, argv, "add_dua_ints_client");
  if (argc != 3) {
    ROS_INFO("usage: add_dua_ints_client X Y");
    return 1;
  }

  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<aj_service_client_server_cpp::AddDuaInts>("add_dua_ints");
  aj_service_client_server_cpp::AddDuaInts srv;
  srv.request.a = atoll(argv[1]);
  srv.request.b = atoll(argv[2]);

  if (client.call(srv)) {
    ROS_INFO("Sum: %ld",(long int)srv.response.sum);
  }
  else {
    ROS_INFO("Failed to call service add_dua_ints");
    return 1;
  }


  return 0;
}
