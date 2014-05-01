# -*- coding: utf-8 -*-
# 3) Some os 10 primeiros números primos
# Por definicão, um número positivo é primo se for maior do que 1 e for divsível apenas por 1 e por ele mesmo. 

lista_numeros_primos = []

for i in range(2, 1000):
	eh_primo = True
	quantidade_numeros_primos = len(lista_numeros_primos)	

	# Verifica se o número é primo e guarda essa informação em uma variável booleana.
	for j in range(2, i):
		if (i % j) == 0:
			eh_primo = False
	
	if (eh_primo):
		lista_numeros_primos.append(i)
		if quantidade_numeros_primos == 10: #Sai do for caso tenha conseguido capturar os 10 primeiros primos
			break

print "10 primeiros números primos: " + str(lista_numeros_primos)
print "A soma deles é " +  str(sum(lista_numeros_primos))