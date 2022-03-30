p_nome=input('Informe seu primeiro nome: ')

if len(p_nome) <= 4:
    print('Seu nome é curto')
elif len(p_nome) > 6:
    print('Seu nome é muito grande')
else:
    print('Seu nome é normal')