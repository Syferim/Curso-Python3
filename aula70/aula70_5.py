from itertools import zip_longest
'''
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
Lista_a = [1,2,3,4,5,6,7]
Lista_b = [1,2,3,4]

================ resultado
lista_soma = [2,4,6,8]
'''
lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,4]
lista3 = list(zip(lista1,lista2))


### padrão em qualquer linguagem
# lista_soma=[]
# for i in range(len(lista2)):
#     lista_soma.append(lista1[i] + lista2[i])
# print(lista_soma)

### método python
# lista_soma=[]
# for i, _ in enumerate(lista2):
#     lista_soma.append(lista1[i] + lista2[i])
# print(lista_soma)

### como resolvi o exercício
# # lista_soma=[]
# for l1, l2 in lista3:
#     lista_soma.append(l1+l2)
# print(lista_soma)

### método com list comprehension
lista_soma = [x + y for x, y in zip(lista1, lista2)]
print(lista_soma)