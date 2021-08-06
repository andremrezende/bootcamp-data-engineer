import socket

if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print('Conexão criada com sucesso.')
    except BaseException as e:
        print('Erro: {}'.format(e))
    
    host = 'localhost'
    port = 5432
    
    s.bind((host, port))
    message = 'Servidor: Olá Cliente'
    
    while 1:
        data, address = s.recvfrom(4096)
    
        if data:
            print('Enviando mensagem....')
            s.sendto(data + message.encode(), address)
        