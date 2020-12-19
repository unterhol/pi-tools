import RPi.GPIO as gpio
import time
gpio.setwarnings (False)
gpio.setmode(gpio.BCM)
gpio.setup(2, gpio.OUT)
gpio.setup(4, gpio.IN)
var1= gpio.input(4)
while True:
    time.sleep(0.25)
    var1= gpio.input(4)
    print (var1)
    if (var1==gpio.HIGH):
         gpio.output(2, gpio.LOW)
         time.sleep(1)
         gpio.output(2, gpio.HIGH)
         time.sleep(1)
    else:
        gpio.output(2, gpio.LOW)
        
