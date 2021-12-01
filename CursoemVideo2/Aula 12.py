# exeplo de estrutura aninhada
nome = str(input('Digite o seu nome: '))
if nome == '':
    print('Que nome bonito!')
elif nome == 'ale' or nome == 'd' or nome == 'andy':
    print('Nome diferente!')
elif nome in 'ret':
    print('Numa ouvi falar nesse nome!')
else:
    print('Nome normal, bom dia, {}!'.format(nome))