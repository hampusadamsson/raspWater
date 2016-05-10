import Bluetooth as bt
MOISTURE_1 = "0"
TEMP = "1"
HUMIDITY = "2"
WATER_LEVEL = "3"
ACTIVATE_PUMP = "4"
MOISTURE_2 = "5"
READING_MARGIN_OF_ERROR = 15


def test():
  address = '20:14:10:10:21:04'
  s = bt.connect(address)
  data1 = []
  for i in range(5):
    data1.append(getMoisture1(s))
  
  data1 = removeOutliers(data1)
  value = calculateAvg(data1)
  print "Moisture 1: " ,value)
  
  value2 = getTemperature(s)
  print "Temperature: ", value2
  
  value3 = getHumidity(s)
  print "Humidity: ", value3
  
  value4 = getWaterLevel(s)
  print "WaterLevel: ",value4
  
  activatePump()
  
  bt.closeSocket(s)
  


def removeOutliers(values):
  maxValue = max(values)
  minValue = min(values)
  if(maxValue - minValue < READING_MARGIN_OF_ERROR):
    return values
  
  data = sorted(values)
  median = calculateMedian(data)
  newValues = []
  
  
  for i in range(len(data)):
    if(abs(data[i] - median) < READING_MARGIN_OF_ERROR):
      newValues.append(data[i])
  
  return newValues
  

  
  
def calculateMedian(sortedList):
  medianBorder = (int) (len(sortedList) / 2)
  median = 0
  if(len(values) % 2 != 0):
    medianBorder++
    median = sortedList[medianBorder]
  else
    median1 = sortedList[medianBorder]
    medianBorder++
    median2 = sortedList[medianBorder]
    median = (int) ((medain1 + median2)/2)
  
  return median
  


def calculateAvg(values):
  sum = 0
  for i in range(len(values)):
    sum += values[i]
  
  sum = sum /len(values)
  
  return sum
 


def getMoisture1(socket):
  bt.sendMessage(socket,MOISTURE_1)
  data = bt.recieveMessage(socket)
  return data
  
def getMoisture2(socket):
  bt.sendMessage(socket,MOISTURE_2)
  data = bt.recieveMessage(socket)
  return data
  
def getTemperature(socket):
  bt.sendMessage(socket,TEMP)
  data = bt.recieveMessage(socket)
  return data

def getHumidity(socket):
  bt.sendMessage(socket,HUMIDITY)
  data = bt.recieveMessage(socket)
  return data
  
def getWaterLevel(socket):
  bt.sendMessage(socket,WATER_LEVEL)
  data = bt.recieveMessage(socket)
  return data
  
def activatePump(socket):
  bt.sendMessage(socket,ACTIVATE_PUMP)
  data = bt.recieveMessage(socket)
  print data
  


test()
