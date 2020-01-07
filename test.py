import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.Out)
GPIO.setup(17, GPIO.HIGH)
for i in range(10):
    time.sleep(1)
GPIO.setup(17, GPIO.LOW)
