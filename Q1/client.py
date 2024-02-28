import socket
import pickle

def send_file(file_path, server_address, server_port):
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((server_address, server_port))
            pickled_data = pickle.dumps(file_data)
            client_socket.sendall(pickled_data)
        print("File sent successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the file path to transfer: ") # ex. "Q1/sent/sample.txt"
    server_address = "127.0.0.1"
    server_port = 3000
    send_file(file_path, server_address, server_port)
