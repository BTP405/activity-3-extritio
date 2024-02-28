import socket
import threading
import pickle

# Server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 3000
BUFFER_SIZE = 1024

# List to store connected clients and their usernames
connected_clients = {}
lock = threading.Lock()

# Function to handle client connections
def handle_client(client_socket, client_address):
    try:
        # Receive username from client
        username = pickle.loads(client_socket.recv(BUFFER_SIZE))
        with lock:
            connected_clients[client_socket] = username
        print(f"[*] {username} ({client_address}) connected.")
        broadcast_message("SERVER", username+" has connected.", client_socket)
        while True:
            # Receive pickled message from client
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break

            # Unpickle message
            message = pickle.loads(data)

            # Broadcast message to all connected clients
            broadcast_message(username, message, client_socket)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        with lock:
            del connected_clients[client_socket]
        print(f"{username} ({client_address}) disconnected.")
        broadcast_message("SERVER", username+" has disconnected.", client_socket)
        client_socket.close()

# Function to broadcast message to all connected clients
def broadcast_message(username, message, sender_socket):
    with lock:
        for client_socket in connected_clients:
            if client_socket != sender_socket:
                # Pickle message with username before sending
                pickled_message = pickle.dumps(f"{username}: {message}")
                client_socket.send(pickled_message)

# Function to start the server
def start_server():
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

    try:
        while True:
            # Accept incoming connections
            client_socket, client_address = server_socket.accept()

            # Start a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()

    # Wasn't able to get this working
    except KeyboardInterrupt:
        print("Server shutting down.")
        server_socket.close()

if __name__ == "__main__":
    start_server()
