#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro do valor digitado {} vale {}'.format(n,d))
print('O triplo do valor digitado {} vale {}'.format(n,t))
print('A raiz quadrada do valor digitado {} vale é {:.2f}'.format(n,r))