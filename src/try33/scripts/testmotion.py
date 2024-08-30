 #!/usr/bin/python
#
# Send joint values to UR5 using messages
#

from std_msgs.msg import Header
from std_msgs.msg import Float64MultiArray
import rospy
import time

def main():

    rospy.init_node('limb')
    pubList=[]
    pubList.append(rospy.Publisher('/joint01_effort_controller/command', Float64MultiArray, queue_size=10))
    pubList.append(rospy.Publisher('/joint02_effort_controller/command', Float64MultiArray, queue_size=10))
    pubList.append(rospy.Publisher('/joint03_effort_controller/command', Float64MultiArray, queue_size=10))
    pubList.append(rospy.Publisher('/joint04_effort_controller/command', Float64MultiArray, queue_size=10))
    pubList.append(rospy.Publisher('/joint05_effort_controller/command', Float64MultiArray, queue_size=10))
    pubList.append(rospy.Publisher('/joint06_effort_controller/command', Float64MultiArray, queue_size=10))
    pubList.append(rospy.Publisher('/joint07_effort_controller/command', Float64MultiArray, queue_size=10))
    pubList.append(rospy.Publisher('/joint08_effort_controller/command', Float64MultiArray, queue_size=10))
    pubList.append(rospy.Publisher('/joint09_effort_controller/command', Float64MultiArray, queue_size=10))
    pubList.append(rospy.Publisher('/joint10_effort_controller/command', Float64MultiArray, queue_size=10))
    
    
    

    #pub = rospy.Publisher('/joint01_effort_controller/command',Float64MultiArray,queue_size=50)

    # Create the topic message
    
    pi=[-0.03]
    while not rospy.is_shutdown():
       
        jointValList=[]

        print(pi)
  
    
        
        for i in range(10):
            jointValList.append(Float64MultiArray())
            # jointValList[i].data=0
            jointValList[i].data = [pi[0] / 9]

            #time.sleep(1)



        #jointVal=Float64MultiArray()
        #jointVal.data= 0
        rate = rospy.Rate(1)
        rate.sleep()

        for j in range(10):
            pubList[j].publish(jointValList[j])
        time.sleep(0.1)
        print(pi)
        pi[0]=-pi[0]

        #pub.publish(jointVal)
         #similar to rospy.sleep(1)
         
         

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        print ("Program interrupted before completion")
