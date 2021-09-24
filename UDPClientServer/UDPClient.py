# from the socket module import all
from socket import *
# Create a UDP socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_DGRAM is used for UDP)
clientSock = socket(AF_INET, SOCK_DGRAM)
# get domain name of server.
domainName = getfqdn()
ip = gethostbyname(domainName)
server_address = (domainName, 6789)
## Create a datagram socket.
#DatagramSocket clientSocket = new DatagramSocket(12534);

try:
    # Dynamic message to send to server
    message = input("-->")
    print('sending "%s"' % message)
    # Send message to server along with the address (domain name & port no.)
    clientSock.sendto(str(message).encode(),(server_address))
    # data received
    data = clientSock.recvfrom(1024)
    # Pront out data received
    print("Received: %s From: %s" % data)

except:
    # exception if an error occurs
    print("ERROR -- ")

finally:
    # close the socket.
    clientSock.close()
