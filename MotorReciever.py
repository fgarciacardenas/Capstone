#!/usr/bin/env python
from __future__ import division
import time
import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import String #String message type

#Disables warnings and sets up BCM GPIO numbering
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Sets GPIO out pins
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

#Creates PWM instances (channel,frequency)
pwm_A1 = GPIO.PWM(2,490)
pwm_B1 = GPIO.PWM(3,490)
pwm_A2 = GPIO.PWM(27,490)
pwm_B2 = GPIO.PWM(22,490)

#Initial PWM, for DC motors it is always 0
pwm_A1.start(0)
pwm_B1.start(0)
pwm_A2.start(0)
pwm_B2.start(0)

#Defines function that will execute every time a message is received
def callback(data):
    
    #Assigns the data received to a variable and split it for each PWM
    V = data.data
    cmd = V.split("/")
    
    #Assigns each PWM to a variable
    V1 = int(cmd[0])
    V2 = int(cmd[1])
    V3 = int(cmd[2])
    V4 = int(cmd[3])
    
    #Prints the PWM values
    print V1, V2, V3, V4
    
    #Changes the Duty cycles
    #pwm_A1.ChangeDutyCycle(V1)
    #pwm_B1.ChangeDutyCycle(V2)
    #pwm_A2.ChangeDutyCycle(V3)
    #pwm_B2.ChangeDutyCycle(V4)

def listener():
    rospy.init_node('RMotores', anonymous=True) #Tells rospy the name of this node
    rospy.Subscriber("joystick_topic", String, callback) #Declares that the node subscrbes to the 'joystick_topic' topic whose message type is String. 'callback' function is invoked when messages are received
    rospy.spin() #Keeps the node from exiting until the node has been shutdown.

#Checks if this module has been imported
if __name__ == '__main__':
    listener() #Invokes listener function
