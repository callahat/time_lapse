import time
import os

from picamera import PiCamera
from time import sleep

import RPi.GPIO as GPIO

c = PiCamera()
#c.rotation = 90

GPIO.setmode(GPIO.BCM)
GPIO.setup(47, GPIO.OUT)

# BCM pins, connected to the 8 switch DIP switch
# Below are the switches in order 1-8, and which BCM pin
# they connect to
MINUTE  = 23
HOUR    = 24
DAY     = 25

INVERSE = 16 

TWO_1   = 17
TWO_2   = 27
THREE   = 22
FIVE    =  6

# GPIO for the start button
START_BTN = 26

# ACT led on/off values
ACT_OFF = 1
ACT_ON  = 0

SWITCH_ON  = 1
SWITCH_OFF = 0

# Setup GPIO
GPIO.setup(START_BTN, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(MINUTE, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(HOUR, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(DAY, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(INVERSE, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(TWO_1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(TWO_2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(THREE, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(FIVE, GPIO.IN, GPIO.PUD_DOWN)


print("Waiting starting button...")
GPIO.wait_for_edge(26,GPIO.RISING)

START_TIME = time.strftime("%Y-%m-%d_%H-%M-%S")
IMAGE_FOLDER = '/home/pi/lapse_project/lapse_{:s}'.format(START_TIME)

# Base interval between pictures,
# One day, one hour, one minute (in seconds)
if GPIO.input(DAY) == SWITCH_ON:
    SECONDS_TO_SLEEP = 24 * 60 * 60
elif GPIO.input(HOUR) == SWITCH_ON:
    SECONDS_TO_SLEEP = 60 * 60
elif GPIO.input(MINUTE) == SWITCH_ON:
    SECONDS_TO_SLEEP = 60

MODIFIER = 1

# Multipliers from the other switches
if GPIO.input(TWO_1) == SWITCH_ON:
    MODIFIER *= 2
if GPIO.input(TWO_2) == SWITCH_ON:
    MODIFIER *= 2
if GPIO.input(THREE) == SWITCH_ON:
    MODIFIER *= 3
if GPIO.input(FIVE) == SWITCH_ON:
    MODIFIER *= 5

# Invert the modifier
if GPIO.input(INVERSE) == SWITCH_ON:
    MODIFIER = 1 / MODIFIER

# Sleep more or less than the base interval
SECONDS_TO_SLEEP *= MODIFIER

print("Start detected")
print("image save directory:")
print(START_TIME)

print("Sleeping {:.0f} seconds between captures".format(SECONDS_TO_SLEEP))


if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

while(True):
    sleep_time = SECONDS_TO_SLEEP - time.time() % SECONDS_TO_SLEEP
    sleep(sleep_time)
    image_file = 'image_{:s}.jpg'.format(time.strftime("%Y-%m-%d_%H-%M-%S"))
    # blink the ACT led on the board
    GPIO.output(47,ACT_ON)
    sleep(1)
    GPIO.output(47,ACT_OFF)
    c.capture( os.path.join(IMAGE_FOLDER, image_file) )
    
