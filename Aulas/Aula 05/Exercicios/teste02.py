# -*- coding: utf-8 -*-
# Teste 02: Escreva um programa que verifica se um número digitado é primo

numero = input("Digite um número: ")
eh_primo = True

for i in range(2, numero):
	if (numero % i) == 0:
		eh_primo = False

if eh_primo:
	print "O número é primo"
else:
	print "O número não é primo"