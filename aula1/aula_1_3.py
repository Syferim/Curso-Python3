'''
usuario=input('digite seu usuario: ')
qtd_caracteres=len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('vc precisa digitar pelo menos 6 caracteres')
else:
    print('vc foi cadastrado no sistema')
'''

string1 = input('digite algo: ')
string2 = input('digite algo de novo: ')

print(f'A quantidade total de caracteres digitados foi {len(string1)+len(string2)}')
print(string1.__len__())