from socket import *
 
meuHost = 'localhost'
minhaPort = 50007
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((meuHost, minhaPort))
sockobj.listen(1)
 
 
while True:
    conexao, endereco = sockobj.accept()
    print('Server conectado por', endereco)
     
    while True:
        data = conexao.recv(1024)
        print("Ele: ", data.decode())
         
        resposta = input("Voce: ")
        conexao.send(resposta.encode())
 
    conexao.close()