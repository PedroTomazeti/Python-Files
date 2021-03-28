import math
b = float(input('Insira o cateto oposto: '))
c = float(input('Insira o cateto adjacente: '))
a = math.sqrt(b**2 + c**2)
print('O valor da hipotenusa é: {} ou {:.2f}'.format(a, math.hypot(b, c)))
