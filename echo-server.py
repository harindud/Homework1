import socket , threading , traceback

# Create Socket
PORT = 8092
IPADDR = "127.0.0.1"
DATA_BUFFER = 1024


# Task 1
def task1_decrement_letter(rcvvlv):
    x = rcvvlv.decode('utf-8')
    if x != 'A':
        x = chr(ord(rcvvlv) - 1)
    return str.encode(x)


# Task 2
def task2_decrement_integer(rcvvlv):
    x = int(rcvvlv.decode('utf-8'))
    print(x)
    return x - 1


# Task 3
def task3_multiply_float(rcvvlv):
    x = float(rcvvlv.decode('utf-8'))
    print(x)
    return x ** 1.5


# Bind the Socket to IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    try:
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

                chardecr = task1_decrement_letter(data)
                print("Sent Data :", chardecr)
                conn.sendall(chardecr)

                # intdecr = task2_decrement_integer(data)
                # print("Sent Data : ", intdecr)
                # conn.sendall(repr(intdecr).encode('utf-8'))

                # floatdecr = task3_multiply_float(data)
                # print("Sent Data : ", floatdecr)
                # conn.sendall(repr(floatdecr).encode('utf-8'))

    except Exception as e:
        print("** Excpt --> ", e)

    finally:
        mySocket.close()
