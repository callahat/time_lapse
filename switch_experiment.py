import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, GPIO.PUD_DOWN)

GPIO.setup(23, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.IN, GPIO.PUD_DOWN)

print("Waiting for input")

while(True):
    GPIO.wait_for_edge(26,GPIO.RISING)
    print("Button pushed")
    print("Switches:")
    print("1:{:b} 2:{:b} 3:{:b}".format(GPIO.input(23), GPIO.input(24), GPIO.input(25)))

GPIO.cleanup()
