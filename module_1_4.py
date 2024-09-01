my_string = input("Как тебя звать? ")  # Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
Year_age = 2024
my_age = int(input("Каого года рождения? "))  # Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
New_Year = Year_age - my_age
print("Тебя зовут", my_string)
print("Количетсво символов:", len(my_string))  # Вывести количество символов введённого текста
if New_Year < 21:
    print("Тебе", New_Year, "Лет")
else:
    print("Тебе", New_Year, "Года")
#print("Тебе", my_string, if my_string < 21 print("лет") else "года")
print(my_string.upper())  # Выведите строку my_string в верхнем регистре.
print(my_string.lower())  # Выведите строку my_string в нижнем регистре.
print(my_string.replace(" ", ""))  # Измените строку my_string, удалив все пробелы.
print(my_string[0]) #Выведите первый символ строки my_string.
print(my_string[-1]) #Выведите последний символ строки my_string.
