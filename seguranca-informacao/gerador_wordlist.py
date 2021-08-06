import itertools

if __name__ == '__main__':
    listaPalavras= 'abcefg'
    resultado = itertools.permutations(listaPalavras, len(listaPalavras))
    for permuta in resultado:
        print(''.join(permuta))