'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
'''

n = int(input('Введите количество долек длины: '))
m = int(input('Введите количество долек ширины: '))
k = int(input('Сколько долек отломили? '))

a = n*m
if k%n 