# -*- coding: utf-8 -*-
# Escreva um programa que leia o peso e a altura de uma pessoa e informe se seu peso é o ideal ou não para sua altura,
# OBS: peso ideal, se o valor de (peso / altura2) estiver entre 18,6 e 24,9

peso = float(raw_input("Digite seu peso (em quilos): "))
altura = float(raw_input("Digite sua altura (em metros): "))

imc = (peso)/(altura**2)
print "Seu IMC é: ", imc

if imc >=18.6 and imc <=24.9:
    print 'Seu peso é o ideal'
else:
    print 'Você está Fora do peso ideal'