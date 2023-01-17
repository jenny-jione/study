from socket import *
import time


clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('192.168.0.102', 8099))
# clientSock.connect(('192.168.0.65', 8099))  # 아 경 님
# clientSock.connect(('127.0.0.1', 8099))
print('Server Connected')


while True:
    client_msg = input('서버에게 보낼 메시지: ')
    # client_msg = ' 안 녕 하 세 요 저 는 클 라 이 언 트 입 니 다 . '
    clientSock.send(client_msg.encode('utf-8'))

    print('msg transmitted. :: ', client_msg)
    data = clientSock.recv(1024)
    print()
    print(data.decode('utf-8'))

    # 단방향 통신이다. 서버에게만 (라디오처럼) 보내고 있음

    # 양방향 통신을 하는게 목적 ==> 채 팅 방 !
