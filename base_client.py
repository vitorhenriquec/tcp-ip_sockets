from socket import *

serverHost = 'localhost'
serverPort = 50007

menssagem = [b'Ola mundo da internet!']

socketObj = socket(AF_INET,SOCK_STREAM)

#Connect indica que é um cliente
socketObj.connect((serverHost,serverPort))

for linha in menssagem:
	socketObj.send(linha)
	data = socketObj.recv(1024)
	print('Cliente recebeu', data)