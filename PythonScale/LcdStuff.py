from Adafruit_CharLCD import Adafruit_CharLCD as afLcd

lcd = afLcd()
lcd.begin(20,4)
lcd.clear()
lcdText = ["", "", "", ""]


def clearText():
    lcdText = ["", "", "", ""]
    lcd.clear()

def setText(line0 = "", line1 = "", line2 = "", line3 = ""):
    lcdText[0] = line0
    lcdText[1] = line1
    lcdText[2] = line2
    lcdText[3] = line3

    lcd.messages(lcdText)

def addTextToTop(text, update = False):
    # add to top, lose the bottom
    lcdText[3] = lcdText[2]
    lcdText[2] = lcdText[1]
    lcdText[1] = lcdText[0]
    lcdText[0] = text

    lcd.messages(lcdText)
    if (update): lcd.messages(lcdText)

def addTextToBottom(text, update = False):
    # add to bottom, lose the first line
    lcdText[0] = lcdText[1]
    lcdText[1] = lcdText[2]
    lcdText[2] = lcdText[3]
    lcdText[3] = text

    if (update): lcd.messages(lcdText)
