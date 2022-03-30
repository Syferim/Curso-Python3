nome=input('qual o seu nome? ')
idade=int(input('qual a sua idade?'))

idade_menor=18
idade_maior=30
if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')