# -*- coding: utf-8 -*-
#4) A Smart Rocket Telecomunicações lançou uma promoção para incentivar
# que seus clientes façam mais ligações. O preço por minuto para clientes que
# falam até 100 minutos é de R$0.75. Caso o cliente fale até 200 minutos, o
# preço é R$0.60. Caso fale até 400 minutos, R$0.50. Clientes que falam mais
# do que 400 minutos pagam R$0.30.

# Escreva um programa que peça a quantidade de minutos falados pelo cliente
# durante um mês e exiba quanto o cliente deve pagar.

quantidade_de_minutos_falados = input("Digite a quantidade de minutos falados no mês: ")

if quantidade_de_minutos_falados <=100:
	custo_por_minuto = 0.75
elif quantidade_de_minutos_falados <= 200:
	custo_por_minuto = 0.60
elif quantidade_de_minutos_falados <= 400:
	custo_por_minuto = 0.50
else:
	custo_por_minuto = 0.30

print "O total de sua fatura é de R$", (quantidade_de_minutos_falados * custo_por_minuto)