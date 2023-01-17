from socket import *
import time


serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8099))   # 어디에 연결을 할 것인가. 빈 문자열을 넣으면 모든 ip로부터 수신을 받겠다. 포트: 8099 포트를 사용하겠다
# serverSock.listen(100)  # 동시에 100명까지 소통을 하겠다. 


while(True):
    serverSock.listen(100)  # 동시에 100명까지 소통을 하겠다. 
    connectionSock, addr = serverSock.accept()  # serverSocket에서 뭔가 오면 accept로 캐치를 하고 주소
    print(f'Connected from {addr}')
    data = connectionSock.recv(1024)
    print('received data ', data.decode('utf-8'))

    # server_msg = '안 녕 하 세 요 저 는 서 버 입 니 다 !'
    server_msg = input('클라이언트한테 보낼 메시지: ')
    connectionSock.send(server_msg.encode('utf-8'))
    print('msg transmitted. :: ', server_msg)

    # 여기까지가 서버. 단방향






# 문제점: 메세지 하나 보내면 서버가 바로 끝난다.
# 해결책 찾아오기 (루프문)