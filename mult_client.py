from socket import *
import threading

class Cliente(threading.Thread):
	def __init__(self,c,server,port, *menssagem):
		#Número de identificação do cliente
		self.c = c
		#Servidor a ser conectado
		self.server = server
		#Port para ser utilizada
		self.port = port
		#Messagens que serão colocadas
		self.msgs = menssagem
		threading.Thread.__init__(self)

	def run(self):
		#Criamos o socket e conectamos ao servidor
		socketobj = socket(AF_INET, SOCK_STREAM)
		socketobj.connect((self.server,self.port))

		#Mandamos a mensagem linha por linha
		for linha in self.msgs:
			socketobj.send(linha)
			#Após mandar uma linha, esperamos uma repostas do servidor 
			data = socketobj.recv(1024)
			print('Cliente:',self.c,' recebeu: ', data)
		socketobj.close()

#Configuro a conexão com o servidor 
#O valor de hostServer pode ser um ip ou um domínio
hostServer = 'localhost'
portServer = 50007

#Messagem a ser codificada em bytes
menssagem =  [b'Ola mundo da internet!']

#Simula de uma maneira simples 20 clientes
for c in range(20):
	Cliente(c,hostServer,portServer,*menssagem).start()

print('Geramos todos os clientes')
'''			
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
'''