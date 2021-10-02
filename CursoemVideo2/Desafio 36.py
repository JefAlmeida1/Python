c = float(input('Qual o valor da casa? '))
s = float(input('Qual é o salario do comprador? '))
an = int(input('Em quantos anos o comprador pretende pagar? '))
m = 12
em = c * ((s + m/100) ** an)
if em > 30:
    print('Voce pode comprar a casa')
else:
    print('Voce passou de 30%, não pode financiar a casa')