# -*- coding: utf-8 -*-
# 5) Escreva um programa que receba três números e imprima o maior deles.
a = input("Digite o primeiro número: ")
b = input("Digite o segundo número: ")
c = input("Digite o terceiro número: ")

if (a > b and a > c): 
	print a
elif (b > a and b > c):
	print b
else:
	print c