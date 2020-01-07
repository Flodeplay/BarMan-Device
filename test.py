import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(17, GPIO.LOW)
for i in range(10):
    print(i)
    time.sleep(1)
GPIO.setup(17, GPIO.HIGH)
exit()

