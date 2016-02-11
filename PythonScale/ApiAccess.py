import httplib2 

def SubmitWeight(workOrderNumber, weight):
    """submit weight to web api"""
    h=httplib2.Http('.cache')
    response, content = h.request('http://craigverburgh.com/asdfadsf')
    
    responseStatus = response.status
    data = content.decode("utf-8")  # convert byte to string

    result = ApiResponse(responseStatus, data)
    return result

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

