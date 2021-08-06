import re
import json
from urllib.request import urlopen

if __name__ == '__main__':
    url = 'http://ipinfo.io/json'
    resposta = urlopen(url)
    dados = json.load(resposta)
    ip = dados['ip']
    org = dados['org']
    cidade = dados['city']
    pais = dados['country']
    regiao = dados['region']
    
    print('Detalhes do seu IP externo\n')
    print('IP: {4} \nRegiao: {1}\nPais: {2}\nCidade: {3}\nOrganização: {0}'.format(org, regiao, pais, cidade, ip))
