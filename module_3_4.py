def single_root_words(root_word, *other_words):# функция
    same_words = [] # пустой список
    for key in other_words: # Цикл
        if len(root_word) < len(key): # число букв меньше число
            if root_word in key:
                same_words.append(key) # Добавление в список
        else:
            if key.lower() in root_word.lower():
                same_words.append(key)
    return same_words




result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

