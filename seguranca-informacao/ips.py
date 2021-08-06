import ipaddress

if __name__ == '__main__':
    ip = '192.168.0.1'
    endereco = ipaddress.ip_address(ip)
    print(endereco+256)
    
    rede = ipaddress.ip_network(ip)
    print(f'Rede: {rede}')
    
    ip = '192.168.0.100/24'
    rede = ipaddress.ip_network(ip, strict = False)
    print(f'rede: {rede}')
    
    ip = '192.168.0.0/24'
    rede = ipaddress.ip_network(ip, strict = False)
    for ipCorrente in rede:
        print(ipCorrente)