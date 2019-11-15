from socket import *

port = 8080
server_ip = '192.168.0.8'
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((server_ip,port))

print('connecting to the server(%s) on %d port'%(server_ip,port))

while True:
    sendData = input('>>> ')
    clientSock.send(sendData.encode('UTF-8'))
    recvData = clientSock.recv(1024).decode('UTF-8')
    print('서버 : ', recvData)
    if(recvData == 'close'):
        print('server notify that service is over')
        break
clientSock.close()
print("Client is shutdown")