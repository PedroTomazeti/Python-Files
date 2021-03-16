print('Enter the temperature measurement for your region: ')
print('1 - Celsius;\n2 - Fahrenheit;\n3 - Kelvin;')
choice = int(input('What´s your choice? '))
if choice == 1:
    c = float(input('inform the temperature in °C: '))
    print(f'The temperature of {c}°C stands for {c * 1.8 + 32}°F and {c + 273.15}K! ')
elif choice == 2:
    f = float(input('inform the temperature in °F: '))
    print(f'The temperature of {f}°F stands for {(f - 32)/1.8}°F and {(f - 32)/1.8 + 273.15}K! ')
elif choice == 3:
    k = float(input('inform the temperature in K: '))
    print(f'The temperature of {k}K stands for {k - 273.15}°C and {(k - 273.15)* 1.8+ 32}°F! ')
else:
    print('Invalid value!')
