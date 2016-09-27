# Adapted from:
# https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/code
import os
from time import sleep
 
import RPi.GPIO as GPIO

 
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
 
while True:
    if GPIO.input(23) == False:
        print(1)
 
    if GPIO.input(24) == False:
        print('2')
 
    if GPIO.input(25) == False:
        print('3')
 
    sleep(.1)
