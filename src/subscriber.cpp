#include "ros/ros.h"
#include "performance_test/SuperAwesome.h"

void callback(const performance_test::SuperAwesome::ConstPtr& msg)
{
    int subscriber_time = std::stoi(std::to_string(ros::Time::now().toSec()).substr(0,10));
    int publisher_time = std::stoi(msg->content.substr(0,10));
    int diff = subscriber_time - publisher_time;
    ROS_INFO("cpp_subscriber time diff: %i ms\n", diff);
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "cpp_subscriber");
  ros::NodeHandle n;

  ros::Subscriber subscriber = n.subscribe("performance_test", 1000, callback);

  ros::spin();

  return 0;
}