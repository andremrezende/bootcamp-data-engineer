import random, string

tamanho = 16
chars = string.ascii_letters + string.digits + '!@#$%&*()-=+'

rnd = random.SystemRandom()
print(''.join(rnd.choice(chars) for char in range(tamanho)))