#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState

class JointDistanceRecorder:
    def __init__(self):
        # Initialize the ROS node
        rospy.init_node('joint_distance_recorder')
        
        # Initialize variables
        self.previous_position = None
        self.total_distance = 0.0
        
        # Subscribe to the /joint_states topic
        rospy.Subscriber('/joint_states', JointState, self.joint_states_callback)
        
    def joint_states_callback(self, msg):
        # Extract the joint names and positions from the message
        joint_positions = dict(zip(msg.name, msg.position))
        
        # Check if joint02 is in the received joint states
        if 'joint02' in joint_positions:
            current_position = joint_positions['joint02']
            
            # Compute distance traveled if there's a previous position
            if self.previous_position is not None:
                distance = abs(current_position - self.previous_position)
                self.total_distance += distance
                rospy.loginfo(f'Distance traveled by joint02: {self.total_distance:.2f} meters')
            
            # Update the previous position
            self.previous_position = current_position

    def run(self):
        # Keep the node running
        rospy.spin()

if __name__ == '__main__':
    try:
        recorder = JointDistanceRecorder()
        recorder.run()
    except rospy.ROSInterruptException:
        pass
