import ctypes

if __name__ == '__main__':
    atributo_ocultar = 0x02
    retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar)
    if retorno:
        print('Arquivo ocultado')
    else:
        print('Erro ao ocultar arquivo')
