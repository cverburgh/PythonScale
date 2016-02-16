import RPi.GPIO as GPIO
import LedConfig as leds
import ButtonConfig as btns
import LcdStuff as lcd
import sys
import time

pressAckMsg = "Press ACK to cont."

def exitPiScale(args):
    global time_stamp
    a=False
    b=False
    c=False

    x=0
    while(btns.btnExit.state == GPIO.HIGH):
        time.sleep(0.1)
        x = x + 0.1
        if (x < 5):
            if (a== False):
                lcd.setText("release button to", "reboot", "continue to hold for", "more options")
                a = True
        if (x >= 5 and x < 10): 
            if (b == False):
                a = False
                lcd.setText("release button to", "shutdown", "continue to hold for", "more options")
                b = True
            #halt()

        if (x >= 10):
            if (c == False):
                b = False
                lcd.setText("release button to", "resume part weight", "continue to hold for", "more options")
                c = True
        
    if (a): 
        lcd.setText("rebooting")
        GPIO.cleanup()
        reboot()
    else:
        if (b): 
            lcd.setText("shutting down")
            GPIO.cleanup()
            halt()
        else: 
            lcd.setText("System ready...")


def reboot():
    import os
    os.system("sudo reboot")

def halt():
    import os
    os.system("sudo halt")


# setup the button to exit
# when a rising edge is detected on the Exit button pin, regardless of whatever   
# else is happening in the program, the exitPiScale function will be called
GPIO.add_event_detect(btns.btnExit.pin, GPIO.RISING, callback=exitPiScale, bouncetime=150)  

    
try:
    lcd.setText("PiScale started, ", "waiting for data", "", "")
    leds.statusLed.turnOn()

except Exception as e:
    lcd.setText(e)

finally:
    pass