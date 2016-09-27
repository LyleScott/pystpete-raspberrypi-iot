import time

import RPi.GPIO as GPIO


#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GREEN_LED = 20
RED_LED = 21
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

def loop():
    for i in range(100):
        print(i, i % 2)
        if i % 2 == 0:
            GPIO.output(GREEN_LED, True)
            GPIO.output(RED_LED, False)
        else:
            GPIO.output(GREEN_LED, False)
            GPIO.output(RED_LED, True)
        time.sleep(1)


if __name__ == '__main__':
    try:
        print('Press Ctrl-C to quit.')
        loop()
    finally:
        GPIO.cleanup()
