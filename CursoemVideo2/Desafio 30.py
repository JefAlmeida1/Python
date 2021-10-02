#n = int(input('Digite um numero: '))
#p = 2,4,6,8,10,12,14,16,18,20
#i = 1,3,5,7,9,11,13,15,17,19
#if i < p:
#    print('O numero é PAR!')
#else:
#    print('O numero é IMPAR!')

#Correção:

numero = int(input('Digite um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero))