import math
import random


random.seed(4)
for i in range(9):
    print(random.randrange(1,7))#numeri random da (x,x)
    print(random.randint(0,2)) #stessa cosa di randrange() ma include anche gli estremi


miaLista = [2,6,567,'pippo','ciao']
print(random.choice(miaLista)) #prendi a caso 1 solo della lista
print(random.sample(miaLista,2)) #prendi a caso 2 valori dalla lista
