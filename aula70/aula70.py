import sys
import time
lista = [0,1,2,3,4,5]
# lista = 1234
# lista = 'ola'
lista = iter(lista)
print(hasattr(lista,'__iter__'))
print(hasattr(lista, '__next__'))

print(next(lista))
print(next(lista))

# for v in lista:
#     print(v)


lista = list(range(10))
print(lista)
print(sys.getsizeof(lista))

def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)
    return r

g = gera()
print(g)
# for v in g:
#     print(v)

print(next(g))
print(next(g))

def gera():
    variavel = 'valor 1'
    yield variavel
    variavel = 'valor 2'
    yield variavel
    variavel = 'valor 3'
    yield variavel

g = gera()

print(next(g))
print(next(g))
print(next(g))

lista = [x for x in range(1000)]
print(type(lista))
lista = (x for x in range(1000))
print(type(lista))
print(sys.getsizeof(lista))