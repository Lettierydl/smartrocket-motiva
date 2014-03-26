# -*- coding: utf-8 -*-
# A linha acima nos permite digitar caracteres acentuados no nosso programa.

#1) Faça um programa que peça dois números inteiros e imprima a soma desses dois números.
# Lembrem-se que em Python 2 a função input() captura números. A funcao raw_input() captura strings (palavras).

primeiro_numero = input('Digite o primeiro numero: ') #captura o primeiro numero
segundo_numero = input('Digite o segundo numero: ') #captura o segundo numero
soma = primeiro_numero + segundo_numero

print 'A soma dos dois numeros eh: ', soma