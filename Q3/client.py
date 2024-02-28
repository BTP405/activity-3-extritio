import socket
import threading
import pickle

# Server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 3000
BUFFER_SIZE = 1024

# Function to receive messages from the server
def receive_messages(client_socket):
    try:
        while True:
            # Receive pickled message from server
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break

            # Unpickle message
            message = pickle.loads(data)
            print(message)

    except Exception as e:
        print(f"Error: {e}")
        client_socket.close()

# Function to send messages to the server
def send_message(client_socket, username):
    try:
        while True:
            # Get user input and send pickled message to server
            message = input("")
            if message.lower() == 'quit':
                break
            pickled_message = pickle.dumps(message)
            client_socket.send(pickled_message)

        client_socket.close()

    except Exception as e:
        print(f"Error: {e}")
        client_socket.close()

if __name__ == "__main__":
    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print("Connected to server.")

        # Prompt user to enter username
        username = input("Enter your username: ")
        print("Type \"quit\" to disconnect")
        # Send username to server
        client_socket.send(pickle.dumps(username))

        # Start threads for sending and receiving messages
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()

        send_thread = threading.Thread(target=send_message, args=(client_socket, username))
        send_thread.start()

    except Exception as e:
        print(f"[!] Error: {e}")
        client_socket.close()
