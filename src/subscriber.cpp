#include "ros/ros.h"
#include "performance_test/SuperAwesome.h"

void callback(const performance_test::SuperAwesome::ConstPtr& msg)
{
  ROS_INFO("Received message: %s", msg->content.c_str());
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "cpp_subscriber");
  ros::NodeHandle n;

  ros::Subscriber subscriber = n.subscribe("performance_test", 1000, callback);

  ros::spin();

  return 0;
}