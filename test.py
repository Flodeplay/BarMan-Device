import time
import RPi.GPIO as GPIO

#Relai 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(17, GPIO.LOW)
for i in range(3):
    print(i)
    time.sleep(1)
GPIO.setup(17, GPIO.HIGH)

#27
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(27, GPIO.LOW)
for i in range(3):
    print(i)
    time.sleep(1)
GPIO.setup(27, GPIO.HIGH)
#22
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(22, GPIO.LOW)
for i in range(3):
    print(i)
    time.sleep(1)
GPIO.setup(22, GPIO.HIGH)
#23
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(23, GPIO.LOW)
for i in range(3):
    print(i)
    time.sleep(1)
GPIO.setup(23, GPIO.HIGH)

exit()
