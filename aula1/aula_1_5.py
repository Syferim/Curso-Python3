num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))


num_1 = 1
print(f'{num_1:0>10}')
print(f'{num_1:0<10}')
print(f'{num_1:0>10.2f}')

nome = 'marlon'
sobrenome='leandro'
print(f'{nome:#^10}')

nome_formatado = '{:@>10}'.format(nome)
print(nome_formatado)

nome_formatado = '{0:$^50}{1:#^50}'.format(nome, sobrenome)
print(nome_formatado)



