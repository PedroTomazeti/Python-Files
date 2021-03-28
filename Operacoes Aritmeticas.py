n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
print('A soma vale {}, a subtração é {}, a multiplicação igual a {},'.format(n1 + n2, n1 - n2, n1 * n2), end=' ')
print(f'A divisão vale {n1 / n2:.2f}, divisão inteira é {n1 // n2}, resto da divisão vale {n1 % n2} e a potência é {pow(n1, n2)}')
