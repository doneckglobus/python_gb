"""
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию,
вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция,
у которой ровно два аргумента, как, например, у операции умножения.
*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**

1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
"""

#from tabulate import tabulate

rows = int(input("Введите количетсво строк: "))
columns = int(input("Введите количетсво столбцов: "))

n=1 
x=1 
y=0
for j in range(1, columns+1):
    print('\n')
    if j > 1:
        n+=1 # увеличение нумерации стобцов
        y+=rows # увеличенине массива строк в связи с увеличением шага цикла
        x+=1 # увеличение шага цикла
    for i in range(n, rows+y+1, x):
        print(f'{i:5}', end =" ")
  
print('\n')    
m_nums = lambda x, y: x*y
print(f"Произведениен чисел равно: {m_nums(rows, columns)}")
#Кажется, я не совсем верно понял условие задачи



    
        
        