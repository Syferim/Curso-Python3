# variavel = 'valor'
#
# def func():
#     print(variavel)
#
# func()
#
# def func2(): #variavel local se torna global
#     global variavel
#     variavel = 'Outro valor'
#     print(variavel)
#
# func()
# func2()
#
# print(variavel)
#
# def func3(arg = None): #com função replace que muda uma coisa por outra
#     arg = arg.replace('v', 'c')
#     variavel = 'Outro valor'
#     return arg
# func()
# variavel= func3(arg = variavel)
#
# print(variavel)

variavel = 'valor'

def func():
    print(variavel)

func()
