#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

using namespace std;

ros::Publisher velocity_publisher;

// method to move the robot straight
void move(double speed, double distance, bool isForward);


int main(int argc, char **argv) {

  double speed;
  double distance;
  bool isForward;

  // inisialisasi ROS node baru dengan nama "robot_ngepel"
  ros::init(argc, argv, "robot_basic_movement");
  ros::NodeHandle n;

  velocity_publisher = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10);

  cout << "enter speed: ";
  cin >> speed;
  cout << "enter distance: ";
  cin >> distance;
  cout << "forward?: ";
  cin >> isForward;
  move(speed, distance, isForward);
  // move(2.0, 5, 1);



  return 0;
}



void move(double speed, double distance, bool isForward){

  geometry_msgs::Twist vel_msg;
  // distance = speed * time

  // set a random linear velocity in the x-axis
  if (isForward) {
    vel_msg.linear.x = abs(speed);
  }
  else{
    vel_msg.linear.x = -abs(speed);
  }
  vel_msg.linear.y = 0;
  vel_msg.linear.z = 0;

  // set a random angular velocity in the y-axis
  vel_msg.angular.x = 0;
  vel_msg.angular.y = 0;
  vel_msg.angular.z = 0;

  // t0: current time
  // loop
  // publish the velocity
  // estimate the distance = speed * (t1 - t0)
  // current_distance_move_by_robot <= distance
  double t0 = ros::Time::now().toSec();
  double current_distance = 0;
  ros::Rate loop_rate(10);
  do {
    velocity_publisher.publish(vel_msg);
    double t1 = ros::Time::now().toSec();
    current_distance = speed * (t1 - t0);
    ros::spinOnce();
    loop_rate.sleep();
  } while(current_distance < distance);
  vel_msg.linear.x = 0;
  velocity_publisher.publish(vel_msg);



}
