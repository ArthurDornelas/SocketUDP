from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))

print('Esse servidor esta pronto para receber')
while 1:
    print('Esperando...')

    message, clientAddress = serverSocket.recvfrom(2048)
    messageDecoded = message.decode()

    responseMessage = eval(messageDecoded)

    serverSocket.sendto(str(responseMessage).encode(), clientAddress)
    print("Fechando servidor...")
serverSocket.close()
