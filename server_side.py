import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Waiting for a connection...")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

while True:
    # Receive a message from the client
    message = client_socket.recv(1024).decode()
    if not message:
        break  # If the client disconnects
    print(f"Client: {message}")

    # Send a response
    response = input("You: ")
    client_socket.send(response.encode())

client_socket.close()
server_socket.close()
