grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}# множество
my_students = sorted(list(students)) #Cортируем список по алфавиту
print(dict(zip(my_students, grades))) # Cоединяем список и множество
grad_ab = [(sum(grades[0]) / len(grades[0])), # Переменная которая считает + соеденяет в единное
sum(grades[1]) / len(grades[1]),
sum(grades[2]) / len(grades[2]),
sum(grades[3]) / len(grades[3]),
sum(grades[4]) / len(grades[4])] # конец переменной

print(dict(zip(my_students, grad_ab))) #вывод


