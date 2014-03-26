# -*- coding: utf-8 -*-
# 2) Escreva um programa que leia uma letra, 
# se for "M" imprima Masculino, se for “F" imprima Feminino, caso contrário imprima sexo invalido

letra = raw_input("Digite uma letra: ")
letra = letra.upper() # deixa a letra em caixa alta.

if letra == 'M':
    print 'Masculino'
elif letra == 'F':
    print 'Feminino'
else:
    print 'Letra inválida!'