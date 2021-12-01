#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possiveis sobre ela."""
n = input('Digite algo para converter: ')
print(type(n))
print(n.isalnum()) #isalnum (self) - Verifica se está em Alfanumérico
print(n.isalpha()) #isalpha(self) - Verifica se é Alfabetico
print(n.isnumeric()) #isnumeric(self) - Verifica se os caracteres são numéricos
print(n.isupper()) #isupper(self) - Verifica se está em Maiúsculo
print(n.isdigit()) #isdigit(self) - Verifica se é os caracteres são dígitos
print(n.isdecimal()) #isdecimal(self) - Verifica se todos caracteres são decimais
print(n.isidentifier()) #isidentifier(self) - Verifica se a string for um identificador válido no Python
print(n.islower()) #islower(self) - Verifica se está em minúsculo
print(n.isprintable()) #isprintable(self) - Verifica se todos os caracteres da string forem imprimíveis ou se a string estiver vazia
print(n.isspace()) #isspace(self) - Verifica se é um espaço. Verifica se houver apenas caracteres de espaço em branco na string
