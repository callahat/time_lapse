import time
import os

from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(47, GPIO.OUT)

ACT_OFF = 1
ACT_ON  = 0

SECONDS_TO_SLEEP = 1

while(True):
    # blink the ACT led on the board
    start = time.time()
    GPIO.output(47,ACT_ON)
    sleep(0.1)
    GPIO.output(47,ACT_OFF)
    # Sleeps until the next increment of time
    sleep_time = SECONDS_TO_SLEEP - time.time() % SECONDS_TO_SLEEP
    sleep(sleep_time)
    print('{:f} - slept: {:f}'.format(time.time(), sleep_time))
