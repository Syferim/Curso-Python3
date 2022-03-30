variavel = ['luiz Otavio', 'Joaozinho', 'Maria']

começa_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'):
        começa_com_j = True
if começa_com_j:
    print('Existe uma palavra que começa com J')
else:
    print('Não existe uma palavra que começa com J')