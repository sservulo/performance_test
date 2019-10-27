#!/usr/bin/env python

import rospy
from performance_test.msg import SuperAwesome

def publisher():
    """
	Publishes SuperAwesome message using rospy.
	"""
    # Node, handler and publisher init
    rospy.init_node("python_publisher", anonymous=True)

    pub = rospy.Publisher("performance_test", SuperAwesome, queue_size = 100000)
    
    rate_param = rospy.get_param("/publish_rate")
    rate = rospy.Rate(rate_param)

    while not rospy.is_shutdown():
        msg = SuperAwesome()
        # Since SuperAwesome is only allowed to contain string, use to send time at message creation
        msg.content = str(rospy.Time.now())
        pub.publish(msg)

        # Check latest rate param and update if different
        if(rate_param != rospy.get_param("/publish_rate")):
            rate_param = rospy.get_param("/publish_rate")
            rate = rospy.Rate(rate_param)

        # Sleep thread until next loop
        rate.sleep()

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass 
