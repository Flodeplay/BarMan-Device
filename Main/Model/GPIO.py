import time
#import RPi.GPIO as GPIO



def acessPort(port, zeit):
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(port, GPIO.OUT)
    #GPIO.setup(port, GPIO.LOW)
    print(zeit)
    time.sleep(zeit)
    #GPIO.setup(port, GPIO.HIGH)

def cleanPumps():
    print("to be added")
