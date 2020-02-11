import time
import RPi.GPIO as GPIO

GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
while 1:
    # Eingang lesen
    if GPIO.input(11) == GPIO.HIGH:
        print( "Eingang HIGH 11")
        #logic when button pressed
