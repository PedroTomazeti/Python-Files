import random
n1 = str(input('Insira o primeiro nome: '))
n2 = str(input('Insira o segundo nome: '))
n3 = str(input('Insira o terceiro nome: '))
n4 = str(input('Insira o quarto nome: '))
Lista = [n1, n2, n3, n4]
escolhido = random.choice(Lista)
random.shuffle(Lista)
print('O escolhido foi: {}'.format(escolhido))
print('A ordem será: {}'.format(Lista))
