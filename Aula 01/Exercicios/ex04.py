# -*- coding: utf-8 -*-
# 4) Faça um programa que calcule o aumento de um salário. Ele
# deve solicitar o valor do salário atual e a porcentagem do
# aumento. Exiba o valor do aumento e o valor do novo salário.

salario = input("Digite o valor do salário: ")
porcentagem_aumento = input("Digite a porcentagem do aumento: ")

valor_do_aumento = salario * (porcentagem_aumento/100.0)
novo_salario = salario + valor_do_aumento

print "O valor do aumento é de",  valor_do_aumento, "reais"
print "O novo salário é de",  novo_salario, "reais"