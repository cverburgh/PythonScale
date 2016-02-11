﻿# setup IO pins
import LEDs as leds
import RPi.GPIO as GPIO
import time

fastBlinkDelay = 0.1
slowBlinkDelay = 0.5

# setup LEDs
statusLed = leds.Led(29, True)              # status LED
goLed = leds.Led(31, False)                 # Go
noGoLed = leds.Led(32, False)               # NoGo

# Setup GPIO
# GPIO - LCD
lcdRegSelect = leds.Pin(35, GPIO.OUT, False)
lcdClockEnable = leds.Pin(37, GPIO.OUT, False)
lcdData4 = leds.Pin(33, GPIO.OUT, False)
lcdData5 = leds.Pin(36, GPIO.OUT, False)
lcdData6 = leds.Pin(38, GPIO.OUT, False)
lcdData7 = leds.Pin(40, GPIO.OUT, False)

# GPIO - buttons
btnAck = leds.Pin(11, GPIO.IN, False)
#btnShutdown = SetupPin(12, GPIO.OUT, False)
# This button simulates data coming in from the serial port
btnSimData = leds.Pin(13, GPIO.IN, False)

keepFlashing = True;

def fastBlink(led, condition):
    while (condition == True):
        led.turnOn()
        time.sleep(slowBlinkDelay)
        led.turnOff()
        time.sleep(slowBlinkDelay)
        
