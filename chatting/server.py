import socket
from threading import Thread

# 핸들러가 필요함 (task 함수와 비슷한 것이 필요)
# 우리들이 쓴 메세지를 . . . . 
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



# def run_server(host='', port=7789):
def run_server(host='172.30.1.39', port=7789):
    print("server start")
    with socket.socket() as sock:
        sock.bind((host, port))
        sock.listen(20)
        while True:
            conn, addr = sock.accept()
            t = Thread(target=echo_handler, args=(conn, addr, ))    # echo_handler를 여러개를 가져가겠다 ==> 모든 접속자가 각각 스레드 하나씩을 갖게 된다.
            t.start()
        sock.close()


if __name__ == '__main__':
    run_server()