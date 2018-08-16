#Uma maneira de configurar um servidor baseado em thread
import time, _thread as thread
from socket import *

myhost = '' 
myport = 50007

#AF_INIT = Protocolo de endereço IP
#SOCK_STREAM = Protocolo de comunicação TCP
#Gerando um server TCP/IP

socketobj = socket(AF_INET,SOCK_STREAM)

#Vinculo o servidor ao número da porta
socketobj.bind((myhost,myport))

#O socket espera por clientes e ouve 5 conexões por vez
socketobj.listen(5)

def agora():
	#Retorna o tempo em que a tentativa do cliente foi executado
	return time.ctime(time.time())

def lidaCliente(conexao):
	#Simula a ativadade do bloco
	time.sleep(5)

	while True:
		#Recebe o 'data' enviado pelo cliente
		data = conexao.recv(1024)
		
		#Se não receber os dados então paramos o loop
		if not data: break
		
		#Escreve a resposta recebido
		resposta = 'Eco=>%s as %s' % (data, agora())

		#O servidor manda uma resposta
		conexao.send(resposta.encode())
	conexao.close()

def despacha():
	while True:
		#Aceita uma conexão encontrada e devole um novo socket conexao e o endereco do cliente conectado
		conexao, endereco = socketobj.accept()
		print('Server conectado por', endereco, end=' ')
		print('as ', agora())

		#Inicia nova thread para lidar com o cliente
		thread.start_new_thread(lidaCliente,(conexao,))

despacha()


