import random
import time
lista = ['Rokket', 'Zombie', 'Salamangreat', 'Phantom Knight', 'Darklord', 'Shaddoll', 'Dino', 'Aesir', 'Destiny',
         'Black Magician', 'Cyber Dragon', 'Odd Eyes', 'Lunalight', 'Dinomist', 'Peluguel', 'Pendulum Magician',
         'Harpie', 'Crusadia']
lista1 = ['Salamangreat', 'Phantom Knight', 'Dino', 'Aesir', 'Destiny',
         'Black Magician', 'Cyber Dragon', 'Odd Eyes']
#for c in range(0, 18):
  #  sorteio = random.choice(lista)
   # print(sorteio)
    #lista.remove(sorteio)
    #time.sleep(2)
for c in range(0, 8):
    sorteio = random.choice(lista1)
    print(sorteio)
    lista1.remove(sorteio)
    time.sleep(2)