#f = float(input('Informe o seu salario: '))
#s = f + (f * 10) / 100
#sa = f + (f * 15) / 100
#if f > s and s > sa:
#    print('O funcionario recebia R${:.2f}, com aumento de 10% vai receber R${:.2f}.'.format(f,s))
#if f < sa and f < s:
#    print('O funcionario recebia R${:.2f}, com o aumento de 15% vai receber R${:.2f}.'.format(f,sa))

#correção:

s = float(input('Qual é o salario do funcionario? R$'))
if s <= 1250:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)
print('Ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(s,novo))