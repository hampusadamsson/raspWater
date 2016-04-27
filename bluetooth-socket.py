import socket
import time
import matplotlib
matplotlib.use('Agg')
from time import gmtime, strftime
import graph as gr


serverMACAddress = '20:14:10:10:21:04'
#serverMACAddress = '68:5D:43:72:4A:EC'
port = 1
#s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
#s.connect((serverMACAddress,port))

while True:
	s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

	try:
		s.connect((serverMACAddress,port))
		s.send('1')
		f = s.makefile()
		data = f.readline()
	
		print data
		f = open('plotVal','a')
		sendStr = ""
		sendStr += str(data)
		sendStr += " "
		sendStr += str(strftime("%H:%M", gmtime()))
		f.write(sendStr) # python will convert \n to os.linesep
		f.close() # you can omit in most cases as the destructor will call it

#        f2 = open('plotValues','a')
#        f2.write(data) # python will convert \n to os.linesep
#        f2.close() # you can omit in most cases as the destructor will call it

		gr.plot(0)
		s.close()
	except socket.error, exc:
		print "Caught exception socket.error : %s" % exc

	time.sleep (10)
        



