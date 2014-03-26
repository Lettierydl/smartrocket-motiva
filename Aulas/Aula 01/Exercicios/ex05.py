# -*- coding: utf-8 -*-
# 5) Solicite o preço de uma mercadoria e o percentual de desconto oferecido caso a mesma seja paga à vista.
# Exiba o valor do desconto e o preço a pagar.

valor_mercadoria = float(input("Digite o valor da mercadoria: "))
percentual_desconto = float(input("Digite o valor do percentual de desconto: "))

valor_do_desconto = valor_mercadoria * (percentual_desconto/100.0)
preco_a_pagar = valor_mercadoria - valor_do_desconto

print "O valor do desconto é de:", valor_do_desconto
print "O valor a pagar é de:", preco_a_pagar