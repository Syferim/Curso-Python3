'''
lista   = ['A', 'BACANA' , 'C' , 'D' , 'E' , '10,5']
print(lista[-1])
string  = 'ABacanaCDE'
print(string[1] )

print(lista[0:3])

print(lista[0])
lista[0] = 'Algo'
print(lista[0])

print(lista[0:3]) # o 3 não é incluído, só vai até o 2

print(lista[:3])

print('###########')

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1+l2
print(l3)
print('-----')

l1.extend(l2)
print(l1)
print('-----')
l2.append('b')
print(l2)
'''
'''
l2=[1,2,3,4,5,6]
l2.insert(0, 'banana')
print(l2)
print('---------')
l2.pop() # remove o ultimo
print(l2)
print('############')
l2 = [1,2,3,4,5,6,7,8,9]
del(l2[3:5]) # remove uma faixa
print(l2)
'''


'''
l1=[1,2,3,4]
print(max(l1))
print(min(l1))

l2 = list(range(1,10,2))
print(l2)

for valor in l2:
    print(valor)

l2=['string', True, 10, -20.5]

for elemento in l2:
    print(f'O tipo de elemento é {type(elemento)} e seu valor é {elemento}')
'''

secreto = 'perfume'
digitadas = []
chances = 3

while True:

    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFFzzzz: a letra "{letra}" NÃO EXISTE na palavra secreta')
        digitadas.pop()
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario  += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print('Que legal, VOCÊ GANHOU!!!')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')