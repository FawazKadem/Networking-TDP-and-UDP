'''
Server_TCP is a date/time server using TCP.
It will listen for incoming client requests.
There is only one valid request: "What is the current date and time?"
If Server_UDP receives this request, it will return the current date and time.
Otherwise, it will return an error message.

Server_TCP will stay running listening for the next connection.

Note: Can only handle one client interaction at a time.
'''

import socket
from datetime import datetime

# Declare IP address and port
TCP_IP = '127.0.0.1'
TCP_PORT = 5005

# Create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind socket to port
s.bind((TCP_IP, TCP_PORT))

# Begin listening for incoming connections
s.listen(1)

# Valid request (exhaustive)
validReq = "What is the current date and time?"


# Loop allows server to keep listening after one connection ends.
while True:
    print("Waiting for connection...")
    conn, addr = s.accept()

    # Await request & decode request when one arrives.
    currReq = conn.recv(4096).decode()

    # If the request isn't valid, send error message.
    # If request is valid, send current date and time string.
    if currReq != validReq:
        print("Request is invalid")
        conn.send("Error: Invalid Request.".encode())
    else:
        now = datetime.now()
        dateTimeStr = now.strftime("%m/%d/%Y %H:%M:%S")
        conn.send(("Current Date and Time - " + dateTimeStr).encode())


