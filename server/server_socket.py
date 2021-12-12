import socket
import sys

HOST = '0.0.0.0'
PORT = 3000

# Create the UDP Socket
try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # socket.setblocking(false)
    print("Socket Created")
except:
    print("Failed to create socket.")
    sys.exit()

# Bind socket to local host and port
try:
    socket.bind((HOST, PORT))
except:
    print("Bind failed.")
    sys.exit()

print("Socket bind complete.")

# Now keep talking to clients

while 1:
    # Receive data from client (data, addr)
    d = socket.recvfrom(1024)
    data = str(d[0], "utf-8")
    addr = d[1]

    # Print to the server who made a connection.
    print("{} wrote:".format(addr))
    print(data)

    # Now have our UDP handler handle the data
    myResponse = data

    # Respond back
    print(myResponse)
    socket.sendto(bytes(myResponse, 'utf-8'), addr)

socket.close()
