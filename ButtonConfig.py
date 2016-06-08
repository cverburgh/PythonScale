import RPi.GPIO as GPIO
from Button import Button as btn
import Testing as test

# GPIO - buttons
ackPin = 17
exitPin = 27
simPin = 22

if (test.mode == True):
    # swap the testing/exit buttons
    exitPin = 22
    simPin = 27


   
btnAck = btn(ackPin, "pullDown")     # 17 Acknowledge and clear warning
btnExit = btn(exitPin, "pullDown")    # 27 Exit the program
btnSimData = btn(simPin, "pullDown") # 22 Simulate scale data

#btnShutdown = SetupPin(18, GPIO.OUT, False)

# This button simulates data coming in from the serial port
#btnSimData = leds.Pin(27, GPIO.IN, False) 

