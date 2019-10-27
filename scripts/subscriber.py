#!/usr/bin/env python
import rospy
from performance_test.msg import SuperAwesome

def callback(msg):
    """
	Subscribes to SuperAwesome message using rospy.
	"""
    # Extracts timestamps from publisher at the time the message was created and when it is read
    subscriber_time = int(str(rospy.Time.now())[:10])
    publisher_time = int(msg.content[:10])
    # Calculate diff (in ms)
    diff = subscriber_time - publisher_time
    # Print time diff between pub/sub
    rospy.loginfo("py_subscriber time diff: %s ms\n", diff)

def subscriber():
    # Node, handler and subscriber init
    rospy.init_node("python_subscriber", anonymous=True)

    rospy.Subscriber("performance_test", SuperAwesome, callback)
    rospy.spin()

if __name__ == "__main__":
    subscriber() 
