import random
import time
lista = ['Rokket', 'Zombie', 'Salamangreat', 'Phantom Knight', 'Darklord', 'Shaddoll', 'Dino', 'Aesir', 'Destiny', 'Black Magician', 'Cyber Dragon', 'Odd Eyes']
for c in range(0, 12):
    sorteio = random.choice(lista)
    print(sorteio)
    lista.remove(sorteio)
    time.sleep(2)
#print(lista)
