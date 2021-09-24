# import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
# Assign a port number
defaultserverPort = 6789
# Get ip address
defaultdomain = getfqdn()
defaultip = gethostbyname(defaultdomain)
# the machine address and port number have to be the same as the server is using.
server_address = (defaultdomain, defaultserverPort)
# Connect using host & port
serverSocket.connect(server_address)
ip = input("IP: ")
port = input("Port: ")
path = input("Path: ")
try:
    # the url of the site we want to get info from
    # if ip/port/path isnt specified:
    if not ip or port or path:
        #use default
        data = ("http://"+ str(defaultip)+ ":"+ str(defaultserverPort), "/HelloWorld.html")
    else:
        data = ("http://"+str(ip)+":"+str(port),"/"+path)

    serverSocket.sendall(str(data).encode())
    msg = serverSocket.recv(1024).decode()
    print('received "%s"' % (msg))

finally:
    print("Closing socket")
    serverSocket.close()
