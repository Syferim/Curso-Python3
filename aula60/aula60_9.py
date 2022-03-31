l1 = [1,2,3,4,5,6]
l2 = [v*2 for v in l1]
# print(l2)

lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

# d1 = {x:y for x,y in lista} # comprensão de dicionários
# d1 = dict(lista) # igual o de cima
# print(d1)

d1 = {f'chave_{x}' : x**2 for x in range(5)} # comprensão de dicionários
print(d1, type(d1))
