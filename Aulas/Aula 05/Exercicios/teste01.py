# -*- coding: utf-8 -*-
# Teste 01: Escreva um programa que conte quantas letras ‘b' aparecem nessa lista:  
# [‘barbados’, ‘barem’, ‘brasil’, ‘cabo verde’, 'cuba']

lista = ['barbados', 'barem', 'brasil', 'cabo verde', 'cuba']

quantidade_de_b = 0

for pais in lista:
	for letra in pais:
		if letra == 'b':
			quantidade_de_b = quantidade_de_b + 1

print "A lista tem %d b's " % (quantidade_de_b)