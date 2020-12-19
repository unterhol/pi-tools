import RPi.GPIO as GPIO
import time

GPIO.setwarnings (False)
GPIO.setmode (GPIO.BCM)
GPIO.setup(18, GPIO. OUT)

def setOn(duration):
    setLed(True, duration)

def setOff(duration):
    setLed(False, duration)
    
def setLed(ooo, duration):
    GPIO.output(18 , ooo)
    time.sleep(duration)
    return;


while True :
    setOn(.1)
    setOff(.1)
    setOn(2)
    setOff(3)
    setOn(.1)
    setOn(7)
    setOff(4)
    
    
    
    
    
