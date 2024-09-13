import random

def draw_are(number): # функция
    graw_ = '' #Пустой значение
    for i in range(1, number): #Идёт счёт от 1
        for j in range(i+1, number): #Идёт счёт от 1 + 1 и веденное число
            if number % (i+j) == 0:
                graw_ += str(i) + str(j) #Перевод + сложение
    return graw_


print('Введите число')
print(draw_are(int(input())))
