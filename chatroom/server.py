import socket
import threading
import sys

# Server configuration
IP = socket.gethostbyname(socket.gethostname())  # Listen on all available network interfaces
PORT = 55203

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((IP, PORT))

# Listen for incoming connections
server_socket.listen(10)  # Maximum number of clients to support

# List to store connected clients
connected_clients = []

# Function to broadcast messages to all connected clients
def broadcast_message(message, sender_socket):
    for client in connected_clients:
        if client != sender_socket:
            try:
                client.send(message.encode("utf-8"))
            except Exception as e:
                print(f"Error broadcasting message: {e}")
        else:
            mes = input("Enetr messaage here: ")
            client.send(mes.encode("utf-8"))

# Function to handle individual client connections
def client_handle(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                print("No message")
                break
            print(f"{client_socket.getpeername()} : {message}")
            broadcast_message(f"{client_socket.getpeername()} : {message}", client_socket)
        except Exception as e:
            print(f"Error handling client: {e}")
            break

    # Remove the client from the list
    connected_clients.remove(client_socket)
    client_socket.close()


# Main server loop to accept incoming connections
def accept_connections():
    while True:
        try:
            client_socket, client_addr = server_socket.accept()
            print(f"[+] {client_addr[0]}:{client_addr[1]} connected")
            connected_clients.append(client_socket)
            client_thread = threading.Thread(target=client_handle, args=(client_socket,))
            client_thread.start()
            print(f"[Active clients] = {len(connected_clients)}")
        except Exception as e:
            print(f"Error accepting client connections: {e}")
            break

if __name__ == "__main__":
    try:
        print(f"Server is up and running at {IP}:{PORT}")
        accept_connections()
    except KeyboardInterrupt:
        print("Server closed.")
        server_socket.close()
        sys.exit()
