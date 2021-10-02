#Desenvolva um programa que pergute a quantidade de km percorridos por um carro alugado e a quantidade de dia pelo quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro consta R$60,00 por dia e R$0,15 por KM rodado.
d = int(input('Quantos dias alugado? '))
km = float(input('Quanto Km rodado? '))
p = (d*60) + (km*0.15)
print('O total a pagar é R${:.2f}.'.format(p))