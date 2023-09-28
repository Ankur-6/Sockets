#echo server using TCP in python

import socket
import sys

#GIVE IP ADDRESS 
IP = socket.gethostbyname(socket.gethostname())
#GIVE PORT NUMBER
PORT = 55520

#create socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP,PORT))
    sock.listen()
    print(f"Server is up and running at {IP}:{PORT}")
except Exception as e:
    print("Error in socket creation",e)
    sys.exit()



#handle the client

while True:
    try:
        client,addr = sock.accept()
        print("Client connected from : ",addr[0],":",addr[1])
        while True:
            try:
                msg = client.recv(1024)
                if not msg:
                    print("No data received")
                    break
                print(addr[0],":",addr[1],">> ",msg)
                client.send(msg)
            except Exception as e:
                print("Error in send/receive: ",e)
                break
            except KeyboardInterrupt:
                print("Closing client connection")
                break
    except Exception as e:
        print("Error in handling client",e)
        break
    except KeyboardInterrupt:
        print("Closing server")
        break
sock.close()
sys.exit()
