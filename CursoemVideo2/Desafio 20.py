#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
p = str(input('Digite o nome do primeiro aluno: '))
s = str(input('Digite o nome do segundo aluno: '))
t = str(input('Digite o nome do terceiro aluno: '))
q = str(input('Digite o nome do quarto aluno: '))
l = [p,s,t,q]
r = random.choice(l)
l2 = [p,s,t,q]
r2 = random.shuffle(l2)
print('A ordem de apresentação será: ',l2)