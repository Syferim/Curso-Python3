cpf = '089.583.649.12'#'168.995.350-09'
contador = 0
cpf_lista=[]
cpf_limpo=[]
soma_1=0
soma_2=0
novo_cpf =0

for i in cpf:
    if i.isnumeric():
        i=int(i)
        cpf_lista.append(i)
#    if i=='-':
#        break
print(cpf_lista)

for i in range(0,9):
    cpf_limpo.append(cpf_lista[i])
print(cpf_limpo)

for i,n in enumerate(range(10,1,-1)):
  #  print(cpf_limpo[i],n)
    soma_1+=cpf_limpo[i]*n
print(f'A primeira some é: {soma_1}')
soma_1=11-(soma_1%11)

if soma_1 > 9:
    soma_1=0
print(f'O primeiro digito é: {soma_1}')
cpf_limpo.append(soma_1)

for i,n in enumerate(range(11,1,-1)):
#    print(cpf_limpo[i],n,"ok")
    soma_2+=cpf_limpo[i]*n
print(f'A segunda some é: {soma_2}')
soma_2=11-(soma_2%11)

if soma_2 > 9:
    soma_2=0
print(f'O segundo digito é: {soma_2}')

novo_cpf=cpf_lista[:9]
novo_cpf.append(soma_1)
novo_cpf.append(soma_2)
print(cpf_lista, 'cpf digitado')
print(novo_cpf,'cpf válido')
if cpf_lista == novo_cpf:
    print('Válido')
else:
    print('Inválido')