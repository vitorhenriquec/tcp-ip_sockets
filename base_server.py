from socket import *
import time

host = 'localhost'
portnumber = 50007

#Cria um objeto socket
socketObj = socket(AF_INET,SOCK_STREAM)

#Vincula o servidor a um port number
socketObj.bind((host,portnumber))

#Número de 5 conexões(clientes) por vez
socketObj.listen(5)

while True:
	#Aceita uma requerimento
	conection, address = socketObj.accept()
	print('Server connected to ', address)
	while True:
		#Recebe o data enviado pelo cliente
		data = conection.recv(1024)
		time.sleep(3)

		#Se não recebe nada para o loop
		if not data: break

		#O servidor manda de volta a menssagem
		conection.send(b'ECO=>' + data)
	conection.close()