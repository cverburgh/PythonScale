def ErrorMessage(var1, var2=""):
    lcdMsgA1
    lcdMsgA2
    lcdMsgB1
    lcdMsgB2

errorCantConnectToPort = ErrorMessage
errorCantConnectToPort.lcdMsgA1 = "Can't connect to"
errorCantConnectToPort.lcdMsgA2 = "port " + errorCantConnectToPort.var2