import RPi.GPIO as gpio
import time

gpio.setwarnings (False)

gpio.setmode(gpio.BCM)
gpio.setup(2, gpio.OUT)
gpio.setup(3, gpio.IN)

while True:
    if (gpio.input, 3)==True :
         gpio.output(2, gpio.LOW)
         time.sleep(1)
         gpio.output(2, gpio.HIGH)
         time.sleep(1)
    
