#!/usr/bin/python
# Socket client

# This application runs on the remote logger.  
# It must access the Pipe Scan server with an IP address.
ip = ('192.168.1.102', 2525) 
packet_size = 1000

import socket

# Send data and make sure it got there
def send(data):
    clisock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    clisock.connect(ip)
    clisock.send(data)
    x = clisock.recv(packet_size)
    if data!=x:
        print "Send:    ", data
        print "Recieved:", x
    else:
        print "OK"
    clisock.close()

# Open a connection and send the data
send('START')
for i in range(10):
    send(str(i)+". Hello World\n")
send('END')
