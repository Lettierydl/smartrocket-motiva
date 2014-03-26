# -*- coding: utf-8 -*-
#1) Faça um programa que peça o dia do mês e retorna se eu devo lavar o cabelo ou não.
# Só devo lavar o cabelo em dias pares.

dia = input("Digite o dia do mês: ")

if (dia >= 1 and dia <= 31):
    if (dia % 2 == 0): # Dia é par
        print "Devo lavar meu cabelo, pois o dia é par!"
    else:
        print "Não devo lavar meu cabelo, pois hoje é dia ímpar!"  

else:
    print "Isso que você digitou não é um dia válido!"