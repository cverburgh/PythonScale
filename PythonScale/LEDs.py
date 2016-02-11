#import RPi.GPIO as GPIO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

# set default blink speed, in ms
defaultFastBlink = 0.1 
defaultSlowBlink = 0.5 

class Led():
    """ an led(s) """
    fastBlinkDelay = defaultFastBlink
    slowBlinkDelay = defaultSlowBlink

    def __init__(self, pinNumber, pinIsHigh = False):
        GPIO.setup(pinNumber, GPIO.OUT)
        self.pin = pinNumber
        self.pinValue = pinIsHigh       

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        if (pin < 0 or pin > 40): 
            self.__pin = 0
        else: 
            self.__pin = pin
            
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

class Pin():
    """ any old pin """

    def __init__(self, pinNumber, gpioMode, initialpinValue = GPIO.LOW):
        self.pin = pinNumber
        self.mode = gpioMode
        if (gpioMode == GPIO.OUT): self.pinValue = initialpinValue

        #GPIO.setup(self.pin, self.mode)
        #if (self.mode == GPIO.OUT): 
        #    self.pinValue = initialpinValue
        #    GPIO.OUT(self.pin, self.pinValue)

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
        return self.__pinValue;

    @pinValue.setter
    def pinValue(self, pinValue):
        self.__pinValue = pinValue
        GPIO.output(self.pin, self.pinValue)
