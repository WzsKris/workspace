#!/usr/bin/env python

import rospy
from gazebo_msgs.msg import LinkStates
from gazebo_msgs.msg import ModelStates
from std_msgs.msg import Float64
import math

# Initialize global variable for previous position
previous_position = None

def model_states_callback(data):
    global previous_position
    
    try:
        # Find the index of the link named 'fullurdf3::sec02'
        index = data.name.index('fullurdf3::sec02')
        
        # Extract the position of sec02 link within fullurdf3 model
        current_position = data.pose[index].position
        current_position_xy = (current_position.x, current_position.y)

        # Calculate Euclidean distance if previous position is available
        if previous_position is not None:
            distance = math.sqrt(
                (current_position_xy[0] - previous_position[0]) ** 2 +
                (current_position_xy[1] - previous_position[1]) ** 2
            )
            # Publish the calculated distance
            distance_pub.publish(distance)
            rospy.loginfo(f"Published Distance: {distance:.3f} meters")
        
        # Update previous position to current position for next calculation
        previous_position = current_position_xy

    except ValueError:
        rospy.logwarn("Link 'fullurdf3::sec02' not found in link states")


# Initialize the node and the publisher
rospy.init_node('sec02_distance_publisher', anonymous=True)
distance_pub = rospy.Publisher('/sec02_distance', Float64, queue_size=10)

# Subscribe to the /gazebo/link_states topic
rospy.Subscriber("/gazebo/model_states", ModelStates, model_states_callback)

rospy.loginfo("Publishing Euclidean distance for sec02 link based on /gazebo/link_states...")
rospy.spin()
