import RPi.GPIO as GPIO
import GenericPinConfig as pin

# GPIO - buttons
btnAck = pin.Pin(4, GPIO.IN, False)            # w/11

#btnShutdown = SetupPin(18, GPIO.OUT, False)    # w/12

# This button simulates data coming in from the serial port
#btnSimData = leds.Pin(27, GPIO.IN, False)      # w/13

