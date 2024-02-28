import socket
import pickle
import tasks

def send_task(task, worker_address, worker_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((worker_address, worker_port))
            serialized_task = pickle.dumps(task)
            s.sendall(serialized_task)
            result = s.recv(1024)
            return pickle.loads(result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    task1 = {"function": tasks.multiply, "args": (2, 8)} 
    result = send_task(task1, '127.0.0.1', 3000)
    print("Result:", result)
