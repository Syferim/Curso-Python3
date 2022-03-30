hora=input('Informe a hora: ')

try:
    hora=int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print("Boa tarde!")
    elif hora >= 18 and hora <= 23:
        print("Boa noite!")
    else:
        print('O número informado não é uma hora válida.')
except:
    print('O valor informado não é um número inteiro.')