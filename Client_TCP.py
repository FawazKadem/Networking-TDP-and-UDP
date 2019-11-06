'''
Client_TCP is a client used to access Server_TCP server to receive the current date & time.
Allows user to enter text commands to be sent to the server.
Displays response back from server.

Note: Wasn't sure if client was supposed to keep accepting input or if the program was supposed to end.
I went with the second option because of the line:
    "Client closes connection (only for TCP), server stays running listening for next connection"
If it wanted to keep accepting input, then it wouldn't have to close the connection.

This could be changed by adding a while loop starting after s.connect and ending before s.close()
'''

import socket

# Declare IP address and port
TCP_IP = '127.0.0.1'
TCP_PORT = 5005

# Create TCP socket to be used on client side
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
s.connect((TCP_IP, TCP_PORT))

# Receive request from user
msg = input("Enter request for server: ")
# Send request to server
s.sendall(msg.encode('ascii'))
# Await response from server and decode it
resp = s.recv(4096).decode()

# Display server response (Date and Time if valid request was made, otherwise error message)
print(resp)

# Close connection
s.close()
