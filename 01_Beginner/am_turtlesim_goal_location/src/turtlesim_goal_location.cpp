#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

using namespace std;

// ini untuk void move
ros::Publisher velocity_publisher;

// ========== ini untuk void rotate ==========
#include "turtlesim/Pose.h"

ros::Subscriber pose_subscriber;
turtlesim::Pose turtlesim_pose;

const double x_min = 0.0;
const double y_min = 0.0;
const double x_max = 11.0;  // maksimal ukuran area layar
const double y_max = 11.0;  // maksimal ukuran area layar

const double PI = 3.14159265359;
// ========== ini untuk void rotate ==========


// method to move the robot straight
void move(double speed, double distance, bool isForward);

// ========== ini untuk void rotate ==========
void rotate(double angular_speed, double angle, bool clockwise);
double degrees2radians(double angle_in_degrees);
double setDesiredOrientation(double desired_angle_radians);
void poseCallback(const turtlesim::Pose::ConstPtr & pose_message);
// ========== ini untuk void rotate ==========

// ========== ini untuk void goal ==========
void moveGoal(turtlesim::Pose goal_pose, double distance_tolerance);
// ========== ini untuk void goal ==========


int main(int argc, char **argv) {



  // inisialisasi ROS node baru dengan nama "turtlesim_goal_location"
  ros::init(argc, argv, "turtlesim_goal_location");
  ros::NodeHandle n;

  velocity_publisher = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10);

  pose_subscriber = n.subscribe("/turtle1/pose", 10, poseCallback);

  // double speed;
  // double distance;
  // bool isForward;
  //
  // cout << "enter speed: ";
  // cin >> speed;
  // cout << "enter distance: ";
  // cin >> distance;
  // cout << "forward?: ";
  // cin >> isForward;
  // move(speed, distance, isForward);
  // // move(2.0, 5, 1);
  //
  //
  // // ========== ini untuk void rotate ==========
  // double angular_speed;
  // double angle;
  // bool clockwise;
  //
  // cout << "enter angular velocity (degree/sec): ";
  // cin >> angular_speed;
  // cout << "enter desired angle (degree): ";
  // cin >> angle;
  // cout << "clockwise?: ";
  // cin >> clockwise;
  // rotate(degrees2radians(angular_speed), degrees2radians(angle), clockwise);
  // // ========== ini untuk void rotate ==========

// // ========== ini untuk percobaan void rotate ==========
  // ros::Rate loop_rate(0.5);
  // setDesiredOrientation(degrees2radians(180));
  // loop_rate.sleep();
  // setDesiredOrientation(degrees2radians(-60));
  // loop_rate.sleep();
  // setDesiredOrientation(degrees2radians(0));
  // ros::spin();
// // ========== ini untuk percobaan void rotate ==========

// // ========== ini untuk percobaan void moveGoal ==========
  ros::Rate loop_rate(0.5);
  turtlesim::Pose goal_pose;
  goal_pose.x = 1;
  goal_pose.y = 1;
  goal_pose.theta = 0;
  moveGoal(goal_pose, 0.01);
  loop_rate.sleep();
// // ========== ini untuk percobaan void moveGoal ==========


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

// ========== ini untuk void rotate ==========
void rotate(double angular_speed, double relative_angle, bool clockwise){
  geometry_msgs::Twist vel_msg;
  // set a random linear velocity in the x-axis
  vel_msg.linear.x = 0;
  vel_msg.linear.y = 0;
  vel_msg.linear.z = 0;

  // set a random angular velocity in the y-axis
  vel_msg.angular.x = 0;
  vel_msg.angular.y = 0;

  if (clockwise) {
    vel_msg.angular.z = -abs(angular_speed);
  }
  else {
    vel_msg.angular.z = abs(angular_speed);
  }

  double current_angle = 0.0;
  double t0 = ros::Time::now().toSec();
  ros::Rate loop_rate(10);  // 10 pesan perdetik
  do {
    velocity_publisher.publish(vel_msg);
    double t1 = ros::Time::now().toSec();
    current_angle = angular_speed * (t1 - t0);
    ros::spinOnce();
    loop_rate.sleep();
  } while(current_angle < relative_angle);
  vel_msg.angular.z = 0;
  velocity_publisher.publish(vel_msg);


}

double degrees2radians(double angle_in_degrees){
  return angle_in_degrees * PI / 180.0;
}

double setDesiredOrientation(double desired_angle_radians){
  double relative_angle_radians = desired_angle_radians - turtlesim_pose.theta;
  bool clockwise = ((relative_angle_radians < 0) ? true:false);
  // cout << desired_angle_radians << "," << turtlesim_pose.theta << "," << relative_angle_radians << "," << clockwise << endl;
  rotate(abs(relative_angle_radians), abs(relative_angle_radians), clockwise);
}


void poseCallback(const turtlesim::Pose::ConstPtr & pose_message){
  turtlesim_pose.x = pose_message->x;
  turtlesim_pose.y = pose_message->y;
  turtlesim_pose.theta = pose_message->theta;
}
// ========== ini untuk void rotate ==========


// ========== ini untuk void goal ==========
double getDistance(double x1, double y1, double x2, double y2){
  return sqrt(pow((x1-x2),2) + pow((y1-y2),2));
}

void moveGoal(turtlesim::Pose goal_pose, double distance_tolerance){
  geometry_msgs::Twist vel_msg;

  ros::Rate loop_rate(10);
  do {
    // *********** Proportional Controller ***********
    // linear velocity in the x-axis
    vel_msg.linear.x = 1.5*getDistance(turtlesim_pose.x, turtlesim_pose.y, goal_pose.x, goal_pose.y);
    vel_msg.linear.y = 0;
    vel_msg.linear.z = 0;

    // angular velocity in the z-axis
    vel_msg.angular.x = 0;
    vel_msg.angular.y = 0;

    // nilai 4 karena Proportional controler, sifat si P kontroler
    vel_msg.angular.z = 4 * (atan2(goal_pose.y - turtlesim_pose.y, goal_pose.x - turtlesim_pose.x) - turtlesim_pose.theta);


    velocity_publisher.publish(vel_msg);
    ros::spinOnce();
    loop_rate.sleep();

  } while(getDistance(turtlesim_pose.x, turtlesim_pose.y, goal_pose.x, goal_pose.y) > distance_tolerance);
  cout << "end move goal" << endl;
  vel_msg.linear.x = 0;
  vel_msg.angular.z = 0;
  velocity_publisher.publish(vel_msg);

}
// ========== ini untuk void goal ==========
