import socket
import sys

def abreConexaoTCP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Erro: {}".format(e))
        sys.exit()
    
    print('Socket criado com sucesso.')
    
    hostAlvo = input("Digite o Host ou IP a ser conectado: ")
    portaAlvo = input("Digite a porta a ser conectada: ")
    
    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print("Cliente TCP conectado com Sucesso no Host: " + hostAlvo + ":" + portaAlvo)
        s.shutdown(2)
    except socket.error as ex:
        print("Não foi possível conectar ao host {} porta {}. Erro {}".format(hostAlvo, portaAlvo, ex))
        s.close()
        sys.exit()

def abreConexaoUDP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    except socket.error as e:
        print("Erro: {}".format(e))
        sys.exit()
    
    print('Socket UDP criado com sucesso.')
    host = 'localhost'
    port = 5433
    message = 'Olá nego véio!'
    
    try:
        s.sendto(message.encode(), (host, 5432))
        
        dados, servidor = s.recvfrom(4096)
        dados = dados.decode()
        print('Cliente: {}'.format(dados))
    except BaseException as ex:
        print('Erro: {}'.format(ex))
    finally:
        s.close()
        
if __name__ == '__main__':
    
    #abreConexaoTCP()
    abreConexaoUDP()