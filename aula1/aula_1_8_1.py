'''
texto='python'
c=0
while c < len(texto):
    print(texto[c])
    c+=1
'''

texto = 'python'

for letra in texto:
    print(letra)


for n, letra in enumerate(texto): #0123456789
    print(n, letra)


for numero in range(5,10,2): #começando em 5 e vai até 10 pule de 2 em 2
    print(numero)

for numero in range(9,4,-1): #decrementa
    print(numero)

for n in range (0, 100, 8): # acha multiplos de 8
    print(n)
for n in range(100): #o mesmo que o de cima, mostra multiplos de 8
    if n % 8 == 0:
        print(n)

texto = 'Python'
nova_string = ''
for letra in texto:
    if letra == 't':
        nova_string = nova_string +letra.upper()
        continue
    elif    letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra
print(nova_string)