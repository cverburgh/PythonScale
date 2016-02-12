# setup IO pins
import LEDs as leds
import RPi.GPIO as GPIO
import time

fastBlinkDelay = 0.1
slowBlinkDelay = 0.5

# setup LEDs
statusLed = leds.Led(5, True)              # status LED    w/29
goLed = leds.Led(6, False)                 # Go            w/31
noGoLed = leds.Led(12, False)              # NoGo          w/32

# Setup GPIO
# GPIO - LCD
#lcdRegSelect = leds.Pin(19, GPIO.OUT, False)    # w/35
#lcdClockEnable = leds.Pin(26, GPIO.OUT, False)  # w/37
#lcdData4 = leds.Pin(13, GPIO.OUT, False)        # w/33
#lcdData5 = leds.Pin(16, GPIO.OUT, False)        # w/36
#lcdData6 = leds.Pin(20, GPIO.OUT, False)        # w/38
#lcdData7 = leds.Pin(21, GPIO.OUT, False)        # w/40

# GPIO - buttons
btnAck = leds.Pin(17, GPIO.IN, False)           # w/11
#btnShutdown = SetupPin(18, GPIO.OUT, False)    # w/12
# This button simulates data coming in from the serial port
btnSimData = leds.Pin(27, GPIO.IN, False)       # w/13

keepFlashing = True;

def fastBlink(led, condition):
    while (condition == True):
        led.turnOn()
        time.sleep(slowBlinkDelay)
        led.turnOff()
        time.sleep(slowBlinkDelay)
        
