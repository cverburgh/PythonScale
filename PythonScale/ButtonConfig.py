import RPi.GPIO as GPIO
from Button import Button as btn

# GPIO - buttons
btnAck = btn(4, "pullDown")
btnReset = btn(5, "pullDown")
#btnShutdown = SetupPin(18, GPIO.OUT, False)

# This button simulates data coming in from the serial port
#btnSimData = leds.Pin(27, GPIO.IN, False) 

