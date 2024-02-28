import socket
import pickle

def receive_file(save_directory, server_address, server_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((server_address, server_port))
            server_socket.listen(1)
            print("Server listening...")

            conn, addr = server_socket.accept()
            with conn:
                print(f"Connection from {addr}")

                received_data = b""
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    received_data += data
                
                unpickled_data = pickle.loads(received_data)
                with open(save_directory, 'wb') as file:
                    file.write(unpickled_data)
        print("File received and saved successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    save_directory = input("Enter the directory to save the received file: ") # ex. "Q1/received/testFile.txt"
    server_address = "127.0.0.1"
    server_port = 3000
    receive_file(save_directory, server_address, server_port)
