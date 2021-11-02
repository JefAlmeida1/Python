h = int(input("Digite horas trabalhadas: "))
ht = int(input("Digite a carga horaria do mês: "))
s = float(input("Digite o valor que voce recebe por hora: "))
total = s * ht
print("o valor do salário sai U${:.2f}.".format(total))
