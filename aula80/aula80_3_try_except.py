try:
    # a = []
    # a = {}
    a= 1/0
    print(a)
    print(a[1])
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except IndexError as erro:
    print('Erro de índice.')
except KeyError as erro:
    print('Erro de chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else: # Executa se tudo ocorreu bem em try except
    print('Seu bloco foi executado com sucesso!')
finally: #Sempre executa no final do try excep
    print('Finalmente.')
    a = '0' #Dar um valor padrão ao a caso o try falhe
print(a)
print('Bora continuar...')
