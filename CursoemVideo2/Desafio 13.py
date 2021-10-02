#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.
s = float(input('Digite o salario: R$'))
n = s + (s * 15/100)
print('O funcionario recebia R${}, agora com aumento de 15%, vai receber R${} de salario'.format(s,n))