#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
import math
ag = float(input('Digite o angulo que voce deseja: '))
se = math.sin(math.radians(ag))
cos = math.cos(math.radians(ag))
ta = math.tan(math.radians(ag))
print('O angulo de {} tem o SENO de {:.2f}.'.format(ag,se))
print('O angulo de {} tem o COSSENO de {:.2f}.'.format(ag,cos))
print('O angulo de {} tem a TANGENTE de {:.2f}.'.format(ag,ta))