#include "ros/ros.h"
#include "performance_test/SuperAwesome.h"

// Initial publish rate constant
int kPublishRate = 10;

int main(int argc, char **argv) {
  // Node, handler and publisher init
  ros::init(argc, argv, "cpp_publisher");

  ros::NodeHandle n;
  ros::Publisher publisher = n.advertise<performance_test::SuperAwesome>("performance_test", 100000);

  // Sets rate from param
  int rate_param = kPublishRate;
  n.getParam("/publish_rate", rate_param);
  ros::Rate publish_rate(rate_param);

  while (ros::ok()) {
    // Creates new SuperAwesome message
    performance_test::SuperAwesome msg;
    // Since SuperAwesome is only allowed to contain string, use to send time at message creation
    msg.content = std::to_string(ros::Time::now().toNSec());
    publisher.publish(msg);

    ros::spinOnce();

    // Check latest rate param and update if different
    int current_rate_param = kPublishRate;
    n.getParam("/publish_rate", current_rate_param);
    if(rate_param != current_rate_param) {
      rate_param = current_rate_param;
      ros::Rate latest_rate(rate_param);
      publish_rate = latest_rate;
    }

    // Sleep thread until next loop
    publish_rate.sleep();
  }
  return 0;
} 
