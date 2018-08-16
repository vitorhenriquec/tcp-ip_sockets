#Configuração de um servidor multiplex - cria várias filas de execução e as executam em 'paralelas'
#Servidor Assíncrono/Desincronizado - utiliza multiplex

#A biblioteca select server é capaz de selecionar as tarefas a serem executadas
import time
from select import select
from socket import socket, AF_INET, SOCK_STREAM

def agora(): return time.ctime(time.time())

#Configurações do servidor
myHost = ''
myPort = 50007

#Número de sockets usados
numberPortSocks = 2

#Lista de sockets criados por funcção de cada socket
socks_principais, leitura_socks, escrita_socks = [], [], []

#Cria um socket para cada função

for i in range(numberPortSocks):
	#Configura um socket TCP/IP
	portsock = socket(AF_INET, SOCK_STREAM)

	#Configura o socket
	portsock.bind((myHost,myPort))
	portsock.listen(5)

	#Adiciona-o a lista de principais e leitores
	socks_principais.append(portsock)
	leitura_socks.append(portsock)

	#Aumento o valor da port para mudar o próximo socket
	#Preciso criar sockets distintos
	myPort+=1

print('Loop de selecao de socket iniciado')

while True:
	#Selecionamos os seguintes sockets:
	legiveis, escreviveis, excessoes = select(leitura_socks, escrita_socks, []) 

	#Para cada socket legível
	for socketobj in legiveis:
		#Caso seja um socket principal
		if socketobj in socks_principais:
			#Aceita todas uma novo cliente de socket
			novo_sock, endereco = socketobj.accept()

			#Imprime as conexões
			print('Conect: ', endereco, id(novo_sock))
			#Coloca no socket de leitura
			leitura_socks.append(novo_sock)
		else:
			#Lemos o que está no socket
			data = socketobj.recv(1024)

			#Imprimi a menssagem recebida
			print('\t Recebeu', data, ' em ', id(socketobj))

			#Se não há dados no socket
			if not data:
				#Fecha-se o socket
				socketobj.close()
				#Remove-se do socket de leitura
				leitura_socks.remove(socketobj)
			else:
				#Prepara-se uma resposta para ser encaminhada
				resposta = 'Eco=>%s as %s' % (data,agora())
				socketobj.send(resposta.encode())