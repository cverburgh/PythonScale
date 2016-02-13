import LED as led
from time import sleep
# setup IO pins
#import RPi.GPIO as GPIO
#import time

fastBlinkDelay = 0.1
slowBlinkDelay = 0.5
        
# setup LEDs
statusLed = led.Led(16, True)      # status LED    w/29
goLed     = led.Led(17, False)     # Go
noGoLed1  = led.Led(18, False)     # NoGo 1
noGoLed2  = led.Led(19, False)     # NoGo 2
noGoLed3  = led.Led(20, False)     # NoGo 3

noGoLeds = [noGoLed1, noGoLed2, noGoLed3]
allLeds = [statusLed, goLed, noGoLed1, noGoLed2, noGoLed3]


def fastBlink(led, condition):
    while (condition == True):
        led.turnOn()
        time.sleep(slowBlinkDelay)
        led.turnOff()
        time.sleep(slowBlinkDelay)


def cycleLeds(ledArray, delay = 100):
    turnOffLeds(ledArray)
    for x in range(0, 5):
        for i in range(0, len(ledArray)):
            currentLed = ledArray[i]
            if (i == 0):
                prevLed = ledArray[len(ledArray)-1]
            else:
                prevLed = ledArray[i-1]

            prevLed.turnOff()
            currentLed.turnOn()
    
            delayMs(delay)

    turnOffLeds(ledArray)

def cycleLeds2(ledArray, delay = 100):
    turnOffLeds(ledArray)
    for x in range(0, 5):
        for i in range(len(ledArray)):
            currentLed = ledArray[i]
            if (i == 0):
                prevLed = ledArray[len(ledArray)-1]
            else:
                prevLed = ledArray[i-1]

            prevLed.turnOff()
            currentLed.turnOn()
    
            delayMs(delay)
            
        # go backwards now
        # but don't use last and first item in the array
        # since those leds will be handled above
        for i in range(len(ledArray)-2, -1, -1):
            currentLed = ledArray[i]
            prevLed = ledArray[i+1]

            prevLed.turnOff()
            if (i > 0): currentLed.turnOn()
    
            delayMs(delay)
        ledArray[1].turnOff
    turnOffLeds(ledArray)

def blinkAll(blinks = 5, delay = 500):
    for x in range(blinks):
        turnOnLeds(allLeds)
        delayMs(delay)
        turnOffLeds(allLeds)
        delayMs(delay)

def turnOffAll():
    turnOffLeds(allLeds)

def turnOffLeds(ledArray):
    for i in range(len(ledArray)):
        ledArray[i].turnOff()
        
def turnOnLeds(ledArray):
    for i in range(len(ledArray)):
        ledArray[i].turnOn()
        
def delayMs(ms):
    seconds = ms / float(1000)  # divide ms by 1 thousand for seconds
    sleep(seconds)
