import ptvsd
# for VS debugging
ptvsd.enable_attach('piscale')
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import sys
import LedConfig as leds
import ButtonConfig as btns
import LcdStuff as lcd

import ScaleSerial as mySerial
import ApiAccess as webApi
import json
from io import StringIO
from PartWeightResult import PartWeightResult as pwr
import GeneralSetup

readyText = "PiScale started,    waiting for data"
testingMode = True

try:
    #while (btns.btnExit.pinValue == GPIO.LOW): #exit by pressing the ack button
    while (True):   #exit by pressing the Exit button
        # .getData returns the PartWeightResult object
        pw = mySerial.getData(testingMode)

        # no data from scale, keep on truckin' 
        if (pw.hasData == False): continue
    
        lcd.addTextToBottom("Received data:")

        # Data from scale
        # data is good
        if (pw.success):
            #leds.goLed.turnOn()
            lcd.clearText()
            lcd.addTextToBottom("WO: " + pw.workOrderNumber)
            lcd.addTextToBottom("Weight: " + pw.weight)

            # send data to webApi and get the result
            lcd.addTextToBottom("Submitting data...", True)

            apiResult = webApi.SubmitWeight(pw.workOrderNumber, pw.weight, testingMode)

            # some error occured, but it was (probably already handled, 
            # so just get on with things
            if (apiResult == None): 
                lcd.setText(readyText)
                continue


            if (apiResult.status != 200):
                lcd.addTextToBottom("Invalid Request!!", True)
                lcd.addTextToBottom("Error: " + str(apiResult.status), True)

            else:
                apiData = apiResult.data
                lcd.addTextToBottom("Status: " + str(apiResult.status))
            
                if (testingMode):
                    sc = "SOME STOCKCODE"
                else:
                    #jsonData = json.loads(apiData)
                    jsonData = json.load(StringIO(apiData))
                    sc = jsonData['model']['comtekStockCode']

                lcd.setText("Weight submitted", "for stock code", sc)
                leds.goLed.turnOn()
                time.sleep(10)
                leds.goLed.turnOff()

        else:
            # failed to properly read data
            if(pw.hasData): 
                lcd.setText(pw.msg)
                leds.blinkNoGoLeds();

        lcd.setText(readyText)
        leds.statusLed.turnOn()
        time.sleep(0.1)
        
        continue

    GeneralSetup.exitPiScale()

except KeyboardInterrupt:  
    GeneralSetup.exitPiScale()

except Exception as e:
    lcd.setText(e.args[0])
    leds.blinkNoGoLeds()

finally:
    pass
