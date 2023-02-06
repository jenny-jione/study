import socket
from threading import Thread

def echo_handler(conn, addr):
    while True:
        data = conn.recv(1024)
        msg = data.decode()
        print(f'{msg}')

        if "quit" in msg:
            name = msg.split(' ')[0]
            print(f'INFO :: "{name}" exited from the server. {addr}')
            conn.close()
            break

def run_server(host='', port=7789):
    with socket.socket() as sock:
        sock.bind((host, port))
        sock.listen(20)
        while True:
            conn, addr = sock.accept()
            t = Thread(target=echo_handler, args=(conn, addr, ))
            t.start()
        sock.close()
    
if __name__ == '__main__':
    run_server()