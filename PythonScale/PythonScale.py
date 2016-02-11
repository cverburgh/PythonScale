import time
import RPi.GPIO as GPIO
import Setup as myio
import ptvsd
ptvsd.enable_attach('piscale')

GPIO.setmode(GPIO.BOARD)

myio.noLed.turnOn()

for i in range (0, 10):
    myio.statusLed.turnOn()
    time.sleep(myio.fastBlinkDelay)
    myio.statusLed.turnOff()
    time.sleep(myio.fastBlinkDelay)

myio.noLed.turnOff()

myio.fastBlink(myio.statusLed, myio.keepFlashing)

myio.noLed.turnOn()


GPIO.cleanup()

#while (true):
    
