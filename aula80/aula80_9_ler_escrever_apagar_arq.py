import os, json

d1 = {
    'Pessoa 1': {
        'nome': 'luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'rose',
        'idade': 30,
    },
}

d1_json = json.dumps(d1, indent=True)   # transforma a lista em json

with open('abc.json', 'w+') as file:    # abre o documento em modo de escrita
    file.write(d1_json)                 #  converte a lista em um arquivo txt



with open('abc.json', 'r') as file: # abre o documento em modo de leitura
    d1_json = file.read()           # importa para o código o txt dentro da variavel
    d1_json = json.loads(d1_json)   # volta a ser lista a variavel com o txt

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)



# https://docs.python.org/3/library/functions.html#open
# modo basico
#
# file = open('abc.txt', 'w+')
# file.write('Linha 1\n')
# file.write('Linha 2\n')
# file.write('Linha 3\n')
#
# file.seek(0,0)
# print('Lendo Linhas: ')
# print(file.read())
# print('#'*10)
#
# file.seek(0,0)
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')
# print('#'*10)
#
# file.seek(0,0)
# print(file.readlines())
#
# file.seek(0,0)
# for linha in file.readlines(): # "for linha in file:" funciona igual
#     print(linha, end='')
#
# file.close()

# modo correto
# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha')
#     file.seek(0,0)
#     print(file.read())
# finally: # sempre é executado
#     file.close

# Modo Pythonico
# with open('abc.txt', 'w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#
#     file.seek(0,0)
#     print(file.read())

# with open('abc.txt', 'r') as file: # apenas lê o arquivo
#     print(file.read())

# with open('abc.txt', 'a+') as file: # Adiciona itens ao final da lista sem apagar o resto
#     file.write('Outra Linha\n')
#     file.seek(0,0)
#     print(file.read())
#
# os.remove('abc.txt')