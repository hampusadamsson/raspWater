import socket
import time	


MAC = '20:14:10:10:21:04'
port = 1
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
connected = 0

while connected==0:
	try:
		s.connect((MAC,port))
		connected = 1
	except:
		print "cant connect"
		time.sleep(1)

while True:
	try:
		print("0 - read moisture (sensor1)")
		print("1 - read temerature")
		print("2 - read humidity")
		print("3 - read water sensor")
		print("4 - activate pump")
		print("5 - read moisture (sensor2)")
		print("e - EXIT")

		var = raw_input("Action(0-5): ")

		print "You entered ", var
		if(var == "E") or (var == "e"):
			print "Exiting... "
			s.close
			break
		s.send(var)
		f = s.makefile()
		data = str(f.readline())
		f.close()
		print data
	except:
		print("Error")
		s.close()
	time.sleep (2)
	
