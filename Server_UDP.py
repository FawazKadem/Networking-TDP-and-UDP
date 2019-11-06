'''
Server_UDP is a date/time server using UDP.
It will listen for incoming client requests.
There is only one valid request: "What is the current date and time?"
If Server_UDP receives this request, it will return the current date and time.
Otherwise, it will return an error message.

Server_UDP will stay running listening for the next connection.

Note: Can only handle one client interaction at a time.
'''

import socket
from datetime import datetime

# Declare IP address and port
UDP_IP = '127.0.0.1'
UDP_PORT = 5005

# Valid request (exhaustive)
validReq = "What is the current date and time?"

# Create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind socket to port
s.bind((UDP_IP, UDP_PORT))

# Loop allows server to keep listening after one connection ends
while True:
    # Wait for request and decode it when one comes
    req, addr = s.recvfrom(4096)
    currReq = req.decode()

    # If the request isn't valid, send error message.
    # If request is valid, send current date and time string.
    if currReq != validReq:
        errMsg = "Error: Invalid Request.".encode()
        s.sendto(errMsg, addr)
    else:
        now = datetime.now()
        dateTimeStr = now.strftime("%m/%d/%Y %H:%M:%S")
        s.sendto(("Current Date and Time - " + dateTimeStr).encode(), addr)








