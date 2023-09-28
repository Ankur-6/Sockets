#client for echo server using TCP in python

import socket
import sys

#server credentials
#GIVE IP ADDRESS 
#To connect to other devices
#HOST = "192.168.56.1"
IP = socket.gethostbyname(socket.gethostname())
#GIVE PORT NUMBER
PORT = 55203

#create socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST,PORT))
    print("Client is connected")
except Exception as e:
    print("Error in socket creation",e)
    sys.exit()



#client operations

while True:
    try:
        input_message =  input("Enter here: ")
        sock.send(input_message.encode("utf-8"))
        recv_msg = sock.recv(1024)
        if not recv_msg:
            print("No message received")
            break
        print("echo >> ",recv_msg)
    except Exception as e:
        print("Error in handling client",e)
        break
    except KeyboardInterrupt:
        print("Closing client connection")
        break
sock.close()
sys.exit()
