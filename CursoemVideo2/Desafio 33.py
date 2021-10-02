#n = int(input('Digite o primeiro numero: '))
#a = int(input('Digite o segundo numero: '))
#s = int(input('Digite o terceiro numero: '))
#if n < a < s and n < a > s and n > a > s:
#    print('O Primeiro numedo {} é maior'.format(n))
#if n < a > s and n > a > s and n < a < s:
#    print('O segundo numero {} é maior'.format(a))
#if n > a > s and n <= a > s and n >= a == s:
#    print('O terceiro numero é {} maior'.format(s))
#else:
#    print('O primiro numero {} é menor'.format(n))
#    print('O segundo numero {} é menor'.format(a))
#    print('O terceiro numero {} é menor'.format(s))

#Como ele fez(correção):

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
     menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))