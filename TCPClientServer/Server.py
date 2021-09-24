# from the socket module import all
from socket import *import time
# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)
# if we did not import everything from socket, then we would have to write the previous line as:
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get fully qualified domain name
domainName = getfqdn()
# get ipv4 format of domain
nameip = gethostbyname(domainName)
# set values for host 'localhost' - meaning this machine and port number 10000
server_address = (domainName, 10000)
# output to terminal some info on the address details
print('*** Server is starting up on %s port %s***' % server_address)
print("*** IP: %s ***" % ip)
# Bind the socket to the host and portsock.bind(server_address)
# Listen for one incoming connections to the
serversock.listen(1)
# we want the server to run all the time, so set up a forever true while loop
while True:
    # Now the server waits for a connection
    print('*** Waiting for a connection ***')
    # accept() returns an open connection between the server and client, along withthe address of the client
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
            # Receive the data in small chunks and retransmit it
        while True:
            # decode() function returns string object
            data = connection.recv(16).decode()
            # if there's data, open log file to add any received data to it
            file = open("log.txt", "a")
            # date & time of received message
            dateTime = time.strftime("%a, %d %b %Y %H:%M:%S")
            if data:
            # data to add to the log file
                logdata = "%s \nMessage: %s" % (dateTime, data)
                # write to logfile
                file.write(logdata)
                # close the log file
                file.close()
                # print out data from the client
                print('received "%s"' % data)
                print('sending data back to the client')
                # Send a message back to the client.
                newData = input("Send Message --> ")
                # encode() function returns bytes object
