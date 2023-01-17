# 2023.01.16

from socket import *

port = 8099
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print("접속 대기중 . . . ")

connectionSock, addr = serverSock.accept()  # 이걸 리스트로 만들어도 0번째 사람이 끝나야 1번째가 보낼 수 있음. 

while True:
    sendData = input('>>> ')
    connectionSock.send(sendData.encode('utf-8'))

    recvData = connectionSock.recv(1024)
    print('상대방: ', recvData.decode('utf-8'))


# 무전기와 같은 원리 but 근데 이 코드는 서버와 클라이언트가 핑퐁만 가능. 단방향 통신