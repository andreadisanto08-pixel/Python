import math #importa modulo math

print(math.pi)
print(math.sin(math.pi))
print(math.sin(math.pi/2))
print(dir(math))


miaLista = [1,5,6,'pippo'] #array dinamico
print(miaLista)

for mioElemento in miaLista: #for di python
    print(mioElemento)

for mioElemento in dir(math) :
    print (mioElemento)

for i in range(9):
    print(i)
    
for i in range(2,9,2):
    print(i)

def sin(x):    #def -> parola chiave delle funzioni
    print("ciao", x ,sep = "--")

sin("Pippo")
