#!/usr/bin/env python

import rospy
from performance_test.msg import SuperAwesome

def publisher():
    rospy.init_node("python_publisher", anonymous=True)

    pub = rospy.Publisher("performance_test", SuperAwesome, queue_size = 1000)
    
    rate_param = rospy.get_param("/publish_rate")
    rate = rospy.Rate(rate_param)

    while not rospy.is_shutdown():
        msg = SuperAwesome()
        msg.content = str(rospy.Time.now())
        rospy.loginfo(msg)
        pub.publish(msg)
        if(rate_param != rospy.get_param("/rate_param")):
            rate_param = rospy.get_param("/rate_param")
            rate = rospy.Rate(rate_param)
        rate.sleep()

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass 
