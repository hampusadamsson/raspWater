import socket

def connect(Address):
    print "Connecting"
    Mac = Address
    port = 1
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    try:
        s.connect((Mac,port))
        print "Connected to", Mac
    except:
        print "Caught exception socket.error"
        s = 0
    return s


def sendMessage(socket, message):
    try:
        socket.send(message)
    except:
        print "Caught exception socket.error"


def recieveMessage(socket):
    try:
        f = socket.makefile()
        data = str(f.readline())
        f.close()
    except:
        data = "0"
        print "Caught exception socket.error"

    return data


def closeSocket(socket):
    try:
        socket.close()
        #print "Socket succesfully closed"
    except:
        print "Caught exception socket.error"
	
