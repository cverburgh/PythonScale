
import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import LedConfig as leds
import ButtonConfig as btns
import ScaleSerial as mySerial
import random
import ApiAccess as webApi
import json
from io import StringIO
from PartWeightResult import PartWeightResult as pwr
from Adafruit_CharLCD import Adafruit_CharLCD as afLcd

import ptvsd
# for VS debugging
ptvsd.enable_attach('piscale')

leds.statusLed.turnOn()

leds.cycleLeds(leds.allLeds)
leds.cycleLeds2(leds.allLeds)
leds.blinkAll()

leds.statusLed.turnOn();

lcd = afLcd()
lcd.begin(20,4)
lcd.clear()
lcdText = ["", "", "", ""]

def clearLcdText():
    lcdText = ["", "", "", ""]
    lcd.messages(lcdText)
def setLcdText(line0 = "", line1 = "", line2 = "", line3 = ""):
    lcdText[0] = line0
    lcdText[1] = line1
    lcdText[2] = line2
    lcdText[3] = line3

    lcd.messages(lcdText)
def addLcdTextToTop(text, update = False):
    # add to top, lose the bottom
    lcdText[3] = lcdText[2]
    lcdText[2] = lcdText[1]
    lcdText[1] = lcdText[0]
    lcdText[0] = text

    lcd.messages(lcdText)
    if (update): lcd.messages(lcdText)
def addLcdTextToBottom(text, update = False):
    # add to bottom, lose the first line
    lcdText[0] = lcdText[1]
    lcdText[1] = lcdText[2]
    lcdText[2] = lcdText[3]
    lcdText[3] = text

    if (update): lcd.messages(lcdText)
setLcdText("starting up and", "wating for data...")


while (btns.btnAck.pinValue == GPIO.LOW): #exit by pressing the ack button
    time.sleep(0.1)
    leds.goLed.turnOff();
    leds.noGoLed1.turnOff();
    leds.noGoLed2.turnOff();
    leds.noGoLed3.turnOff();
    rndm = random.random()
    
    # .getData returns the PartWeightResult object
    pw = mySerial.getData()

    # no data from scale, keep on truckin' 
    if (pw.hasData == False): continue
    
    addLcdTextToBottom("Received data:")

    # Data from scale
    # data is good
    if (pw.success):
        myio.goLed.turnOn();
        clearLcdText()
        addLcdTextToBottom("WO: " + pw.workOrderNumber)
        addLcdTextToBottom("Weight: " + pw.weight)

        # send data to webApi and get the result
        addLcdTextToBottom("Submitting data...")
        apiResult = webApi.SubmitWeight(pw.workOrderNumber, pw.weight)

        if (apiResult.status != 200):
            addLcdTextToBottom("Invalid Request!!", True)
            addLcdTextToBottom("Error: " + str(apiResult.status), True)

        else:
            addLcdTextToBottom("weight submitted!")
            apiData = apiResult.data
            addLcdTextToBottom("Status: " + str(apiResult.status))
            
            #jsonData = json.loads(result.data)
            jsonData = json.load(StringIO(apiData))
            sc = jsonData['model']['comtekStockCode']
            addLcdTextToBottom(sc, True)
            
    else:
        # failed to properly read data
        if(pw.hasData): 
            myio.noGoLed.turnOn();
            addLcdTextToBottom("ERROR:")
            addLcdTextToBottom(pw.msg)

    continue

    if (myio.btnSimData.pinValue == GPIO.HIGH): 
        data = "00198454 0.164KG"
        print(rndm)
        print("found some data: ")
        print(data)

        if (rndm > 0.5):
            # pretend it's bad data
            myio.noGoLed.turnOn();
            print("**************** WARNING ****************")
            print("bad data!!")
            print("**************** WARNING ****************")
        else:
            # pretend it's good data
            workOrderNumber = "00198454"
            weight = "2.345"
            myio.goLed.turnOn();
            print("good data")
            print("submitting weight...")
    else: print("looking for data...")


# end of while loop
lcd.clear()
lcd.message("exiting PiScale")
GPIO.cleanup()

#while (true):
    
