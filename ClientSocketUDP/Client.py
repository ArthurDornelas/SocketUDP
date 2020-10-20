from socket import *
from pip._vendor.distlib.compat import raw_input

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = raw_input('Digite a operação aritmética:')
clientSocket.sendto(message.encode(), (serverName, serverPort))

responseMessage, serverAddress = clientSocket.recvfrom(2048)
print(responseMessage.decode())
clientSocket.close()

