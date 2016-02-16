import httplib2 

def SubmitWeight(workOrderNumber, weight, testingMode):
    """submit weight to web api"""
    # make some fake apiResult data if we're testing
    if (testingMode):
        result = ApiResponse(200, "everything is awesome!")
        return result

    try:
        h = httplib2.Http('.cache')

        url = 'http://incomtek3/api/partWeights/records/scale/' + workOrderNumber + "/" + weight
        
        print(url)
        response, content = h.request(url, "POST", headers={'content-length':'0'} )
    
        responseStatus = response.status
        data = content.decode("utf-8")  # convert byte to string

        result = ApiResponse(responseStatus, data)
        return result

    except Exception as e:
        import LcdStuff as lcd
        lcd.setText(e.args[0])
        import LedConfig as leds
        leds.blinkNoGoLeds()
    finally:
        pass

class ApiResponse():
    """ an object to encapsulate a response from the api """

    def __init__(self, responseStatus, responseData):
        self.status = responseStatus
        self.data = responseData

        @property
        def status(self):
            return self.__status

        @status.setter
        def status(self, status):
            self.__status = status

        @property 
        def data(self):
            return self.__data

        @data.setter
        def data(self, data):
            self.__data = data

