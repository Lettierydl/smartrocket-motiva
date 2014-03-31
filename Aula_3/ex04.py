minutos = input('Digite a quantidade de minutos do mes: ')
preco = 0.0
if minutos <= 100:
    preco = 0.75
elif minutos <= 200:
    preco = 0.60
elif minutos <= 400:
    preco = 0.50
else:
    preco = 0.30

print 'O cliente deve pagar ', preco*minutos