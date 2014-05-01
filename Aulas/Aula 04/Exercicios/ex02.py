# -*- coding: utf-8 -*-
# 2)Escreva um programa que ordene a lista [‘gato’, ‘cavalo’, ‘rato’,
# 'formiga'] do maior animal para o menor, exemplo [‘gato’, ‘rato’,
# ‘cachorro’], saída: [‘cachorro’, ‘gato’, ‘rato’]

a = ['gato', 'cavalo', 'rato', 'formiga']
a.sort()
a.append(a.pop(1))
print a