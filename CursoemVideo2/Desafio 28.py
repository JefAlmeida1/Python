import random
n = int(input('Qual numero eu escolhi? '))
l = [0,1,2,3,4,5]
r = random.choice(l)
if n == r:
    print('Voce acertou, eu escolhi {}. Parabéns!'.format(r))
else:
    print('Voce errou. Perdeu!')