import socket

# Create Socket
PORT = 8092
IPADDR = "127.0.0.1"
DATA_BUFFER = 1024


# Function - Decrement Letter
def decrement_letter(charrcv):
    if charrcv.decode('utf-8') != 'A':
        x = chr(ord(charrcv) - 1)
    else:
        x = charrcv
    return x


# Bind the Socket to IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    mySocket.bind((IPADDR, PORT))
    mySocket.listen()

    conn, addr = mySocket.accept()

    with conn:
        print("Connected to the Host:IP ", addr)
        while True:
            data = conn.recv(DATA_BUFFER)
            if not data:
                break
            print("Received Data : ", data.decode('utf-8'))
            chardecr = decrement_letter(data)
            print("Sent Data :", chardecr)
            conn.sendall(chardecr.encode('utf-8'))



