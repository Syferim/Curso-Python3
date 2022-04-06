from aula80.dados import pessoas


# nova_lista = map(lambda x: x * 2, lista)

# nova_lista = [x *2 for x in lista] # multiplica cada item da lista por 2
# print(lista)
# print(list(nova_lista))
# preços= map(lambda p: p['preço'], produtos) # acessando o conteudo de produto com lambda
# for preço in preços:
#     print(preço)





# def aumenta_preco(p): #aumenta 5% a mais no valor
#     p['preço'] = round(p['preço'] * 1.05,2) # round reduziu a casa após a virgula em 2
#     return p
#
# novos_produtos = map(aumenta_preco, produtos)
#
# for produto in novos_produtos:
#     print(produto)

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p

nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)