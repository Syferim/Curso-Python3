# def fala_oi():
#     print('fala oi')
#
# variavel = fala_oi

def master(funcao):
    def slave(*args,**kwargs):
        print('estou decorada.')
        funcao(*args, **kwargs)
    # slave()
    return slave

@master
def fala_oi():
    print('oi')

@master
def outra_funcao(msg):
    print(msg)

fala_oi()
outra_funcao('Olá, eu sou o marlon!')

# variavel = master(fala_oi)
# variavel()

# print(type(variavel))
