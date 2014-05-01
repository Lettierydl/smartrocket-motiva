# -*- coding: utf-8 -*-
#2) Some os números impares de 0 até 1000

soma = 0
for i in range(1001):
	if(i%2 != 0):
		soma += i

print "A soma é: %d" % soma