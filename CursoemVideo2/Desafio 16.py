#Crie um programa que leia um numero REAL qualquer pelo teclado e mostre na tela a sua proção INTEIRA.

import math
n = float(input('Digite um numero: '))
print('O numero {} tem a parte inteira {}'.format(n, math.trunc(n)))