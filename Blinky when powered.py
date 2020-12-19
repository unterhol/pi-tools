import RPi.GPIO as gpio
import time
gpio.setwarnings (False)
gpio.setmode(gpio.BCM)
gpio.setup(6,gpio.OUT)
gpio.setup(13,gpio.OUT)
gpio.setup(19,gpio.OUT)
gpio.setup(26,gpio.OUT)
gpio.setup(12,gpio.OUT)
gpio.setup(16,gpio.OUT)
gpio.setup(20,gpio.OUT)
gpio.setup(21,gpio.OUT)
gpio.setup(17,gpio.IN)
y=gpio.input(17)
X=X
while True:
    if y:
        x+1
    print (y)
    print (x)
