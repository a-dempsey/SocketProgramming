# fromm the socket module import all
from socket import *
import time
# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)
# return fully qualified domain name of server
#domainName = "cs1dev.ucc.ie"
domainName = getfqdn()
# IPV4 address of domain name
ip = gethostbyname(domainName)
# set values for host 'localhost' - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
server_address = (domainName, 10000)
# output to terminal some info on the address details
print('connecting to server at %s port %s' % server_address)
print(" IP: %s " % ip)
# Connect the socket to the host and
portsock.connect(server_address)
try:
    # Send data
    message = input("Send Message -->")
    print('sending "%s"' % message)
    # Data is transmitted to the server with sendall()
    # encode() function returns bytes object
    sock.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    # time message was received
    currTime = time.strftime("%H:%M:%S")
    while amount_received < amount_expected:
        # Data is read from the connection with recv()
        # decode() function returns string object
        data = sock.recv(16).decode()
        amount_received += len(data)
        print('received "%s" at %s' % (data, currTime))
        # Send new message back to the server
        message = input("Send Message -->")
finally:
    print('closing socket')
    sock.close()
