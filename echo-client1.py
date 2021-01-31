import socket

#print("Starting Code Execution of Client 1")
# Create Socket
PORT = 8092
HOST = "127.0.0.1"
RCV_DATA_BUFFER = 1024
RCV_DATA = b"Z"

# Bind the Socket to IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    mySocket.connect((HOST, PORT))
    print("Sending data : ", RCV_DATA.decode('utf-8'))
    mySocket.sendall(b"Z")
    data = mySocket.recv(RCV_DATA_BUFFER)

print("Received with thanks : ", repr(data.decode('utf-8')))