''''''
'''
while True:
    nome = input("Qual o seu nome? ")
    print(f'Olá {nome}')

print('Não será executado')
'''


'''
x=0
while x <10:
    if x == 3:
        x=x+1
        continue
    print(x)
    x=x+1
print('Acabou!')

'''

x= 0 #coluna
while x <10:
    y= 0 #linha
    while y < 5:
        print(f' X vale {x} e Y vale {y}')
        y+=1
    x+=1
print ('acabou')