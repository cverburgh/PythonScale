import RPi.GPIO as GPIO

class Pin():
    """ any old pin """
    def __init__(self, pinNumber, gpioMode, initialpinValue = GPIO.LOW):
        self.pin = pinNumber
        self.mode = gpioMode
        if (gpioMode == GPIO.OUT): self.pinValue = initialpinValue


    @property
    def pin(self): return self.__pin

    @pin.setter
    def pin(self, pin):
        if (pin < 0 or pin > 40): 
            self.__pin = 0
        else: 
            self.__pin = pin


    @property
    def mode(self): return self.__mode

    @mode.setter
    def mode(self, mode):
        self.__mode = mode
        GPIO.setup(self.pin, self.mode)

    @property
    def pinValue(self):
        self.__pinValue = GPIO.input(self.__pin)
        return self.__pinValue;

    @pinValue.setter
    def pinValue(self, pinValue):
        self.__pinValue = pinValue
        GPIO.output(self.pin, self.pinValue)
