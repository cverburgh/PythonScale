class PartWeightResult(object):
    """an object to represent reading data from the scale"""

    def __init__(self, hasData, workOrderNumber, weight, success, msg):
        self.__hasData = False
        self.__workOrderNumber = workOrderNumber
        self.__weight = weight
        self.__success = success
        self.__msg = msg


    ## bool - if data was received from scale
    @property
    def hasData(self):
        return self.__hasData

    @hasData.setter
    def hasData(self, hasData):
        self.__hasData = hasData


    ## Work Order Number
    @property
    def workOrderNumber(self):
        return self.__workOrderNumber

    @workOrderNumber.setter
    def workOrderNumber(self, workOrderNumber):
        self.__workOrderNumber = workOrderNumber

    
    ## weight
    @property 
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight


    ## success
    @property 
    def success(self):
        return self.__success

    @success.setter
    def success(self, success):
        self.__success = success


    ## msg
    @property 
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, msg):
        self.__msg = msg

