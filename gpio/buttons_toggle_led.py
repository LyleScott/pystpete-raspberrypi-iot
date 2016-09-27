# Adapted from:
# https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/code
import os
from time import sleep
 
import RPi.GPIO as GPIO

 
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

GREEN_LED = 20
BLUE_LED = 21
GPIO.setup(BLUE_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
 
try:
    while True:
        b1 = GPIO.input(23)
        b2 = GPIO.input(24)
        b3 = GPIO.input(25)
   
        if not b1:
            print('1')
            GPIO.output(BLUE_LED, True)
        else:
            GPIO.output(BLUE_LED, False)

        if not b2:
            print('2')
            GPIO.output(GREEN_LED, True)
        else:
            GPIO.output(GREEN_LED, False)
 
        if not b3:
            print('3')
            GPIO.output(GREEN_LED, True)
            GPIO.output(BLUE_LED, True)
 
        sleep(.1)
finally:
    GPIO.cleanup()
