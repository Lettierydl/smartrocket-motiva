# -*- coding: utf-8 -*-
# 10) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.

valor_total = 2 ** 1000000
valor_total = str(valor_total)
print "2 ^ 1.000.000 tem", len(valor_total), "dígitos"