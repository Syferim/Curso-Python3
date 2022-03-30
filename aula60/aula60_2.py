import copy

# d1 = {'chave1':'valor da chave'}
# d1['nova_chave'] = 'valor da nova chave'
#
# print(d1['chave1'])
#
# d1 = dict(chave1='valor da chave', chave2='valor da outra chave')
#
# print(d1['chave1'])
#
# d1 = {1:'teste', 2:'novo'}
#
# print(d1[2])

# d1 = {
#     '':'valor',
#     123:'outro valor',
#     (1,2,3,4):'tupla',
#}

# print(    d1[(1,2,3,4)]    )
#
# if 'naoexiste' in d1:
#     print(d1['naoexiste'])
#
# print("oi")
#
# d1['nomedachave'] = 'agora existe'
#
# if d1.get('nomedachave') is not None:
#     print(d1.get('nomedachave'))
#
# d1.update({'nova_chave' : 'novo_valor'})
#
# print(d1['nova_chave'])

#########################

d1 = {                  #dicionario
    'chave1':'valor',
    'chave2':'outro valor',
    'chave3':'tupla',
}
print('chave' in d1) #checa se a chave existe
print('chave1' in d1.keys()) #o mesmo que o de cima
print('valor' in d1.values()) #checa valor dentro das chaves
print(len(d1)) #soma quantos pares tenho dentro do dicionario

#del d1['chave1'] #deleta uma chave e seu valor

print(d1)

for k in d1: #enlace de chaves
    print(k)

for v in d1.values(): #enlace de valores
    print(v)

for k in d1.items(): #enlace de tudo
    print(k)
    print(k[0])
    print(k[1])

for k, v in d1.items(): #o mesmo for de cima, só que mais simples
    print(k, v)


clientes = {
    'cliente1' : {
        'nome' : 'Luiz',
    'sobrenome' : 'Otávio',
    },
    'cliente2' : {
        'nome' : 'João',
        'sobrenome' : 'Moreira',
    }
}
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

d1= {1:'a',2:'b',3:['c', 'd']}
v=d1.copy() #dicionarios se não copiados, ambas as variaveis tem o mesmo dicionario
#quando edita um dicionario que não é cópia, ele edita o original tambem
#d1=v1 ambos são os mesmos, d1=v1.copy(), agora v1 é uma cópia independente
v[1] = 'Luiz'

print(f'{d1}\n{v}')
print(v[3][0]) #print do dicionario v da chave 3 no indice 0


v = copy.deepcopy(d1) #copia profunda, agora sim, não existe ligação nenhuma entre eles

v[1] = 'Luiz'
v[3][0]= 'joaozinho'
v[3][1]= 'joaozinho'

print(v)



lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d1= dict(lista) #convertendo uma lista em dicionario
print(d1)

d1.pop('c1') #eliminando a chave e valor c1
print(d1)

d1.popitem() #eliminando o ultimo item do dicionario independente do que seja
print(d1)

d1= {
    1:2,
    3:4,
    5:6,
}

d2 = {
    'a' : 'b',
    'c' : 'd',
    'e' : 'f',
}

d1.update(d2)
print(d1)