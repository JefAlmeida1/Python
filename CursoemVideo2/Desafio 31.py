#d = float(input('Quantos Km de distancia voce vai viajar? '))
#km = 200
#n = 0.50
#nu = 0.45
#v = (d - km) * n
#p = (d - km) * nu
#if d > km:
#    print('A viagem de {}Km vai custar R${:.2f}.'.format(d,v))
#else:
#    print('A viagem de {}km vai custar R${:.2f}.'.format(d,p))

#correção:
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você esta prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <=200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))