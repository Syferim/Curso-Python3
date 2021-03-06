#list comprehension

l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in range(3)]

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in l1]

l2=['luiz', 'mauro', 'maria']
ex4 = [v.replace('a','@').upper() for v in l2]

tupla= (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
ex5 = [(y, x) for x, y in tupla]
ex5 = dict(ex5)

l3 = list(range(100))
ex6= [v for v in l3 if v % 2 == 0 if v % 8 == 0]

ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]



# print(ex1)
# print(ex2)
print(ex3)
# print(ex4)
# print(ex5)
# print(ex5['valor2'])
# print(ex6)
# print(ex7)