n1=input('Digite um número inteiro: ')

try:
    n1=int(n1)
    print('é um número inteiro.')
    if n1%2 == 0:
         print ('O número é par')
    else:
        print("O número é ímpar")

except:
    print('Não é um número inteiro.')
'''
    try:
        n1=float(n1)
        if n1%2 == 0:
            print ('O número é par')
        else:
            print("O número é ímpar")
    except:
        print('Também não é float, ou seja, não é um número.')
'''
