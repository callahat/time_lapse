import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(47, GPIO.OUT)

# BCM pins, connected to the 8 switch DIP switch
# Below are the switches in order 1-8, and which BCM pin
# they connect to
MINUTE  = 25
HOUR    = 24
DAY     = 23

INVERSE = 16 

TWO_1   =  6
TWO_2   = 22
THREE   = 27
FIVE    = 17

# GPIO for the start button
START_BTN = 26

# GPIO to use the last folder instead of creating a new one
REUSE_FOLDER = 4

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
GPIO.setup(REUSE_FOLDER, GPIO.IN, GPIO.PUD_DOWN)
