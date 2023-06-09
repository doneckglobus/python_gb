'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
'''
import random

num = int(input('Введите количество монеток: '))
# Сколько из неих упало решкой вверх:
reshka = random.randint(0, num)
orel = num - reshka
print (f"Решка - {reshka}шт., орел - {orel}шт.")

if orel > reshka:
    print(f'Нужно перевернуть решка {reshka} монет ')
elif orel < reshka:
    print(f'Нужно перевернуть орел {orel} монет ')
else:
    print('Неважно, что переворачивать, одинаковое количество орлов и решек')