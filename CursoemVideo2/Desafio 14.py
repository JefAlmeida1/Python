#Desenvolva um programa que converta uma temperatura digitado em C° e converta para F°.
c = float(input(' Informe a temperatura em C°: '))
f = ((9*c)/5) + 32
print('A temperatura de {}C° correponde a {}F°.'.format(c,f))