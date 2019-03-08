#!/usr/bin/env python
import numpy as np
import rospy
import cv2
import sys
from cv_bridge import CvBridge       # Import cvbridge to allow convertions between ROS and Opencv
from sensor_msgs.msg import Image    # Import the Image ROS message 

br=CvBridge()               # Initialize cvbridge
cap=cv2.VideoCapture(0)     # Declare cap as video capture from the camera #0
cap.set(3,120)              # Set width of the image as 120 pixels
cap.set(4,100)              # Set height of the image as 100 pixels
#cap.set(5,15)
              
def talker():
    pub=rospy.Publisher('video_topic',Image,queue_size=10) #Set the node as a publisher of Image messages in 'video_topic'
    rospy.init_node('transmiter',anonymous = True)  #Initialize the node as 'transmiter'
    while not rospy.is_shutdown():
        ret, img = cap.read() # get "frame" The RGB matrix (Image from Opencv)
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ros_img = br.cv2_to_imgmsg(img_gray,"mono8")
        pub.publish(ros_img) # Convert the RGB matrix to ROS image message and finally publish
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    try:
        talker()                     # Run the code
        #cap.release()
        #cv2.destroyAllWindows()
    except rospy.ROSInterruptException:  # Allow code to be interrupt via ROS        
        cap.release()
        cv2.destroyAllWindows()
        pass
