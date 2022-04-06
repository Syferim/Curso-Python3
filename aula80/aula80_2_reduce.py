from aula80.dados import produtos, pessoas, lista
from functools import reduce


soma_lista = reduce(lambda ac, i: i + ac, lista, 0) # cumulador correto, soma os valores da lista
print(soma_lista)

print()

soma_preços = reduce(lambda ac, p: p['preço'] + ac, produtos, 0) # somando todos os preços da chave preço da biblioteca produtos
print(soma_preços) # print total preço
print(soma_preços / len(produtos)) # print média de preços

print()

soma_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0) #mesmo comando de cima só que com a biblioteca pessoas
print(soma_idades / len(pessoas)) # média de idade das pessoas da biblioteca pessoas