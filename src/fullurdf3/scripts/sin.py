#!/usr/bin/python
#
# Send joint values to UR5 using messages
#

from std_msgs.msg import Float64
import rospy
import math
import time

def main():

    rospy.init_node('limb')
    pubList = []
    #pubList.append(rospy.Publisher('/joint01_effort_controller/command', Float64, queue_size=11))
    pubList.append(rospy.Publisher('/joint02_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint03_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint04_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint05_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint06_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint07_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint08_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint09_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint10_effort_controller/command', Float64, queue_size=9))

    rate = rospy.Rate(20)  # 10 Hz

    num_joints = len(pubList)
    amplitude = 0.35  # Maximum torque (amplitude of the sine wave)
    frequency = 50  # Frequency of the sine wave in Hz

    start_time = time.time()

    while not rospy.is_shutdown():
        current_time = time.time() - start_time  # Elapsed time since the start
        jointValList = []

        # Generate sinusoidal torque for each joint based on time
        for i in range(num_joints):
            torque_value = amplitude * math.sin(2 * math.pi * frequency * current_time)
            jointValList.append(Float64(torque_value))
            print(f"Publishing torque for joint {i + 2}: {torque_value:.3f}")

        # Publish torque values for each joint
        for j in range(num_joints):
            pubList[j].publish(jointValList[j])

        rate.sleep()  # Sleep for the defined rate (10 Hz)


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        print("Program interrupted before completion")
