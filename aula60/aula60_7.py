string = '012345678901234567890123456789'
new_string=[]
numeros = ''
for n in string:

    if not n=='9':
        numeros=numeros+n

        continue
    numeros=numeros+n
    new_string.append(numeros)
    numeros=''

print(new_string)


print('#################################')

n = 10
lista = [string[i: i + n] for i in range(0, len(string), n)]
retorno ='.'.join(lista)
print(retorno)

