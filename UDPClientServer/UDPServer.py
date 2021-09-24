# from the socket module import all
from socket import *
import time
# Create a UDP socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_DGRAM is used for UDP) [Datagram socket]
serverSock = socket(AF_INET, SOCK_DGRAM)
# get domain name of server.
domainName = getfqdn()
ip = gethostbyname(domainName)
server_address = (domainName, 6789)
serverSock.bind(server_address)

while True:
    print("Server is ready")
    # receives message from client
    message, client_address = serverSock.recvfrom(1024)
    print("Received: ", message, " from ", client_address)
    # date & time of received message
    dateTime = time.strftime("%a, %d %b %Y %H:%M:%S")
    # save records of received messages in log file with timestamp.
    file = open("logfile.txt", "a")
    data = ("Message received: %s \ton %s" %(message, dateTime))
    file.write(data)
    file.close()
    # change received message to uppercase
    message = message.upper(), dateTime
    # Send uppercase message back to client along with ip & port no.
    serverSock.sendto(str(message).encode(), client_address)

# close socket
serverSock.close()
