import time
import RPi.GPIO as GPIO
import Setup as myio
import ScaleSerial as mySerial
import ptvsd
import random
import ApiAccess as webApi
import json
from io import StringIO
import LCd

LCd.main

ptvsd.enable_attach('piscale')

GPIO.setmode(GPIO.BOARD)

#myio.noLed.turnOn()
myio.statusLed.turnOn()

counter=0;

while (myio.btnAck.pinValue == GPIO.LOW): #exit by pressing the ack button
    time.sleep(0.25)    
    myio.goLed.turnOff();
    myio.noGoLed.turnOff();

    rndm = random.random()
    data = mySerial.ser.readline()
    
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

            result = webApi.SubmitWeight(workOrderNumber, weight)

            if (result.status != 200):
                print("Bad data returned!!")
            else:
                data = result.data

                #jsonData = json.loads(result.data)
                jsonData = json.load(StringIO(data))
                print(jsonData['ip'])

    else:
        print("looking for data...")

    counter += 1


GPIO.cleanup()

#while (true):
    
