# setup IO pins
import RPi.GPIO as GPIO
import LEDs as leds

# setup LEDs
statusLed = SetupLed(29, defaultFastBlink, defaultFastBlink, 0, GPIO.OUTPUT)             # status LED
noLed = SetupLed(31, defaultFastBlink, defaultFastBlink, 0, GPIO.OUTPUT)                 # Go
noGoLed = SetupLed(32, defaultFastBlink, defaultFastBlink, 0, GPIO.OUTPUT)               # NoGo

# Setup GPIO
# GPIO - LCD
lcdRegSelect = SetupPin(33, GPIO.OUTPUT, GPIO.LOW)
lcdClockEnable = SetupPin(35, GPIO.OUTPUT, GPIO.LOW)
lcdData4 = SetupPin(36, GPIO.OUTPUT, GPIO.LOW)
lcdData5 = SetupPin(37, GPIO.OUTPUT, GPIO.LOW)
lcdData6 = SetupPin(38, GPIO.OUTPUT, GPIO.LOW)
lcdData7 = SetupPin(40, GPIO.OUTPUT, GPIO.LOW)

# GPIO - buttons
btnAck = SetupPin(32, GPIO.OUTPUT, GPIO.LOW)
btnShutdown = SetupPin(31, GPIO.OUTPUT, GPIO.LOW)

def SetupLed(pin, fastBlinkDelay, slowBlinkDelay, initialState):
    ledObject = leds.Led()
    ledObject.pin = pin
    ledObject.fastBlinkDelay = fastBlinkDelay
    ledObject.slowBlinkDelay = slowBlinkDelay
    ledObject.state = initialState

    GPIO.setup(ledObject.pin, GPIO.OUT)
    GPIO.output(ledObject.pin, initialState)

    return ledObject

def SetupPin(pin, mode, initialState):
    pinObject = leds.Pin()
    pinObject.pin = pin,
    pinObject.mode = mode
    pinObject.state = initialState
    
    GPIO.setup(pinObject.pin, mode)
    if (pinObject.mode == GPIO.OUTPUT): GPIO.output(pinObject.pin, initialState)

    return pinObject