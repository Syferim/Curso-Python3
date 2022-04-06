from aula80.dados import produtos, pessoas, lista


nova_lista = filter(lambda x: x > 5, lista) # valores acima de 5 na lista lista
print(list(nova_lista))



nova_lista = filter(lambda p: p['preço'] > 50, produtos) # produtos acima de 50 reais na biblioteca produtos

for produto in nova_lista:
    print(produto)

print()

def filtra(produto): # outro método de fazer o filtro acima, só que com def
    if produto['preço'] > 50:
        return True

nova_lista = filter(filtra, produtos) # assim se usa o def de filtro
for produto in nova_lista:
    print(produto)

print()

def filtra(pessoa): # outro exemplo para filtrar menor de idade
    if pessoa['idade'] < 18:
        return True
    else:                  # desnecessário esse else
        return False

nova_lista = filter(filtra, pessoas) # como se usa o def acima
for produto in nova_lista:
    print(produto)