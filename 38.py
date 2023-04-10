"""
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
"""
import json
from pprint import pprint
import os



def menu():
    print("Введите 1 дня просмотра телефонной книги")
    print("Введите 2 для добавления записи")
    print("Введите 3 дня удаления записи")
    choice = input()
    return choice

def give_id():
    if os.path.exists("notebook.json"):
        with open("notebook.json") as f:
            phone_book = json.load(f)
            return len(phone_book.keys())+1
    else: return 1

def writefile(file, phone_book):
    with open(file, 'a+') as f:
        json.dump(phone_book, f)


def addtel(phone_book):
    list_info = []
    phone_book.setdefault(give_id(), list_info)
    a = b = c = None
    a = input("Ведите имя: ")
    b = input("Ведите фамилию: ")
    c = input("Ведите номер: ")
    list_info.extend([a, b, c])
#    writefile("notebook.json", phone_book)
    return phone_book

#def rmtel(phone_book):
#    choice = input("Введите имя или фамилию удаляемого контакта")
#    if os.path.exists("notebook.json"):
#        with open("notebook.json", "a+") as f:
#            phone_book = json.load(f)
#            for i, j in phone_book.items():
#               if choice in j:
#                   print('gg')

#                   del phone_book[i]
#            json.dump(phone_book, f)




phone_book = {}
#ch = menu()
#if ch == "1":
#    with open('notebook.json') as f:
#            phone_book = json.load(f)
#            pprint(templates)
#elif ch =="2":
#    addtel(phone_book)

g = addtel(phone_book)
print(*list(*g.values()))
writefile("notebook.json", phone_book)


