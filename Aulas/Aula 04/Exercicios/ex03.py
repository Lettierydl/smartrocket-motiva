# -*- coding: utf-8 -*-
# 3)Escreva um programa que reordene a lista[ ‘r’, ‘B’, ‘a’, ‘l’, ‘i’, ‘z' ] para que
# ela forme [‘B’, ‘r’, ‘a’, ‘z’, ‘i’, ‘l’]

l = [ 'r', 'B', 'a', 'l', 'i', 'z' ]
aux = l[0]
l[0] = l[1]
l[1] = aux
aux = l[3]
l[3] = l[5]
l[5] = aux
print l