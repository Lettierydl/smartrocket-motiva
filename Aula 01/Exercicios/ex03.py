# -*- coding: utf-8 -*-

#3) Escreva um programa que leia a quantidade de dias, horas,
# minutos e segundos de vida do usuário. Calcule o total do tempo
# de vida desse usuário em segundos.

numero_de_dias = input("Digite o número de dias: ")
numero_de_horas = input("Digite o número de horas: ")
numero_de_minutos = input("Digite o número de minutos: ")
numero_de_segundos = input("Digite o número de segundos: ")

# dia = #dias 60s * 60m * 24h
# hora = #horas * 60s * 60m
# minuto = #minutos * #60s

total_em_segundos = numero_de_dias * 60 * 60 * 24
total_em_segundos = total_em_segundos + (numero_de_horas * 60 * 60)
total_em_segundos = total_em_segundos + (numero_de_minutos * 60 )
total_em_segundos = total_em_segundos + numero_de_segundos

print numero_de_dias, "dias +", numero_de_horas, "horas +",  numero_de_minutos, "minutos +", numero_de_segundos, "segundos =", total_em_segundos, "segundos."