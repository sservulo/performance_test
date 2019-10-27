#!/usr/bin/env python

import rospy
from performance_test.msg import SuperAwesome

def publisher():
    rospy.init_node("python_publisher", anonymous=True)

    pub = rospy.Publisher("performance_test", SuperAwesome, queue_size=1000)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        msg = SuperAwesome()
        msg.content = "Sample content"
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass 
