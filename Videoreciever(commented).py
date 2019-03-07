#!/usr/bin/env python
import rospy
import cv2
import sys
import numpy as np
from cv_bridge import CvBridge, CvBridgeError # Import cvbridge to allow convertions between ROS and Opencv
from sensor_msgs.msg import Image       # Import the Image ROS message 

br = CvBridge()      # Initialize cvbridge

def callback(data):  #define what the code should do when recieves a new message
    try:
        image = br.imgmsg_to_cv2(data,"bgr8") # declare frame as the convertion of ROS image to opencv image (BGR 8 bits)
        resize_image = cv2.resize (image,none,fx=2,fy=2)  # resize the image in a factor of 2 for both hieght amd width
        cv2.imshow("Video",resize_image)        # show the image  
        cv2.waitKey(1)
    except CvBridgeError as e:
        print(e)

def videoreciever():
    rospy.init_node('reciever',anonymous = True)    # Initialize node as "reciever" 
    rospy.Subscriber("video_topic",Image,callback)  # Set the node as a subscriber of images in "video_topic" 
    rospy.spin()

if __name__ == '__main__':
    try:
        videoreciever()                  # run the code 
    except rospy.ROSInterruptException:  # Allow code to be interrupt via ROS        
        pass
