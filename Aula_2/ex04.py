peso = float(raw_input("Digite seu peso: "))
altura = float(raw_input("Digite sua altura: "))
resultado = (peso)/altura**2
print resultado
if resultado >=18.6 and resultado <=24.9:
    print 'peso ideal'
else:
    print 'fora do peso'