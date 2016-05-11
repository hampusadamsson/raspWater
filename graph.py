
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
def plot(pollCount, sensorNr):
    plt.ioff()
    
    #data = np.loadtxt('pv')
    if(sensorNr == 0):
    	fileName = 'plotVal1'
    else:
	fileName = 'plotVal2'

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

    if(sensorNr == 1):
    	plt.plot(x, y,color='blue',linestyle='dotted')
    	plt.xticks(x, xDates)
    	plt.savefig('static/graph.png')
    
    else:
	plt2.plot(x,y,color='red',linestyle='dotted')
	plt2.xticks(x,xDates)
	plt2.savefig('static/graph2.png')    
#plt.show()


#plot(0,0)
