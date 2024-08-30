 #!/usr/bin/python
#
# Send joint values to UR5 using messages
#

from std_msgs.msg import Header
from std_msgs.msg import Float64
import rospy

def main():

    rospy.init_node('limb')
    pubList=[]
    #pubList.append(rospy.Publisher('/joint01_effort_controller/command',Float64,queue_size=10))
    pubList.append(rospy.Publisher('/joint02_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint03_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint04_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint05_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint06_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint07_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint08_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint09_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint10_effort_controller/command', Float64, queue_size=9))

    #pub = rospy.Publisher('/joint01_effort_controller/command',Float64,queue_size=10)
    print('start')
    # Create the topic message
    #pi=-0.1
    jointValList=[]

    torque = -0.5
    num_joints = 9   # Number of joints from joint02 to joint11

    # Calculate torque values for each joint
    for i in range(num_joints):
        #torque = max_torque - (max_torque - min_torque) * (i / (num_joints - 1))
        jointValList.append(Float64(torque))

    # Define the rate of the loop
    rate = rospy.Rate(1)  # 1 Hz (1 cycle per second)

    # Main loop to publish torque values
    while not rospy.is_shutdown():
        for j in range(num_joints):
            pubList[j].publish(jointValList[j])
        rate.sleep()  # Sleep for the defined rate (1 Hz)
        print('---')

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        print("Program interrupted before completion")
