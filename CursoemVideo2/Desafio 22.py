nome = str(input('Digite o seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é{}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
