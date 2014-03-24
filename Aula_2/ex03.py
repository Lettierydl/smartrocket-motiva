# -*- coding: utf-8 -*-
#3) Escreva um programa que leia 4 notas de um aluno, e imprima se ele passou por média ou foi reprovado, OBS: o aluno passou por média se a média das notas for igual ou superior a 7
n1 = float(raw_input("Digite a primeira nota: "))
n2 = float(raw_input("Digite a segunda nota: "))
n3 = float(raw_input("Digite a terceira nota: "))
n4 = float(raw_input("Digite a quarta nota: "))
media = (n1+n2+n3+n4)/4

print "Sua média foi", media 
if media >=7:
    print 'Passou por média!'
else:
    print 'Tente de novo! Reprovado!'