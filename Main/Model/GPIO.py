import time
import RPi.GPIO as GPIO

vorlaufzeit = 1
volumenpersek = 0.1

def acessPort(port, menge):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(port, GPIO.OUT)
    GPIO.setup(port, GPIO.LOW)
    zeit = vorlaufzeit + (menge * volumenpersek)
    print(zeit)
    time.sleep(zeit)
    GPIO.setup(port, GPIO.HIGH)

