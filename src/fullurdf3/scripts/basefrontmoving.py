#!/usr/bin/python

from std_msgs.msg import Float64
import rospy

def main():

    rospy.init_node('basefront')
    pubList = []

    pubList.append(rospy.Publisher('/joint11_effort_controller/command', Float64, queue_size=36))
    pubList.append(rospy.Publisher('/joint21_effort_controller/command', Float64, queue_size=36))

    num_joints = len(pubList)   
    torque_value = -2
    current_value = torque_value  # Start with -1.5

    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        jointValList = []
        
        # Alternate between -1.5 and 0
        for i in range(num_joints):
            jointValList.append(Float64(current_value))
            print("--------")
        
        # Publish torque values
        for j in range(num_joints):
            pubList[j].publish(jointValList[j])

            print('start')

        # Change the current_value between -1.5 and 0
        if current_value == torque_value:
            current_value = 0
        else:
            current_value = torque_value

        print("Current torque value:", current_value)

        rate.sleep()  # Sleep for the defined rate (10 Hz)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        print("Program interrupted before completion")
