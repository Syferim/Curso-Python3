lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

n1, n2, n3, *outra_lista, ultimo_da_lista = lista

print(n1, n2, n3, outra_lista)
print(ultimo_da_lista)


n1, n2, *_ = lista

print(n1, n2)