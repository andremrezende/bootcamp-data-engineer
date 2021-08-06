# https://docs.python.org/pt-br/3/library/hashlib.html
import hashlib

def compararRipemd160(arquivo1, arquivo2):
    hash1 = hashlib.new('ripemd160')
    hash1.update(open(arquivo1, 'rb').read())
    
    hash2 = hashlib.new('ripemd160')
    hash2.update(open(arquivo2, 'rb').read())
    
    if hash1.digest() != hash2.digest():
       print(f'O arquivo : {arquivo1} é diferente do arquivo: {arquivo2}')
    else:
       print(f'O arquivo : {arquivo1} é IGUAL do arquivo: {arquivo2}')
       
    print('O hash do arquivo: a.txt é: {}', hash1.hexdigest())   
    print('O hash do arquivo: b.txt é: {}', hash2.hexdigest())

if __name__ == '__main__':
    arquivo1 = './comparador/a.txt'
    arquivo2 = './comparador/b.txt'

    compararRipemd160(arquivo1, arquivo2)