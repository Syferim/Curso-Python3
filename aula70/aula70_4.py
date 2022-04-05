from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP','MG','BA']
cidades_estados = zip(estados, cidades)

# print(list(cidades_estados))
# print(dict(cidades_estados))

# for valor in cidades_estados:
#     print(valor[0], valor[1])
#     print (valor)
#     print('#'*4)

cidades_estados = zip(
    indice,
    estados,
    cidades,
    # fillvalue = 'Estado'
)

for indice, cidade, estado in cidades_estados:
    print (indice, estado, cidade)