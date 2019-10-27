#!/usr/bin/env python
import rospy
from performance_test.msg import SuperAwesome

def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + "Received message: %s", msg.content)
    
def subscriber():
    rospy.init_node("python_subscriber", anonymous=True)

    rospy.Subscriber("performance_test", SuperAwesome, callback)
    rospy.spin()

if __name__ == "__main__":
    subscriber() 
