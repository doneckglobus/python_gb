"""
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
"""
import json
from pprint import pprint
import os



def menu():
    print("Введите 1 для просмотра телефонной книги")
    print("Введите 2 для добавления записи")
    print("Введите 3 для удаления записи")
    print("Введите 4 для редактирования")
    print("Введите 5 для выхода")
    choice = input("\t")
    return choice


def checkfile(file):
    "Проверка существования файла записной книжки"
    if os.path.exists(file):
        return True
    else: return False

def sh_book(file):
    with open(file) as f:
        phone_book = json.load(f)
        for i in phone_book.values():
            print(*i)

def writefile(file, phone_book):
    "Запись словаря в файл"
    with open(file, 'a') as f:
        json.dump(phone_book, f)

def rm_rec(file):
    rm = input('Введите фамилию или имя для удаления записи: ')
    with open('notebook.json') as f:
        phone_book = json.load(f)
        for i, j in phone_book.items():
            if rm in j:
                ch = input(f'Запись {j} удалить? (y/n?) ')
                if ch == "y":
                    del phone_book[i]
                    break
                else: continue
    with open('notebook.json', 'w') as d:
        json.dump(phone_book, d)

def edt(file):
    ed = input('Введите фамилию или имя для редактирования записи: ')
    with open('notebook.json') as f:
        phone_book = json.load(f)
        for i, j in phone_book.items():
            if ed in j:
                ch = input(f'Запись {j} рекактировать? (y/n?) ')
                if ch == "y":
                    del phone_book[i]
                    list_info = []
                    a = input("Введите имя: ")
                    b = input("Введите фамилию: ")
                    c = input("Введите номер: ")
                    list_info.extend([a, b, c])
                    with open('notebook.json', 'w') as h:
                        phone_book[i] = list_info
                        json.dump(phone_book, h)
                    break
            else: continue

def addtel():
    if checkfile('notebook.json') == False:
        phone_book = {}
        list_info = []
        a = b = c = None
        a = input("Введите имя: ")
        b = input("Введите фамилию: ")
        c = input("Введите номер: ")
        list_info.extend([a, b, c])
        phone_book[1] = list_info
        print(phone_book)
        writefile('notebook.json', phone_book)
    else:
        list_info = []
        a = b = c = None
        a = input("Введите имя: ")
        b = input("Введите фамилию: ")
        c = input("Введите номер: ")
        list_info.extend([a, b, c])
        print(list_info)
        with open('notebook.json') as f:
            phone_book = json.load(f)
        with open('notebook.json', 'w') as h:
            phone_book[len(phone_book.keys())+1] = list_info
            json.dump(phone_book, h)


while True:
    ch = menu()
    if ch == '2':
        addtel()
    elif ch == '1':
        sh_book('notebook.json')
    elif ch == '4':
        edt('notebook.json')
    elif ch == '3':
         rm_rec('notebook.json')
    elif ch == '5':
        exit()
