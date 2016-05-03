import socket
import time	


MAC = '20:14:10:10:21:04'
port = 1
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((MAC,port))

while True:
	#s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
	#s.connect((MAC,port))
	try:
		#s.connect((MAC,port))
		var = raw_input("Enter a number ")
		print "You entered ", var
		if(var == "E") or (var == "e"):
			print "Exiting... "
			s.close
			break

		s.send(var)
		f = s.makefile()
		data = str(f.readline())
		
		print data
		f.close()
		#s.close
	except socket.error, exc:
		print "Error"
	time.sleep (2)
	
