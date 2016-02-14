import RPi.GPIO as GPIO
from Button import Button as btn

# GPIO - buttons
btnAck = btn(4, "pullDown")     # Acknowledge and clear warning
btnExit = btn(5, "pullDown")    # Exit the program
btnSimData = btn(6, "pullDown") # Simulate scale data

#btnShutdown = SetupPin(18, GPIO.OUT, False)

# This button simulates data coming in from the serial port
#btnSimData = leds.Pin(27, GPIO.IN, False) 

