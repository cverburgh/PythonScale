import Adafruit_CharLCD as LCD
import time


'pin_rs': 25,
'pin_e': 24,
'pins_db': [23, 20, 21, 22],
'backlight': 18,
'dimensions': [20, 4]


lcd.message('A')
time.sleep(0.5)
lcd.message('B')
time.sleep(0.5)
lcd.message('C')
time.sleep(0.5)
