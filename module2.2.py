first = int(input('Введите 1-Значение '))
second = int(input('Введите 2-Значение '))
third = int(input('Введите 1-Значение '))

if first == second and second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
else:
    print('0')