import RPi.GPIO as GPIO

class Led():
    """ an led(s) """

    def __init__(self, pinNumber, pinIsHigh = False):
        GPIO.setup(pinNumber, GPIO.OUT)
        self.pin = pinNumber
        self.pinValue = pinIsHigh       

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin
        #if (pin < 0 or pin > 40): 
        #    self.__pin = 0
        #else: 
            
            
    @property
    def pinValue(self):
        self.__pinValue == GPIO.input(self.pin)
        return self.__pinValue

    @pinValue.setter
    def pinValue(self, pinValue):
        self.__pinValue = pinValue
        GPIO.output(self.pin, self.pinValue)
        
    def turnOn(self): self.pinValue = True
    def turnOff(self): self.pinValue = False

    def isOn(self): return GPIO.input(self.pin) == GPIO.HIGH
