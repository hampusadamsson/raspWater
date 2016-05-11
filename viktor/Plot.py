
import numpy as np
import matplotlib.pyplot as plt


def plot(pollCount, file1, titel, yLabel, saveName):
#    plt.ioff()
    fileName = file1
    plt.title(titel)
    plt.ylabel(yLabel)
    
    #plt.xlabel('Time in ['+str(pollCount)+' min]')

    xDates = []
    y = []

    with open(fileName) as f:
        content = f.readlines()
        for row in content:
            tmpStr = row.split(" ")
            try:
                y.append(float(tmpStr[1]))
                xDates.append(tmpStr[0])
            except:
                try:
                    y.append(float(tmpStr[0]))
                except:
                    y.append(0)

                xDates.append("")


    x = []
    for i in range(len(xDates)):
        x.append(i)

    plt.plot(x, y,color='blue',linestyle='dotted')
    plt.xticks(x, xDates)
    plt.savefig('../static/' + saveName + '.png')
    plt.show()

plot(0,0, 'Moisture over time', 'Soil moisture value', "grafen")
