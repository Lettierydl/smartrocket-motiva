# -*- coding: utf-8 -*-
# 1)Imprima um a tabuada de número que o usuário digitar

numero = input ("Digite um número: ")

for i in range(1,100):
	print "%d * %d = %d" % (numero, i , numero*i) 
