#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
#Considere US$1,00 = R$3,27
r = float(input('Quanto dinheiro você tem na conta: '))
d = r/3.27
print('Com esse valor R${} você consegue compra US${:.2f} dolares.'.format(r,d) )