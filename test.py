import time
import RPi.GPIO as GPIO

#Relai 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(17, GPIO.LOW)
for i in range(6):
    print(i)
    time.sleep(1)
GPIO.setup(17, GPIO.HIGH)

#27
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(27, GPIO.LOW)
for i in range(6):
    print(i)
    time.sleep(1)
GPIO.setup(27, GPIO.HIGH)
#22
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(22, GPIO.LOW)
for i in range(6):
    print(i)
    time.sleep(1)
GPIO.setup(22, GPIO.HIGH)
#26
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(26, GPIO.LOW)
for i in range(6):
    print(i)
    time.sleep(1)
GPIO.setup(26, GPIO.HIGH)

exit()
