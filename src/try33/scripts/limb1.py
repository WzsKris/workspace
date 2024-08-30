 #!/usr/bin/python
#
# Send joint values to UR5 using messages
#

from std_msgs.msg import Header
from std_msgs.msg import Float64
import rospy

def main():

    rospy.init_node('limb1')
    pubList=[]
    pubList.append(rospy.Publisher('/joint11_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint12_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint13_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint14_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint15_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint16_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint17_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint18_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint19_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint20_effort_controller/command', Float64, queue_size=37))
    #pubList.append(rospy.Publisher('/joint21_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint22_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint23_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint24_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint25_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint26_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint27_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint28_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint29_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint30_effort_controller/command', Float64, queue_size=37))
    #pubList.append(rospy.Publisher('/joint31_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint32_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint33_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint34_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint35_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint36_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint37_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint38_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint39_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint37_effort_controller/command', Float64, queue_size=37))
   # pubList.append(rospy.Publisher('/joint41_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint42_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint43_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint44_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint45_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint46_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint47_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint48_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint49_effort_controller/command', Float64, queue_size=37))
    pubList.append(rospy.Publisher('/joint50_effort_controller/command', Float64, queue_size=37))
    #pub = rospy.Publisher('/joint01_effort_controller/command',Float64,queue_size=37)

    # Create the topic message
    pi=0.08
    jointValList=[]
    print(pi)


    for i in range(37):
        jointValList.append(Float64())
       # jointValList[i].data=0
        jointValList[i].data = (pi / 9)


    jointVal=Float64()
    jointVal.data= 0
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        for j in range(37):
            pubList[j].publish(jointValList[j])


        #pub.publish(jointVal)
        rate.sleep() #similar to rospy.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        print ("Program interrupted before completion")
