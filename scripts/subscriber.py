#!/usr/bin/env python
import rospy
from performance_test.msg import SuperAwesome

def callback(msg):
    subscriber_time = int(str(rospy.Time.now())[:10])
    publisher_time = int(msg.content[:10])
    diff = subscriber_time - publisher_time
    rospy.loginfo("py_subscriber time diff: %s ms\n", diff)

def subscriber():
    rospy.init_node("python_subscriber", anonymous=True)

    rospy.Subscriber("performance_test", SuperAwesome, callback)
    rospy.spin()

if __name__ == "__main__":
    subscriber() 
