import time
import os

from picamera import PiCamera
from time import sleep

from pin_config import *
from reuse_folder import imageFolder

#import RPi.GPIO as GPIO

c = PiCamera()
#c.rotation = 90

c.resolution = (3280,2464)
#c.resolution = (1700,1280)

sleep(1)

if GPIO.input(26) == SWITCH_ON:
    print("Detected start switch")
else:
    print("Waiting starting button...")
    GPIO.wait_for_edge(26,GPIO.RISING)

print("Start detected")

IMAGE_FOLDER = imageFolder(GPIO.input(REUSE_FOLDER))

if not os.path.exists(IMAGE_FOLDER):
    print("Image folder not found, creating it.")
    os.makedirs(IMAGE_FOLDER)

# Base interval between pictures,
# One day, one hour, one minute (in seconds)
if GPIO.input(DAY) == SWITCH_ON:
    SECONDS_TO_SLEEP = 24 * 60 * 60
elif GPIO.input(HOUR) == SWITCH_ON:
    SECONDS_TO_SLEEP = 60 * 60
else: # GPIO.input(MINUTE) == SWITCH_ON:
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
    MODIFIER = 1.0 / MODIFIER

# Sleep more or less than the base interval
SECONDS_TO_SLEEP *= MODIFIER

print("Sleeping {:.0f} seconds between captures".format(SECONDS_TO_SLEEP))

while(True):
    sleep_time = SECONDS_TO_SLEEP - time.time() % SECONDS_TO_SLEEP
    sleep(sleep_time)
    image_file = 'image_{:s}.jpg'.format(time.strftime("%Y-%m-%d_%H-%M-%S"))
    # blink the ACT led on the board
    GPIO.output(47,ACT_ON)
    sleep(1)
    GPIO.output(47,ACT_OFF)
    c.capture( os.path.join(IMAGE_FOLDER, image_file) )
    
