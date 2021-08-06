import os
def ping(ip_ou_host):
    os.system("ping -n 6 {}".format(ip_ou_host))

def pingSimples():
    print("#" * 60)
    ip_ou_host = input("Digite o Ip ou host a ser verificado: ")
    ping(ip_ou_host)
    print("*" * 60)
    
def pingMultiplo():
    with open("hosts.txt", 'r') as file:
        dump = file.read().splitlines()
        for ip in dump:
            print("#" * 60)
            ping(ip)
            print("*" * 60)
    

if __name__ == '__main__':
    #pingSimples() 
    pingMultiplo()