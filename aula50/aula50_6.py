# def func(a1,a2,a3,a4,a5,nome=None, a6=None):
#     print(a1,a2,a3,a4,a5,nome)
#     return nome, a6
# var=func(1,2,3,4,5,nome='Luiz', a6='5')
#
# print(var)

# def func(*args):
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))
#     args = list(args)
#     args[0]=20
#     print(args)

# def func(*args):
#     for v in args:
#         print(v)
# func(1,2,3,4,5)

# def func(*args,**kwargs):
#         print(args)
#         print(kwargs)
#         print(kwargs['nome'], kwargs['sobrenome'])
# # print('#######')
# lista = [1,2,3,4,5]
# # func(*lista,'6')
#
# lista2 = [10,20,30,40,50]
# # func(*lista, *lista2)
# print('#######')
#
# func(*lista, lista2, nome='luiz', sobrenome='miranda')


def func(*args,**kwargs):
        print(args)
        idade = kwargs.get('idade')
        if idade is not None:
            print(idade)
        else:
            print('Idade não existe')
        idade = kwargs['idade']
        print(idade)
lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]

func(*lista, lista2, nome='luiz', sobrenome='miranda', idade=20)




# lista=[1,2,3,4,5]
# n1, n2, *n = lista
# print(n1,n2,n)
#
# lista=[1,2,3,4,5]
# print(lista)
# print(*lista, sep='-')

