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
                lcd.setText("release button to", "resume part weight", "continue to hold for", "more options")
                a = True
        if (x >= 5 and x < 10): 
            if (b == False):
                a = False
                lcd.setText("release button to", "restart", "continue to hold for", "more options")
                b = True

        if (x >= 10 and x < 15):
            if (c == False):
                b = False
                lcd.setText("release button to", "shutdown", "continue to hold for", "more options")
                c = True
        if (x >= 15):
            lcd.setText("system ready", "  ",  "You can release", "the button now!")
            a = True
            b = False
            c = False           

    if (a): 
        lcd.setText("system ready")
    else:
        if (b): 
            lcd.setText("rebooting")
            GPIO.cleanup()
            reboot()
        if (c): 
            lcd.setText("shutting down...")
            halt()


def reboot():
    import os
    os.system("sudo reboot now")

def halt():
    import os
    os.system("sudo halt now")


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
