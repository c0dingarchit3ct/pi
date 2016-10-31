import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
print (gpio.BOARD)
gpio.setup(21,gpio.OUT)
gpio.setup(19,gpio.OUT)
gpio.setup(23,gpio.OUT)

blinktime=.1
def blink (gpio_no,sl):
    gpio.output(gpio_no,True)
    time.sleep(sl)
    gpio.output(gpio_no,False)
blink(19,blinktime)
for x in range(0,15) :
    blink(21,blinktime)
    blink(23,blinktime)
    blink(21,blinktime)
    blink(19,blinktime)

gpio.cleanup()
