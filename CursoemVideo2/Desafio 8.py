#Escreva um programa que leia um valor em metros e o exiba convertido em cantimetros e milimetros.
me = float(input('Digite a medida: '))
cm = me * 100
mm = me * 1000
print('A media de {}m ter de {}cm e {}mm'.format(me,cm,mm))