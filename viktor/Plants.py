import Bluetooth as bt
import matplotlib
matplotlib.use('Agg')

import Plot as pl
import time
from time import gmtime, strftime


MOISTURE_1 = "0"
TEMP = "1"
HUMIDITY = "2"
WATER_LEVEL = "3"
ACTIVATE_PUMP = "4"
MOISTURE_2 = "5"

WORKING_FILE = "plot"
POLL_INTERVAL = 5
READING_MARGIN_OF_ERROR = 15
HIGHEST_MOISTURE_LEVEL = 120


def test():
    while True:
        address = '20:14:10:10:21:04'
        try:
            s = bt.connect(address)
        except:
            print "Bluetooth unable to connect"

        if(s != 0):
            data1 = []
            data2 = []
            for i in range(5):
                data1.append(getMoisture1(s))
                data2.append(getMoisture2(s))
            data1 = removeOutliers(data1)
            data2 = removeOutliers(data2)

            moist1 = calculateAvg(data1)
            moist2 = calculateAvg(data2)
            humid = str(getHumidity(s)) + " "
            temp = str(getTemperature(s)) + " "
            tiden = str(strftime("%H:%M", gmtime())) + " "

            value = tiden + str(moist1) + " " + str(moist2) + " " + humid + temp

            print("moist1: " + str(moist1))
            print("moist2: " + str(moist2))
            print("temp: " + temp)
            print("humid: " + humid)
            print(value)

            writeToFile(value,WORKING_FILE)

            if (moist1 > HIGHEST_MOISTURE_LEVEL) or (moist2 > HIGHEST_MOISTURE_LEVEL):
                activatePump(s)
                print("Threshold reached")
            bt.closeSocket(s)
        time.sleep(POLL_INTERVAL)


def plotPic():
    print "implement this func"


def writeToFile(sendStr, fileName):
  f = open(fileName,'a')
  sendStr += "\n"
  f.writelines(sendStr) # python will convert \n to os.linesep
  f.close() # you can omit in most cases as the destructor will call it
  #pl.plot(0,fileName)


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
  if(len(sortedList) % 2 != 0):
    medianBorder+=1
    median = sortedList[medianBorder]
  else:
    median1 = sortedList[medianBorder]
    medianBorder+=1
    median2 = sortedList[medianBorder]
    median = (int) ((median1 + median2)/2)
  
  return median
  


def calculateAvg(values):
  sum = 0
  for i in range(len(values)):
    sum += values[i]
  
  sum = sum /len(values)
  
  return sum
 


def getMoisture1(socket):
  bt.sendMessage(socket,MOISTURE_1)
  data = (int)(bt.recieveMessage(socket))
  return data
  
def getMoisture2(socket):
  bt.sendMessage(socket,MOISTURE_2)
  data = (int)(bt.recieveMessage(socket))
  return data
  
def getTemperature(socket):
  bt.sendMessage(socket,TEMP)
  data = (int)(bt.recieveMessage(socket))
  return data

def getHumidity(socket):
  bt.sendMessage(socket,HUMIDITY)
  data = (int)(bt.recieveMessage(socket))
  return data
  
def getWaterLevel(socket):
  bt.sendMessage(socket,WATER_LEVEL)
  data = (int)(bt.recieveMessage(socket))
  return data
  
def activatePump(socket):
  bt.sendMessage(socket,ACTIVATE_PUMP)
  data = bt.recieveMessage(socket)
  print data
  

test()
