"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
"""
import random

B = {random.randint(1, 10) for i in range(10)}
A = list(B)
print(A)

d1 =  int(input('Значание начального диапазона: '))
d2 =  int(input('Значание конечного диапазона: '))

print(A[A.index(d1) + 1:A.index(d2)])



