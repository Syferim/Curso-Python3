nome=input('Qual o seu nome? ')

'''
if nome:
    print(nome)
else:
    print('Você não digitou nada =(')
'''
print(nome or 'Você não digitou nada!')



a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

variavel = a or b or c or d or e or f or g      #jeito 1
print(variavel)

if a:                                           #jeito 2
    variavel = a
elif b:
    variavel = b
else:
    variavel = c

print(variavel)