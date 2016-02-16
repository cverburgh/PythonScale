import RPi.GPIO as GPIO
import LedConfig as leds
import ButtonConfig as btns
import LcdStuff as lcd

def exitPiScale():
    lcd.setText("Exiting PiScale", "Goodbye!")
    GPIO.cleanup()
    import sys
    sys.exit()


def restart():
    import os
    os.system('shutdown -r now')

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