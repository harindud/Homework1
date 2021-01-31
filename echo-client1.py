import socket

#print("Starting Code Execution of Client 1")
# Create Socket
PORT = 8092
HOST = "127.0.0.1"
RCV_DATA_BUFFER = 1024
SND_DATA = b"1.1"

# Bind the Socket to IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    mySocket.connect((HOST, PORT))
    print("Sending data : ", SND_DATA.decode('utf-8'))
    mySocket.sendall(SND_DATA)
    data = mySocket.recv(RCV_DATA_BUFFER)

print("Received with thanks : ", repr(data))