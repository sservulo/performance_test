#include "ros/ros.h"
#include "performance_test/SuperAwesome.h"

int kPublishRate = 10;

int main(int argc, char **argv) {
  ros::init(argc, argv, "cpp_publisher");

  ros::NodeHandle n;
  ros::Publisher publisher = n.advertise<performance_test::SuperAwesome>("performance_test", 1000);

  int rate_param = kPublishRate;
  n.getParam("/publish_rate", rate_param);  

  ros::Rate publish_rate(rate_param);

  while (ros::ok()) {
    performance_test::SuperAwesome msg;
    msg.content = std::to_string(ros::Time::now().toSec());
    ROS_INFO("%s", msg.content.c_str());

    publisher.publish(msg);

    ros::spinOnce();

    int current_rate_param = kPublishRate;
    n.getParam("/publish_rate", current_rate_param);
    if(rate_param != current_rate_param) {
      rate_param = current_rate_param;
      ros::Rate latest_rate(rate_param);
      publish_rate = latest_rate;
    }

    publish_rate.sleep();
  }
  return 0;
} 
