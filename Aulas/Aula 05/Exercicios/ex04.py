# -*- coding: utf-8 -*-
# 4) Leia palavras que o usuário digitar até que ele digite ‘fim’ ou até que seja digitado 100 vezes. 
# Imprima a frase formada 

frase = ""
for i in range(100):
	palavra = raw_input("Digite uma palavra: ")

	if (palavra == "fim"):
		break
	else:
		frase += "%s " % palavra

print "A frase digitada foi: %s " % frase