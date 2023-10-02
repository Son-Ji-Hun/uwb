import rospy
from std_msgs.msg import Float32

def talker():
    pub = rospy.Publisher('anchor1_range', Float32)
    rospy.init_node('Anchor1', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        recive_data = 0.123
        rospy.loginfo(recive_data)
        pub.publish(recive_data)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
