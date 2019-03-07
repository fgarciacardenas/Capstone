#!/usr/bin/env python
from __future__ import division
import time
import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import String #String message type

#Disables warnings and sets up BCM GPIO numbering
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Define PWM and DIR GPIO Pins
DIR_PIN1 = 5
DIR_PIN2 = 6
PWM_PIN1 = 12
PWM_PIN2 = 13

#Sets GPIO out pins
GPIO.setup(DIR_PIN1, GPIO.OUT)
GPIO.setup(DIR_PIN2, GPIO.OUT)
GPIO.setup(PWM_PIN1, GPIO.OUT)
GPIO.setup(PWM_PIN2, GPIO.OUT)

#Creates PWM instances (channel,frequency)
pwm1 = GPIO.PWM(PWM_PIN1,490)
pwm2 = GPIO.PWM(PWM_PIN2,490)

#Initial PWM, for DC motors it is always 0
pwm1.start(0)
pwm2.start(0)

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
    
    if (V1 == 0 and V3 == 0):
        GPIO.output(DIR_PIN1,GPIO.HIGH)
        GPIO.output(DIR_PIN2,GPIO.HIGH)
        pwm1.ChangeDutyCycle(V2)
        pwm2.ChangeDutyCycle(V4)

    elif (V2 == 0 and V4 == 0):
        GPIO.output(DIR_PIN1,GPIO.LOW)
        GPIO.output(DIR_PIN2,GPIO.LOW)
        pwm1.ChangeDutyCycle(V1)
        pwm2.ChangeDutyCycle(V3)
    
    elif (V2 == 0 and V3 == 0):
        GPIO.output(DIR_PIN1,GPIO.LOW)
        GPIO.output(DIR_PIN2,GPIO.HIGH)
        pwm1.ChangeDutyCycle(V1)
        pwm2.ChangeDutyCycle(V4)

    elif (V1 == 0 and V4 == 0):
        GPIO.output(DIR_PIN1,GPIO.HIGH)
        GPIO.output(DIR_PIN2,GPIO.LOW)
        pwm1.ChangeDutyCycle(V2)
        pwm2.ChangeDutyCycle(V3)

def listener():
    rospy.init_node('RMotores', anonymous=True) #Tells rospy the name of this node
    rospy.Subscriber("joystick_topic", String, callback) #Declares that the node subscrbes to the 'joystick_topic' topic whose message type is String. 'callback' function is invoked when messages are received
    rospy.spin() #Keeps the node from exiting until the node has been shutdown.

#Checks if this module has been imported
if __name__ == '__main__':
    listener() #Invokes listener function
