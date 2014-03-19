# -*- coding: utf-8 -*-
# 9) Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro. 
# Calcule quantos dias de vida o fumante já perdeu. Exiba o total de dias.

qtd_cigarros_por_dia = input("Digite a quantidade de cigarros por dia: ")
quantos_anos_fumou = input("Digite a quantidade de anos que já fumou: ")

quantidade_cigarros_fumados = qtd_cigarros_por_dia * 365 * quantos_anos_fumou
qtd_minutos_vida_perdidos = 10 * quantidade_cigarros_fumados

minutos_em_um_dia = 24*60
qtd_dias_de_vida_perdidos = qtd_minutos_vida_perdidos/minutos_em_um_dia

print "Voce já perdeu", qtd_dias_de_vida_perdidos, "dias de vida. Hora de parar! :)"