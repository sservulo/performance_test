#!/usr/bin/env python
import rospy
from performance_test.msg import SuperAwesome

def callback(msg):
    """
	Subscribes to SuperAwesome message using rospy.
	"""
    # Extracts timestamps from publisher at the time the message was created and when it is read
    # Slice each timestamp to milliseconds range
    subscriber_time = int(str(rospy.Time.now())[:13])
    publisher_time = int(msg.content[:13])
    # Calculate diff (in ms)
    diff = subscriber_time - publisher_time
    # Print time diff between pub/sub
    rospy.loginfo("py_subscriber time diff: %s ms\n", diff)
    if(diff >= 10):
        raise Exception
        quit()

def subscriber():
    # Node, handler and subscriber init
    rospy.init_node("python_subscriber", anonymous=True)

    rospy.Subscriber("performance_test", SuperAwesome, callback)
    rospy.spin()

if __name__ == "__main__":
    subscriber() 
