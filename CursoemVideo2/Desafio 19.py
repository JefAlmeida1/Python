#Um professor quer sortear um dos alunos para apagar a guadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
p = str(input('Digite o nome do primeiro aluno: '))
s = str(input('Digite o nome do segundo aluno: '))
t = str(input('Digite o nome do terceiro aluno: '))
q = str(input('Digite o nome do quarto aluno: '))
l = [p,s,t,q]
r = random.choice(l)
print('O aluno sorteado é: ', r)