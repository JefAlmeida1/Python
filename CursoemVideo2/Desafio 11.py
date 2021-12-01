#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessaria para pintá-la, sabendo que cada litro de tinta,
# pinta uma area de 2m².
l = float(input('Digite a largura da parede: '))
alt = float(input(' Digite a altura da parede'))
ar = l * alt
print('Sua parede tem a dimensão de {}x{} e a sua área é de {}m²'.format(l, alt, ar))
