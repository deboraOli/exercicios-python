n1 = int(input('Digite primeira nota '))
n2 = int(input('digite segunda nota '))
n3 = (n1+n2)/2
print('Média foi de {}'.format(n3))
if n3 <= 3:
    print('Reprovado')
elif n3 > 3 and n3 <= 6:
    print('Prova ')
else:
    print('Aprovado')