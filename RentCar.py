days = int(input('How many days rented? '))
distance = float(input('How many kilometer traveled? '))
rateDays = int(input('What flat fee in your local currency is charged for day: '))
rateDistance = float(input('What flat fee in your local currency is charged for distance? '))
print('Enter your local currency: ')
print('1 - American dollar($); \n2 - Euro(€); \n3 - Reais(R$);')
coin = int(input('Which option? '))
if coin == 1:
    coinChoice = '$'
    print('The total amount to be paid is {}{:.2f}'.format(coinChoice, days * rateDays + distance * rateDistance))
elif coin == 2:
    coinChoice = '€'
    print('The total amount to be paid is {}{:.2f}'.format(coinChoice, days * rateDays + distance * rateDistance))
elif coin == 3:
    coinChoice = 'R$'
    print('The total amount to be paid is {}{:.2f}'.format(coinChoice, days * rateDays + distance * rateDistance))
else:
    coinChoice = None
    print('Invalid value!')
