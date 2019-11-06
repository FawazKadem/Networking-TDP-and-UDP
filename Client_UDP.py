'''
Client_TCP is a client used to access Server_TCP server to receive the current date & time.
Allows user to enter text commands to be sent to the server.
Displays response back from server.
'''

import socket

# Declare IP address and port
UDP_IP = '127.0.0.1'
UDP_PORT = 5005

# Create UDP socket to be used on client side
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Receive request from user
msg = input("Enter request for server: ")
# Send message to server
s.sendto(msg.encode('ascii'), (UDP_IP, UDP_PORT))
# Await and receive server response
resp, addr = s.recvfrom(4096)

# Display server response (Date and Time if valid request was made, otherwise error message)
print(resp.decode())
