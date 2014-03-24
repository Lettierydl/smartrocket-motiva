n1 = float(raw_input("Digite a primeira nota: "))
n2 = float(raw_input("Digite a segunda nota: "))
n3 = float(raw_input("Digite a terceira nota: "))
n4 = float(raw_input("Digite a quarta nota: "))
media = (n1+n2+n3+n4)/4
if media >=7:
    print 'passou por media'
else:
    print 'reprovado'