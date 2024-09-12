numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Cписок чисел
not_primes = []  # Cписок Не простых чисел
primes = []  # Cписок простых чисел

for number in numbers:  # Цикл
    is_prime = True  # Все числа из списка По умолчание True
    if number == 1:  # Учтите, что число 1 не является ни простым, ни составным числом, поэтому оно отсутствует в конечных списках.
        continue
    for i in range(2, number):  # Цикл который читает список со 2
        if number % i == 0:  # если число делится с остатком и ровняется 0
            is_prime = False  # если вверно то присваиваем False
    if not is_prime:  # если не правда то добавляем в not_primes
        not_primes.append(number)
    else:
        primes.append(number)

print("Простые числа:", primes)
print("Не простые числа:", not_primes)
