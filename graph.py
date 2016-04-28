
import numpy as np
import matplotlib.pyplot as plt

def plot(pollCount):
    #plt.ioff()
    #data = np.loadtxt('pv')
    fileName = 'plotVal'

    plt.title('Moisture over time')
    plt.ylabel('Soil moisture value')
    #plt.xlabel('Time in ['+str(pollCount)+' min]')

    xDates = []
    y = []

    with open(fileName) as f:
        content = f.readlines()
        for row in content:
            tmpStr = row.split(" ")
            try:
                xDates.append(tmpStr[0])
            except:
                xDates.append("")
            try:
                y.append(float(tmpStr[1]))
            except:
                try:
                    y.append(float(tmpStr[0]))
                except:
                    y.append(0)
    x = []
    for i in range(len(xDates)):
	    x.append(i)

    plt.plot(x, y,color='blue',linestyle='dotted')
    plt.xticks(x, xDates)
    plt.savefig('static/graph.png')
    plt.show()


plot(0)