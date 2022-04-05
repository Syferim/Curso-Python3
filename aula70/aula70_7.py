'''
from types import GeneratorType

variavel = ((x, y) for x,y in zip('Alo', 'Alo'))
print(isinstance(variavel, GeneratorType))

print(list(variavel))
'''
##########################
'''
Count - Itertools
'''
from itertools import count

contador = count(start=-1, step=-1)

for valor in contador:
    print(round(valor,2))
    if valor >= 10 or valor <=-10:
        break

lista = ['Luiz', 'João', 'Maria', 'José', 'Sila', 'Eduardo']
contador = count()
lista = zip(contador, lista)
print(list(lista))