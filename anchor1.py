import rospy
from std_msgs.msg import Float32

def talker():
  print("talker hello")
  pub = rospy.Publisher('Anchor1_range',Float32)
  rospy.init_node('Anchor1',anoymous=True)
  rate = rospy.Rate(10)
  while not rospy.is_shutdown():
        recive_data = 0.123
        pub.publish(recive_data)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
  
