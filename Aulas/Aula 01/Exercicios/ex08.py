# -*- coding: utf-8 -*-
# 8) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo 
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

quantidade_dias = input("Digite a quantidade de dias alugados: ")
km_percorridos = input("Digite a quantidade de KM percorridos: ")

preco_a_pagar = (60 * quantidade_dias) + (0.15 * km_percorridos)
print "Total a pagar: R$", preco_a_pagar