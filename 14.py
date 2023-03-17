'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''

n = int(input('N: '))


ms = []
for i in range(n):
    if 2**i>n:
        break
    else:
        ms.append(2**i)

print(*ms)

