nome = 'luiz'
idade = 32
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso/altura**2
print(idade * altura)

print(nome, 'tem', idade, 'anos e seu imc é', imc)
print(f'{nome} tem {idade} anos e seu imc é {imc:.2f}')
print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))
print('{1} tem {0} anos e seu imc é {2:.2f}'.format(idade, nome, imc))
print('{i} tem {n} anos e seu imc é {im:.2f}'.format(i=idade, n=nome, im=imc))


no='marlon'
al=1.70
pe=70.0
ano_atual=2022
nascimento=1993
idade2=ano_atual-nascimento
imc2=pe/al**2
print(idade2)
print(imc)

print(f'{no} tem {idade2} anos e {al} de altura.')
print(f'{no} pesa {pe} e seu imc é {imc2:.2f}.')
print(f'{no} nasceu em {nascimento}.')
