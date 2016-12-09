import time
import os

from picamera import PiCamera
from time import sleep

import RPi.GPIO as GPIO

c = PiCamera()
c.rotation = 90

GPIO.setmode(GPIO.BCM)
GPIO.setup(47, GPIO.OUT)

ACT_OFF = 1
ACT_ON  = 0

SECONDS_TO_SLEEP = 60
IMAGE_FOLDER = '/home/pi/lapse_{:s}'.format(time.strftime("%Y-%m-%d_%H-%M-%S"))

if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

while(True):
    # blink the ACT led on the board
    start = time.time()
    image_file = 'image_{:s}.jpg'.format(time.strftime("%Y-%m-%d_%H-%M-%S"))
    GPIO.output(47,ACT_ON)
    sleep(1)
    GPIO.output(47,ACT_OFF)
    c.capture( os.path.join(IMAGE_FOLDER, image_file) )
    sleep(SECONDS_TO_SLEEP - (time.time() - start))
