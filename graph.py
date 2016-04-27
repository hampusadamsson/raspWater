
import numpy as np
import matplotlib.pyplot as plt
import datetime


def plot(pollCount):
    plt.ioff()
    data = np.loadtxt('plotValues')

    plt.title('Moisture over time')
    plt.ylabel('Moisture value')
    plt.xlabel('Time in ['+str(pollCount)+' min]')

    if(pollCount>0):
        y = data[-pollCount:];
    else:
        y = data

    x = []

    for i in range(y.size):
	    x.append(i)

    plt.plot(x, y,color='blue',linestyle='dotted')
    plt.savefig('static/graph.png')



def plotDates(plotValues, pollCount)

	plt.ioff();
	dataY,dataX  = np.loadtxt(plotValues)
        
	plt.title('Earth moisture change over time')
	plt.ylabel('Moisture value')
	plt.xlabel('Date')

	if(pollCount > 0):
		y = dataY[-pollCount:]
		x = dataX[-pollCount:]
	else
		y = dataY
		x = dataX
       	dates = matplotlib.dates.date2num(x)
	plt.plot(date,y)
	plt.savefig('static/graph2.png')
	


plot(0)

#    plt.pause(0.1)


#def main():

    #plt.axis([0, 1000, 0, 1000])
#    plt.ion()
#    x = 1
#    y = 1
#    while True:
#        plot(x,y)
#        x += 1
#        y += 1

#main()
