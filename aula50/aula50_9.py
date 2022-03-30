#1
# def ola_mundo(): #correção tarefas
#     return  'olá mundo!'
#
# def mestre(funcao):
#     return funcao()
#
# executando = mestre((ola_mundo))
# print(executando)


#2
def mestre(função, *args, **kwargs):
    return função(*args, **kwargs)

def fala_oi(nome):
    return f'oi {nome}'

def saudação(nome, saudação):
            return f'{saudação} {nome}'

executando = mestre(fala_oi, 'luiz')
print(executando)
