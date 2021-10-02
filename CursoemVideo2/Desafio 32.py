#ano = int(input('Digite o ano: '))
#b = ano / 4
#n = ano / 100
#if b > n:
#    print('O ano é BISSEXTO')
#else:
#    print('O ano não é BISSEXTO')

#Correção:
from datetime import date
ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano %400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))