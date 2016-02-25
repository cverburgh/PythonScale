import RPi.GPIO as GPIO
from Button import Button as btn

# GPIO - buttons
btnAck = btn(17, "pullDown")     # Acknowledge and clear warning
btnExit = btn(27, "pullDown")    # Exit the program
btnSimData = btn(22, "pullDown") # Simulate scale data

#btnShutdown = SetupPin(18, GPIO.OUT, False)

# This button simulates data coming in from the serial port
#btnSimData = leds.Pin(27, GPIO.IN, False) 

