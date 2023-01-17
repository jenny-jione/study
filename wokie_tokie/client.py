from socket import *

port = 8099

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('192.169.0.62', port))

print('접속 오케이!')

while True:
    recvData = clientSock.recv(1024)
    print('서버가 말합니다: ', recvData.decode('utf-8'))

    sendData = input('>>> ')
    clientSock.send(sendData.encode('utf-8'))