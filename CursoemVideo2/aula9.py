#frase = 'prova de python'
#print(len(frase))
#print('p'.join(frase))
#print(frase[5])

#Análise:
#len(): Quando aplicada a um string, retorna o número de caracteres no string (ou seja, o seu comprimento).
#count(): Devolve o número de vezes em que x aparece na lista. Vai contar a quantidade de letra ser repedida.
#find(): Vai mostra a posição de um determinado variavel comaça.
#in: Verifica se tem uma determinada palavra ou valor na variavel.

#Transformação:
#replace(): Vai trocar tudo o que voce quiser que esteja em ''. exemplo:  ('Curso em Video Python' , 'Curso em Video Android')
#upper(): Vai deixar tudo em maiusculo.
#lower(): Vai deixar tudo minusculo.
#capitalize(): Vai jogar todas as caracteres em minusculo, exeto a primeira letra do nome ou algo.
#title(): Vai contar quantas palavra/valores tem na variavel/nome. Pular cada espaço que tem na palavra e deixar as primeiras letras em maiusculo.
#strip(): Vai remover todos os espaço inuteis no inicio e no fim, só não remover o espaço no meio da frase/string.
#rtrip(): Vai remover todos os espaço inuteis da direita da string/nome.
#lstrip(): Vai remover todos os espaço inuteis da esquerda da string/nome.

#Divisão:
#split(): Vai dividir (remover) os espaço numa determinada string/frase/nome. Depois a string recebe uma indexação nova.

#Junção:
#join():  Vai juntar as strings.  Exemplo para ser usado seria colocando em aspas simples:
#'-'.join.(frase) = resultado saria desta forma: Curso-em-Video-Python.


x = y = 10,20
res = x == y
print(res)