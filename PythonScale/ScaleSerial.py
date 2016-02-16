import time
import serial
from PartWeightResult import PartWeightResult as pwr
import unicodedata
import LcdStuff as lcd
import ButtonConfig as btns
import RPi.GPIO as GPIO
import LedConfig as leds

ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

def getData(testingMode):
    try:
        #data = ser.readline()
        if (testingMode == True and btns.btnSimData.state == GPIO.HIGH):
           data = getTestData()
           result = data
        else:
           data = ser.readline()
           result = data.decode(encoding='UTF-8')
        
        # result should be a string something like 00199387   0.186KG
        # length should be exactly 18
        length = len(result)
    
        pw = pwr(False, "", "", False, "no data")
        if (length > 0):
            pw.hasData = True

            if (length == 22):
                pw.success = True
                #work order number is the first 8 chars
                pw.workOrderNumber = remove_control_characters(result[:9].strip())
                print(pw.workOrderNumber)
                # weight is the last 11 (or so) chars
                pw.weight = result[-11:].strip()

                uom = pw.weight[-2:]    # get the UoM, it must bt LG
                if (uom != "LG"):
                    pw.success = False
                    pw.msg = "Invalid U of M"
                    return pw

                pw.weight = pw.weight[:-2] # get rid of the letters at the end

                if (pw.weight == "0.000"):
                    pw.success = False
                    pw.msg = "A zero weight was found, ensure item is on scale"

            else:
                pw.success = False
                pw.msg = "An invalid number of characters was read from the scale"
                pw.workOrderNumber = ""
                pw.weight = "-1"

        return pw

    except Exception as e:
        error = e.args[0]
        lcd.setText(error)


def getTestData():
    import random
    rndm = random.random()
    data = "00198454       0.164LG"

    if (rndm > 0.5):
        # pretend it's bad data
        pass

    else:
        # pretend it's good data
        workOrderNumber = "00198454"
        weight = "2.345"
        displayWoAndWeight(workOrderNumber, weight)

    return data

def displayWoAndWeight(workOrderNumber, weight):
    lcd.setText("Work Order:", workOrderNumber, "Weight:", weight)


# found this at http://stackoverflow.com/questions/4324790/removing-control-characters-from-a-string-in-python
# removes control chars from serial input
def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")