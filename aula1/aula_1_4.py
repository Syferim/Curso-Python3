num1=input('digite um numero?: ')
num2=input('digite outro numero?: ')

#isnumeric isdigit isdecimal
#numeros e positivos (123456)
print(num1.isnumeric())
print(num2.isnumeric())

print(num2.isdigit())


if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
else:
    print('Não pude converter os números para realizar as contas.')