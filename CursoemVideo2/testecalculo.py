#h = int(input("Digite horas trabalhadas: "))
#ht = int(input("Digite a carga horaria do mês: "))
#s = float(input("Digite o valor que voce recebe por hora: "))
#total = s * ht
#print("o valor do salário sai U${:.2f}.".format(total))

#Uma equipe da Fórmula 1 deseja calcular o número mínimo de litros que deverá colocar no tanque de um de seus carros para que ele possa percorrer um determinado número de voltas até o primeiro reabastecimento. Escreva um programa (EM QUALQUER LINGUAGEM) que leia o comprimento da pista (em metros), o número total de voltas a serem percorridas no grande prêmio, o número de reabastecimentos desejados e o consumo de combustível do carro (em Km/L). Calcular e escrever o número mínimo de litros necessários para percorrer até o primeiro reabastecimento. Considere que o número de voltas entre os reabastecimentos é o mesmo.


pista = float(input("Quantos metros tem a pista? "))
voltas = int(input("Digite a quantidade de voltas: "))
litros = float(input("Quantos litro deseja colocar no tanque? "))
km = float(input("Quantos quilometros? "))

cal = litros / km * voltas

print("Total de combustivel até o 1° reabastecimento é {:.2f} litros".format(cal))
