import time

from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(47, GPIO.OUT)

ACT_OFF = 1
ACT_ON  = 0

while(True):
    GPIO.output(47,ACT_OFF)
    sleep(1)
    GPIO.output(47,ACT_ON)
    sleep(2)
