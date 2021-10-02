carro = float(input('Qual foi a velocidade do carro? '))
km = 80
m = (carro - km) * 7
if carro > km:
    print('Voce foi multado, vai pagar R${:.2f}'.format(m))
else:
    print('Voce não ultrapassou o limite!')
