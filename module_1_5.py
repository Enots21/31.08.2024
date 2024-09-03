# Кортежи, которые не изменяемы
immutable_var = 1,2, 3, 4, 5, True, 'Strings'
immutable_var_2 = (1,2, 3, 4, 5)
immutable_var_3 = tuple([1, 2, 3, 4, 5])
#immutable_var[0] = 2 выдаеет ошибку Кортеж не изменяем
print(immutable_var)
print(immutable_var_2)
print(immutable_var[0])

#Cписки
mutable_list = ['apple', 'banana', 'Iphone', 1, 2, 3, True]
mutable_list[0] = 'apples' # Замена значения
mutable_list.append('Footbal') #    в конец строки добовлет
mutable_list.extend(['banana', 2]) #  Разирает на буквы а 2 просто работает как append
mutable_list.remove(1) #Удаления значения
print('Mutable:',mutable_list)
print('Imutable:', immutable_var)