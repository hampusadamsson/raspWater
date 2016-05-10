import Bluetooth as bt
MOISTURE_1 = "0"
TEMP = "1"
HUMIDITY = "2"
WATER_LEVEL = "3"
ACTIVATE_PUMP = "4"
MOISTURE_2 = "5"



def getHumidity1(socket):
  bt.sendMessage(socket,MOISTURE_1)
  data = bt.recieveMessage(socket)
  return data
  
def getHumidity2(socket):
  bt.sendMessage(socket,MOISTURE_2)
  data = bt.recieveMessage(socket)
  return data
  
def getTemperature(socket)
  bt.sendMessage(socket,TEMP)
  data = bt.recieveMessage(socket)
  return data

def getHumidity(socket)
  bt.sendMessage(socket,HUMIDITY)
  data = bt.recieveMessage(socket)
  return data
  
def getWaterLevel(socket)
  bt.sendMessage(socket,WATER_LEVEL)
  data = bt.recieveMessage(socket)
  return data
  
def activePump(socket)
  bt.sendMessage(socket,ACTIVATE_PUMP)
  data = bt.recieveMessage(socket)
  print data
  
