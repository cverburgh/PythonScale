from time import sleep
import RPi.GPIO as GPIO

def cycleNoGoLeds(noGoLed1, noGoLed2, noGoLed3, delay = 100):
    turnOffNoGoLeds(noGoLed1, noGoLed2, noGoLed3)
    for i in range(0, 20):
        noGoLed3.turnOff()
        noGoLed1.turnOn()
    
        delayMs(delay)

        noGoLed1.turnOff()
        noGoLed2.turnOn()
    
        delayMs(delay)

        noGoLed2.turnOff()
        noGoLed3.turnOn()

        delayMs(delay)


def cycleNoGoLeds2(noGoLed1, noGoLed2, noGoLed3, delay = 100):
    turnOffNoGoLeds(noGoLed1, noGoLed2, noGoLed3)
    for i in range(0, 20):
        noGoLed3.turnOff()
        noGoLed1.turnOn()
    
        delayMs(delay)

        noGoLed1.turnOff()
        noGoLed2.turnOn()
    
        delayMs(delay)

        noGoLed2.turnOff()
        noGoLed3.turnOn()

        delayMs(delay)

        noGoLed3.turnOff()
        noGoLed2.turnOn()

        delayMs(delay)

        noGoLed2.turnOff()


def turnOffNoGoLeds(noGoLed1, noGoLed2, noGoLed3):
    noGoLed1.turnOff()
    noGoLed2.turnOff()
    noGoLed3.turnOff()


def turnOnNoGoLeds(noGoLed1, noGoLed2, noGoLed3):
    noGoLed1.turnOn()
    noGoLed2.turnOn()
    noGoLed3.turnOn()


def delayMs(ms):
    seconds = ms / float(1000)  # divide ms by 1 thousand for seconds
    sleep(seconds)
