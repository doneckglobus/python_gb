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

multiplicity_table= []
a = n*m

i = 0
sum = n
while i <= m:
    if sum > a:
        break
    multiplicity_table.append(sum)
    sum = sum + n
    i+=1

i = 0
sum = m
while i <= n:
    if sum > a:
        break
    multiplicity_table.append(sum)
    sum = sum + m
    i+=1

mt = set(multiplicity_table)

if k in mt:
    print('Можно')
else:
    print('Нельзя')


