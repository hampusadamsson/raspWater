
#import numpy as np
import matplotlib.pyplot as plt
plt.use('Agg')

MOISTURE_1 = 1
MOISTURE_2 = 2
HUMIDITY = 3
TEMPERATURE = 4
#WATER = 5

def plot(pollCount, titel, yLabel, saveName, sensorNR):
    plt.ioff()
    fileName = "plot"
    plt.title(titel)
    plt.ylabel(yLabel)
    
    #plt.xlabel('Time in ['+str(pollCount)+' min]')

    xDates = []
    y = []

    #with open(fileName) as f:
    #    content = f.readlines()
    #    for row in content:
    #        tmpStr = row.split(" ")
    #        try:
    #            y.append(float(tmpStr[1]))
    #            xDates.append(tmpStr[0])
    #        except:
    #            try:
    #                y.append(float(tmpStr[0]))
    #            except:
    #                y.append(0)
    #
    #            xDates.append("")

    with open(fileName) as f:
        content = f.readlines()
        for row in content:
            tmpStr = row.split(" ")
            xDates.append(tmpStr[0])
            y.append(float(tmpStr[sensorNR]))

    x = []
    for i in range(len(xDates)):
        x.append(i)

    plt.plot(x, y,color='blue',linestyle='dotted')
    plt.xticks(x, xDates)
    plt.savefig('../static/' + saveName + '.png')
    plt.clf()
    #plt.show()

def plotAll():
    import time
    plot(0, 'Moisture sensor 1', 'Soil moisture value', "moisture_1", MOISTURE_1)
    plot(0, 'Moisture sensor 2', 'Soil moisture value', "moisture_2", MOISTURE_2)
    plot(0, 'Temperature', 'Celsius', "temperature", TEMPERATURE)
    plot(0, 'Humidity', ' water vapour in the air', "humidity", HUMIDITY)

plotAll()