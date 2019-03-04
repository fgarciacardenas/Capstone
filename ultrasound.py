#!/usr/bin/env python
# System imports
import RPi.GPIO as GPIO
import sys
import time
# ROS imports
import rospy
from std_msgs.msg import Bool

# Set up IN/OUT pins, location and status
GPIO.setmode(GPIO.BOARD)
PIN_TRIGGER = 7
PIN_ECHO = 11
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)
GPIO.output(PIN_TRIGGER, GPIO.LOW)
time.sleep(0.01)

# This function communicates with the ROS environment and sends ultrasound readings
def talker():
    # Initialize ROSpy communication, establish topic, data type and queue size
    pub=rospy.Publisher('distance_topic',Bool,queue_size=10)
    rospy.init_node('ultrasound',anonymous = True)
    
    # While the program is executing, the following script is running
    while not rospy.is_shutdown():
        # Turn on and off the trigger signal in order to calculate the distance
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        # Calculate the time between sending the signal till receiving it
        while GPIO.input(PIN_ECHO)==0:
                pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
                pulse_end_time = time.time()
        
        # Convert time into distance using the speed of the sound wave
        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)

        # Alert the system if an object is closer than 20 centimeters
        if distance < 20:
                pub.publish(1)
        else:
                pub.publish(0)

        time.sleep(.3)

# Initialize the code with talker() and, if the program is closed, clean up GPIO configuration
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        GPIO.cleanup()
        pass
