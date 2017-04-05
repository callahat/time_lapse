from time import sleep
from pin_config import *

print("Waiting for input")

while(True):
    print("switch status")
    print("Button: {:b}".format(GPIO.input(START_BTN)))
    
    print("MINUTE: {:b}".format(GPIO.input(MINUTE)))
    print("HOUR:   {:b}".format(GPIO.input(HOUR)))
    print("DAY:    {:b}".format(GPIO.input(DAY)))
    
    print("INVERSE:{:b}".format(GPIO.input(INVERSE)))
    
    print("TWO_1:  {:b}".format(GPIO.input(TWO_1)))
    print("TWO_2:  {:b}".format(GPIO.input(TWO_2)))
    print("THREE:  {:b}".format(GPIO.input(THREE)))
    print("FIVE:   {:b}".format(GPIO.input(FIVE)))
    
    print("REUSE_FOLDER:{:b}".format(GPIO.input(REUSE_FOLDER)))
    junk = input('Hit enter to continue')


GPIO.cleanup()
