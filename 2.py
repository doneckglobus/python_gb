'''
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''

from functools import reduce

def input_num():
    while True:
        try:
            num_str = input('Введите трехзначное число: ')
            if len(num_str) != 3:
                print("Должно быть три значения")
                continue
            num = int(num_str)

        except ValueError:
            print('Нужно ввести число, а не строку')
        
        else:
            return num_str
def st_sum(str_num):
    sum = reduce(
    lambda x, y: x+y,
    map(int, list(str_num))
    )
    return sum     


str_num = input_num()
print(st_sum(str_num))

