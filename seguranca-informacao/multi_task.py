from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} Km: {}\n'.format(piloto, trajeto))
        

if __name__ == '__main__':
    t_carro1 = Thread(target=carro, args = [1, 'André'])
    t_carro2 = Thread(target=carro, args = [2, 'Papas legua'])
    
    t_carro1.start()
    t_carro2.start()