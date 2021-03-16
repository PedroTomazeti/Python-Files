days = int(input('How many days rented? '))
distance = float(input('How many kilometer traveled? '))
rateDays = float(input('What flat fee in your local currency is charged for day: '))
rateDistance = float(input('What flat fee in your local currency is charged for distance? '))
print('Enter your local currency: ')
print('1 - American dollar($); \n2 - Euro(€); \n3 - Reais(R$);')
coin = int(input('Which option? '))
if coin == 1:
    print(f'The total amount to be paid is ${days * rateDays + distance * rateDistance:.2f}')
elif coin == 2:
    print(f'The total amount to be paid is €{days * rateDays + distance * rateDistance:.2f}')
elif coin == 3:
    print(f'The total amount to be paid is R${days * rateDays + distance * rateDistance:.2f}')
else:
    print('Invalid value!')
