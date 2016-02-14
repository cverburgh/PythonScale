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

def doExitStuff():
    lcd.setText("Exiting PiScale")

try:
    while (btns.btnExit.pinValue == GPIO.LOW): #exit by pressing the ack button
    #while (True): #exit by pressing the ack button
        time.sleep(0.1)
        leds.turnOffAll()
        leds.statusLed.turnOn()
    
        # .getData returns the PartWeightResult object
        pw = mySerial.getData(testingMode = True)

        # no data from scale, keep on truckin' 
        if (pw.hasData == False): continue
    
        lcd.addTextToBottom("Received data:")

        # Data from scale
        # data is good
        if (pw.success):
            leds.goLed.turnOn()
            lcd.clearText()
            lcd.addTextToBottom("WO: " + pw.workOrderNumber)
            lcd.addTextToBottom("Weight: " + pw.weight)

            # send data to webApi and get the result
            lcd.addTextToBottom("Submitting data...")
            apiResult = webApi.SubmitWeight(pw.workOrderNumber, pw.weight)

            if (apiResult.status != 200):
                lcd.addTextToBottom("Invalid Request!!", True)
                lcd.addTextToBottom("Error: " + str(apiResult.status), True)

            else:
                lcd.addTextToBottom("weight submitted!")
                apiData = apiResult.data
                lcd.addTextToBottom("Status: " + str(apiResult.status))
            
                #jsonData = json.loads(result.data)
                jsonData = json.load(StringIO(apiData))
                sc = jsonData['model']['comtekStockCode']
                lcd.addTextToBottom(sc, True)
            
        else:
            # failed to properly read data
            if(pw.hasData): 
                leds.noGoLed.turnOn();
                lcd.addTextToBottom("ERROR:")
                lcd.addTextToBottom(pw.msg)

        continue


    doExitStuff()

except KeyboardInterrupt:  
    pass

except Exception as e:
    lcd.addTextToBottom("A error has occured:" )
    lcd.addTextToBottom(e)

finally:
    GPIO.cleanup()
