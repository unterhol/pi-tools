import RPi.GPIO as GPIO
import time

GPIO.setwarnings (False)
GPIO.setmode (GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

def getInput(pin):
    return GPIO.input(pin)

def setOn(duration):
    setLed(True, duration)

def setOff(duration):
    setLed(False, duration)
    
def setLed(ooo, duration):
    GPIO.output(18 , ooo)
    time.sleep(duration)
    return;


while True :
    if getInput(25):
        setOff(.01)
    else:
        setOn(.01)
    
    
    
    
    
