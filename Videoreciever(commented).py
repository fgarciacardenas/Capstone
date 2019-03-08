#!/usr/bin/env python
import rospy
import cv2
import sys
import numpy as np
from cv_bridge import CvBridge, CvBridgeError # Import cvbridge to allow convertions between ROS and Opencv
from sensor_msgs.msg import Image       # Import the Image ROS message 

# Initialize cvbridge
br = CvBridge()      

#define what the code should do when recieves a new message
def callback(data):  
    try:
        # declare frame as the convertion of ROS image to opencv image (gray scale 8 bits)
        image = br.imgmsg_to_cv2(data,"mono8") 
        
        # resize the image in a factor of 4 for both hight amd width using cubic interpolation method
        resize_image = cv2.resize (image,(0,0),fx=4,fy=4,interpolation=cv2.INTER_CUBIC)  
        
        # show the image
        cv2.imshow("Video",resize_image)         
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    except CvBridgeError as e:
        print(e)

def videoreciever():
    # Initialize node as "reciever" 
    rospy.init_node('reciever',anonymous = True)   
    
    # Set the node as a subscriber of images in "video_topic"
    rospy.Subscriber("video_topic",Image,callback) 
    rospy.spin()

if __name__ == '__main__':
    try:
        videoreciever()                     # Run the code
    except rospy.ROSInterruptException:  # Allow code to be interrupt via ROS        
        cap.release()
        cv2.destroyAllWindows()
        pass
