import socket
import pickle
import multiprocessing
import tasks

def worker_task(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            task = pickle.loads(data)
            function = task["function"]
            args = task["args"]
            result = function(*args)
            conn.sendall(pickle.dumps(result))
        except Exception as e:
            print("Error:", e)



def worker_node(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', port))
        s.listen()
        print(f"Worker listening for tasks on port: {port}...")
        while True:
            conn, addr = s.accept()
            print('Connected by', addr)
            p = multiprocessing.Process(target=worker_task, args=(conn,))
            p.start()
            conn.close()
            print(f"Task completed, closing port: {port}")











if __name__ == "__main__":
    worker_node(3000)

