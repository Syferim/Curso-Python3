logged_user = False

'''
if logged_user: # não preciso completar com "== True:"
    msg = 'Usuário locago.'
else:
    msg = 'Usuário precisa logar.'
'''
msg = 'Usuário logado.' if (logged_user) else 'Usuário precisa logar.'
print(msg)


idade = 17
e_de_maior = (idade >=18)
msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'

print(msg)
