#!/usr/bin/python
# Socket server

# This application runs on the Pipe Scan server.
# The remote logger must access this server with an IP address.
ip = ('', 2525) 
packet_size = 1000

import socket
 
# Open the channel
def open():
    srvsock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    srvsock.bind (ip)
    srvsock.listen  (5)
    return srvsock

# Read one packet and then echo it back
def read_packet(srvsock):
    clisock, (remhost, remport) = srvsock.accept()
    m = clisock.recv(packet_size)
    clisock.send (m)
    clisock.close()
    return m

# Repeatedly read packets
srvsock = open()
while 1:
    m = read_packet(srvsock)
    print m

