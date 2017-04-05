import time
import os

from picamera import PiCamera
from time import sleep

from pin_config import *

#import RPi.GPIO as GPIO

c = PiCamera()
#c.rotation = 90

c.resolution = (3280,2464)
#c.resolution = (1700,1280)

print("Waiting starting button...")
GPIO.wait_for_edge(26,GPIO.RISING)

print("Start detected")

START_TIME = time.strftime("%Y-%m-%d_%H-%M-%S")
IMAGE_FOLDER = '/home/pi/lapse_project/lapse_{:s}'.format(START_TIME)

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

if GPIO.input(REUSE_FOLDER):
    print("Reusing previous image save directory")
    lapse_folders = []
    for f in os.listdir('/home/pi/lapse_project/'):
        if os.path.isdir(f) and 'lapse' in f:
            lapse_folders.append(f)
    lapse_folders.sort()
    if len(lapse_folders) > 0:
        IMAGE_FOLDER = lapse_folders[-1]

print("image save directory:")
print(IMAGE_FOLDER)

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
    
