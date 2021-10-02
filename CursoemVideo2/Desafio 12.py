#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Digite o valor da mercadoria: R$'))
d = p - (p*5/100)
print('O produto com o valor de R${} com 5% desconto, o produto sai com valor de R${}'.format(p,d))