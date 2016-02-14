import RPi.GPIO as GPIO
import LedConfig as leds
import ButtonConfig as btns
import LcdStuff as lcd

def exitPiScale(self):
    lcd.setText("Exiting PiScale", "Goodbye!")
    exit()

#GPIO.add_event_detect(btns.btnExit.pin, GPIO.RISING, callback = exitPiScale, bouncetime = 150)

try:
    lcd.setText("Starting up...")
    #leds.slowBlink(leds.statusLed, 10)
    leds.statusLed.turnOn()
    lcd.setText("PiScale started, ", "waiting for data", "", "")

except Exception as e:
    lcd.setText("Error:", e)

finally:
    pass