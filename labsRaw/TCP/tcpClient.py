import socket

# Server config
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5000

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_IP, SERVER_PORT))
print(f"Connected to server {SERVER_IP}:{SERVER_PORT}")

while True:
    # Prompt the client to send a message
    message = input("Client: ")
    client_socket.send(message.encode())

    # Receive data from the server
    data = client_socket.recv(1024).decode()

    print("Server:", data)

# Close the connection
client_socket.close()
