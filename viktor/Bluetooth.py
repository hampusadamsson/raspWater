import socket


def connect(Address):
  Mac = Address
  port = 1
  s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
  
  try:
	s.connect((Mac,port))
	print "Connected to ", Mac 
		
  except socket.error, exc:
	print "Caught exception socket.error : %s" % exc
        s = 0;
  return s
  

def sendMessage(socket, message):
  try:
  	socket.send(message)
  	
  except socket.error, exc:
  	print "Caught exception socket.error : %s" % exc
    
  
def recieveMessage(socket):
  	
  try:
  	f = socket.makefile()
	data = str(f.readline())
		
  except socket.error, exc:
  	print "Caught exception socket.error : %s" % exc	
	data = "0"
	
  f.close()	
  return data	

def closeSocket(socket):
  try:
  	socket.close()
        print "Socket succesfully closed"
    
  except socket.error, exc:
	print "Caught exception socket.error : %s" % exc	
	
