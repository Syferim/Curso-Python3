def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e','3')
    msg = msg.replace('e','3')
    #print(msg, nome)
    return  f'{msg} {nome}'

variavel = saudacao()
print(variavel)
print(type(variavel))

#saudacao()
#saudacao('e ai meu amigo', 'marlon leandro firmo')
#saudacao(nome='Zezinho', msg='hi')
