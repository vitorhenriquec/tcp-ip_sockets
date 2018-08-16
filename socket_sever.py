#Uma maneira de configurar um servidor baseado em threads

import socketserver, time

myHost = ''
myPort = 50007

def agora():
	#Retorna o tempo em que a tentativa do cliente foi executado
	return time.ctime(time.time())

class LidaComCliente(socketserver.BaseRequestHandler):
	#Linha com um requerimento
	def handle(self):
		#Para cada conexão com cliente nós
		#Imprimimos a identificao do cliente e o tempo
		print(self.client_address, agora())

		#Simulamos uma atividade
		time.sleep(5)

		while True:
			#Recebe o dado do cliente
			data = self.request.recv(1024)
			if not data: break

			#Escreve e manda a resposta para o cliente
			resposta = 'Eco=>%s at %s' % (data, agora())
			#'request.' socket que representa a comunicação entre o cliente e o servidor
			self.request.send(resposta.encode())
		self.request.close()

#Cria um thread server e lida com a entrada e requisitos de clientes
myAddress = (myHost, myPort)
server = socketserver.ThreadingTCPServer(myAddress, LidaComCliente)
#server_forever() - Executa um loop infinito sobre o server 
server.serve_forever()
