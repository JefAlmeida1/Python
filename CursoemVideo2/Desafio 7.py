#Desenvolva um programa que leia as duas nota de um aluno, calcule e mostre a sua média.
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('O calculo entre as notas {} e {}, a média é {}'.format(n1,n2,m))