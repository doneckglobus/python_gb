'''
Задача 20:
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

Ввод: notebook
Вывод: 12
'''
from pprint import pprint


world = input('World? ').upper()
dct = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}

sm = []
for l in world:
    for i, it in dct.items():
        if l in it:
            sm.append(i)
print(sum(sm))
