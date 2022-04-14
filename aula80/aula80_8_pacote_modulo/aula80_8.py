from aula80.aula80_8_pacote_modulo.calcula_preço import aumento, reducao
from preco import real

preco = 49.90
preco_com_aumento = aumento(valor=preco, porcentagem=15, formata=True)
print(preco_com_aumento)

preco_com_reducao = reducao(valor=preco, porcentagem=15,formata=True)
print(preco_com_reducao)