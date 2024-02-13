import socket

# Server config
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5000

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the socket to the server address and port
server_socket.bind((SERVER_IP, SERVER_PORT))

# Look for incoming connections
server_socket.listen(1)
print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

# Accept the onnection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode()

    if not data:
        break

    print("Client:", data)

    # Prompt the server to reply
    reply = input("Server: ")
    client_socket.send(reply.encode())

# Close the connection
client_socket.close()
server_socket.close()
