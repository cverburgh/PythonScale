import RPi.GPIO as GPIO

class Button():
    """description of class"""

    def __init__(self, pinNumber, pullUpDown = None, bounce = 150):
        if (pullUpDown == "pullUp" or pullUpDown == "up"):     pullUpDown = GPIO.PUD_UP
        if (pullUpDown == "pullDown" or pullUpDown == "down"): pullUpDown = GPIO.PUD_DOWN
        
        GPIO.setup(pinNumber, GPIO.IN, pull_up_down = pullUpDown)
        self.pin = pinNumber

    @property
    def state(self):
        return GPIO.input(self.pin)
    
    @property
    def pinValue(self):
        return GPIO.input(self.pin)