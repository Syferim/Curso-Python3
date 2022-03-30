def divisao(n1, n2):
    if n2 >0:
        return n1 / n2

divide = divisao(8,0)

if divide:
    print(divide)
else:
    print('Conta Inválida')

def dumb():
    return [1,2,3,4,5,6]

var = dumb()

print(var, type(var))


def f(var):
    print(var)

def g():
    return f

var = g()
var('Oi')

def dumb():
    return  ('Luiz', 'Otávio')

var = dumb()
print(var[1], type(var))