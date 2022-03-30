# add (aciciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)
s1 = {1,2,3,4,5}
s1 = set()
s1.add(1) #adiciona um valor ao set(conjunto=set)
s1.add(2)
#s1.add((1,2,3,'Luiz'))
s1.discard(2) #remove um valor ao set

#s1.update('python') #adicona valores ao set, porém ele itera cada silaba dentro do set
                    #update também não respeita ordem, mandando itens de forma desorganizada
s1.update([1,2,3,4,5], {5,6,7,8})
print(s1)

l1 = [1,2,4,3,4,2,2,1,5,4,5,4,3,4,5,5,6,'marlon','marlon',4,5,6]
l1=set(l1)
l1=list(l1)

print(l1[-1])



s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}

s3= s1 | s2 #junta tudo, eliminando as réplicas
print(s3)

s3= s1 & s2 #mantem tudo o que está em ambos os lados, devem estar em ambos
print(s3)

s3= s1 - s2 #captura elementos unicos, que está em apenas no da esquerda, depende da ordem de s1 e s2
print(s3)

s3= s1 ^ s2 #captura elementos unicos, que está em apenas um, e nãodepende da ordem
print(s3)

s3= s1 == s2