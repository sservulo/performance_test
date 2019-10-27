#include "ros/ros.h"
#include "performance_test/SuperAwesome.h"


int main(int argc, char **argv) {
  ros::init(argc, argv, "cpp_publisher");
  ros::NodeHandle n;

  ros::Publisher publisher = n.advertise<performance_test::SuperAwesome>("performance_test", 10);

  ros::Rate loop_rate(10);

  while (ros::ok()) {
    performance_test::SuperAwesome msg;
    msg.content = "Content sample";
    ROS_INFO("%s", msg.content.c_str());

    publisher.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
  }
  return 0;
} 
