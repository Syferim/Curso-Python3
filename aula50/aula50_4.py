# 1) função que exiba saudação e nome
def hi(a='Olá a todos!',b='usuário'):
    print(a, b)

hi('Oi', 'Marlon')

# 2) função que recebe 3 numeros como parametros e exiba a soma entre eles
def soma(a,b,c):
    return a+b+c

var=soma(1,2,3)
print(var)

# 3) recebe 2 numeros, o primeiro é um valor e o segundo um percentual (ex. 10%).
# retorne o valor do primeiro numero somado do aumento do percentual do mesmo.

def conta(a,b):
    var=a+(a*b/100)
    return var

var=conta(10,20)
print(var)

# 4)
def divisivel(a):
    if a%3 == 0 and a%5 == 0:
        return  'FizzBuzz'
    if a%3 == 0:
        return 'Fizz'
    if a%5 == 0:
        return 'Buzz'
    return a

var=divisivel(60)
print(var)
