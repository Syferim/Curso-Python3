'''
Enumerate- enumerar elementos da lista #list
'''

lista = [
    ['Edu', 'Joao', 'Luiz'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Ed', 'Lu'],
]

minha_lista=[]
enumerada = list(enumerate(lista))
print(enumerada[1][1][2])

for v1 in enumerate (lista, 53):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome3)