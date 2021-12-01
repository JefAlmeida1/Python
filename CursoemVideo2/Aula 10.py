nome = str(input('Qual é o seu nome?: '))
if nome == '':
   print('Que nome lindo!')
else:
    print('Que nome de normal!')
print('Bom dia, {}'.format(nome))

#teste com caulculo de media

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
print('Parabéns'if m>=6 else 'Estude mais!')
