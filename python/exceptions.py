#https://docs.python.org/3/library/exceptions.html#base-classes
class Error(Exception):
    pass
    
class InputError(Error):
    def __init__(self, message):
       self.message = message


if __name__ == '__main__':

    lista = [1, 10]
    try:
     divisao = 10/0
    except ZeroDivisionError:
        print('Erro ao dividir por Zero.')
        
    try:
      invalido = lista[2]
    except IndexError:
      print('Erro ao acesssar indice inválido')  
      
    try:
     x=a
    except BaseException as ex:
      print('Erro: {}'.format(ex))
      1
      
    try:
     x=1
    except BaseException:
     print('Erro')
    else:
     print('Sem exception') 
     
    arquivo = open('teste.txt', 'w')
    try:
        arquivo.write('teste')
    finally:
        arquivo.close()
        print('Arquivo fechado')
    while True:
        x = int(input('Entre com uma nota de 0 a 10: '))
        try:
            if x>10:
                raise InputError('Nota não pode ser maior que 10')
            elif x<0:    
                raise InputError('Nota não pode ser menor que 0')
            else:
                break
        except InputError as ex:
            print('Error: {}'.format(ex))
       
    
    
    