# -*- coding: utf-8 -*-
# 1)Leia uma palavra de 3 letras e escreva de traz para frente. Exemplo,
# entrada:’leo’, saída:’oel'

palavra = raw_input('Digite uma palavra de 3 letras: ')
print palavra[-1]+palavra[-2]+palavra[-3]
