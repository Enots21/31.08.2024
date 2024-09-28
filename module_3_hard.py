data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    dat_num = 0
    for i in data_structure:
        if isinstance(i, int):  # [1, 2, 3],
            dat_num += i
        elif isinstance(i, str):  # "Hello",
            dat_num += len(i)
        elif isinstance(i, (list, tuple, set)):  # (6,35))}]
            inter_sum = calculate_structure_sum(i)
            dat_num += inter_sum
        elif isinstance(i, dict):  # {'cube': 7, 'drum': 8}
            for key, value in i.items():
                if isinstance(key, str):  # 'cube''Urban'
                    dat_num += len(key)
                elif isinstance(key, int):
                    dat_num += key
                if isinstance(value, int):  # 7 8
                    dat_num += value
                elif isinstance(value, str):  # 'drum''Urban2'
                    dat_num += len(value)
    return dat_num


print(calculate_structure_sum(data_structure))

# Рекурсия + внутрения вункция isinstance
