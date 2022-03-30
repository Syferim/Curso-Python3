'''
split, join, enumerate em Python
*split - dividir uma string # str
*join - juntar uma lista # str
*enumerate - enumerar elementos da lista # iteráveis
'''

'''
string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista1 = string.split(' ')
lista2 = string.split(',')

for valor in lista1:
    print(f'A PALAVRA {valor} apareceu {lista1.count(valor)}x vezes na frase')


print('##########')


palavra= ''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é a palavra {palavra} ({contagem}x)')
'''

'''
string = 'O Brasil é o o o país do futebol, o Brasil é penta.'
lista1 = string.split(' ')
lista2 = string.split(',')

for valor in lista2:
    print(valor.strip().capitalize())
'''

string = 'O brasil é penta'
lista = string.split(' ')
string2 = ' '.join(lista)

print(string)
print(lista)
print(string2)

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])


lista = ['luiz', 'joão', 'maria']

n1, n2, n3 = lista

print(n2)