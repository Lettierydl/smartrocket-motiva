n1 = int(raw_input('Digite o primeiro numero: '))
n2 = int(raw_input('Digite o segundo numero: '))
n3 = int(raw_input('Digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print 'seu maior numero:' , n1
elif n2 > n1 and n2 > n3:
    print 'seu maior numero:' , n2
else:
    print 'seu maior numero:' , n3
