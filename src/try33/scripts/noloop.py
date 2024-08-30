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
    pubList.append(rospy.Publisher('/joint01_effort_controller/command', Float64, queue_size=10))
    pubList.append(rospy.Publisher('/joint02_effort_controller/command', Float64, queue_size=10))
    pubList.append(rospy.Publisher('/joint03_effort_controller/command', Float64, queue_size=10))
    pubList.append(rospy.Publisher('/joint04_effort_controller/command', Float64, queue_size=10))
    pubList.append(rospy.Publisher('/joint05_effort_controller/command', Float64, queue_size=10))
    pubList.append(rospy.Publisher('/joint06_effort_controller/command', Float64, queue_size=10))
    pubList.append(rospy.Publisher('/joint07_effort_controller/command', Float64, queue_size=10))
    pubList.append(rospy.Publisher('/joint08_effort_controller/command', Float64, queue_size=10))
    pubList.append(rospy.Publisher('/joint09_effort_controller/command', Float64, queue_size=10))
    pubList.append(rospy.Publisher('/joint10_effort_controller/command', Float64, queue_size=10))


    # Create the topic message
    pi=-0.05
    jointValList=[]

    print(pi)

    for i in range(10):
        jointValList.append(Float64())
       # jointValList[i].data=0
        jointValList[i].data = (pi / 9)


    jointVal=Float64()
    jointVal.data= 0
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        for j in range(10):
            pubList[j].publish(jointValList[j])


        #pub.publish(jointVal)
        rate.sleep() #similar to rospy.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        print ("Program interrupted before completion")
