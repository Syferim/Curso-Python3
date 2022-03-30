x=10 #Luiz
y='Luiz' #10
z='Otávio'

print(f'x={x} e y={y}')

x, y = y, x #invertendo o valor das variáveis
print(f'x={x} e y={y}')

x, y, z = z, x, y
print(f'x={x} e y={y} e z={z}')
