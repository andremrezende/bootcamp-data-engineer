import hashlib

class Switcher(object):
    palavra = ''
    def hashType(self, argument, texto):
        method_name = 'type_' + str(argument)
        method = getattr(self, method_name, lambda: "Invalid type")
        setattr(self, 'palavra', texto)
        return method()
 
    def type_1(self):
        return hashlib.md5(palavra.encode('utf-8'))
 
    def type_2(self):
        return hashlib.sha1(palavra.encode('utf-8'))
 
    def type_3(self):
        return hashlib.sha256(palavra.encode('utf-8'))

    def type_4(self): 
        return hashlib.sha512(palavra.encode('utf-8'))

if __name__ == '__main__':
    resultado = hashlib.md5(b'Python Security')
    print('O hash da string é: {}'.format(resultado.hexdigest()))
    
    palavra = input('Digite o texto a ser gerado a hash: ')
    
    menu = int(input(''' ### MENU - ESCOLHA O TIPO DE HASH ###
                        1) MD5
                        2) SHA1
                        3) SHA256
                        4) SHA512
                        Digite o número do hash a ser gerado: '''))

    tipo = Switcher()    
    tipo.hashType(menu, palavra)
    print('O hash é: {} para o texto: {}'.format(resultado, palavra))