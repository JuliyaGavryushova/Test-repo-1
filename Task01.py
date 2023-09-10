# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента

from os.path import join, abspath, dirname
from datetime import datetime

def menu():
    print("Введите 0, чтобы выйти")
    print("Введите 1, чтобы создать заметку")
    print("Введите 2, чтобы посмотреть список заметок")
    print("Введите 3, чтобы чтобы удалить заметку")
    print("Введите 4, чтобы редактировать заметки")
    notes_dic = {}
    while True:
        num = int(input("Введите номер операции: "))
        if num == 0:
            break
        if num == 1:
            note_entry(notes_dic)
        if num == 2:
            read_notes(notes_dic)
        if num == 3:
            del_num = int(input("Введите номер заметки, которую необходимо удалить: "))
            deleting_note(notes_dic, del_num)
        if num == 4:
            upd_num = int(input("Введите номер заметки, которую хотите редактировать: "))
            update_note(notes_dic, upd_num)
 
def note_entry(n_dic: dict):
    note = []
    count = len(n_dic) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите заметку: ")
    dt_now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    note.append(dt_now)
    note.append(title)
    note.append(body)
    n_dic[count] = note
    save_notes(n_dic)

def save_notes(n_dic: dict):
    MAIN_DIR = abspath(dirname(__file__))
    file_name = join(MAIN_DIR, "notebook.csv")
    with open(file_name, mode="w", encoding="utf-8") as file:
        for i, data in n_dic.items():
            file.write(f"{i};{data[0]};{data[1]};{data[2]}\n")

def read_notes(n_dic: dict):
    if len(n_dic) == 0:
        print("Заметок нет")
    else:
        for i, data in n_dic.items():
            print(f"ID заметки: {i}")
            print(f"Дата/время создания: {data[0]}")
            print(f"Заголовок: {data[1]}")
            print(f"Заметка: {data[2]}")
            print("-----------------------------------")

def deleting_note(n_dic: dict, del_n: int):
    if del_n is not None:
        n_dic.pop(del_n)
        save_notes(n_dic)
        print("Заметка удалена")
    else: print("Такой заметки нет")

def update_note(n_dic: dict, upd_n: int):
    if upd_n is None:
        print("Такой заметки нет")
    new_dt = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    n_dic[upd_n][0] = new_dt
    new_title = input("Введите новый заголовок заметки: ")
    new_note = input("Введите новую заметку: ")
    if len(new_title) >= 1:
        n_dic[upd_n][1] = new_title
    if len(new_note) >= 1:
        n_dic[upd_n][2] = new_note
    save_notes(n_dic)
    print("Заметка изменена")

menu()

# 2 вариант
# def menu():
#     print("Введите 0, чтобы выйти")
#     print("Введите 1, чтобы создать заметку")
#     print("Введите 2, чтобы посмотреть список заметок")
#     print("Введите 3, чтобы сохранить в csv формат")
#     print("Введите 4, чтобы чтобы удалить заметку")
#     print("Введите 5, чтобы редактировать заметки")
#     key_count = 0
#     notes_dic = dict()
#     while True:
#         num = int(input("Введите номер операции: "))
#         if num == 0:
#             break
#         if num == 1:
#             note = note_entry()
#             notes_dic, key_count = creating_record(notes_dic, key_count, note)
#             print("Заметка успешно сохранена")
#         if num == 2:
#             print(notes_dic)
#         if num == 3:
#             file_name = input("Введите имя файла: ")
#             export_notes_dic(notes_dic, file_name)
#         if num == 4:
#             del_num = int(input("Введите номер заметки, которую необходимо удалить: "))
#             deleting_note(notes_dic, del_num)
#         if num == 5:
#             upd_num = int(input("Введите номер заметки, которую хотите редактировать: "))
#             update_note(notes_dic, upd_num)

# def note_entry() -> list:
#     note = []
#     dt_now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
#     note.append(dt_now)
#     note.append(input("Введите заголовок заметки: "))
#     note.append(input("Введите заметку: "))
#     return note

# def creating_record(n_dic: dict, count: int, data: list) -> dict:
#     count += 1
#     n_dic[count] = data
#     return n_dic, count

# def export_notes_dic(n_dic: dict, f_name: str):
#     MAIN_DIR = abspath(dirname(__file__))
#     full_name = join(MAIN_DIR, f_name + ".csv")
#     with open(full_name, mode="w", encoding="utf-8") as file:
#         for i, data in n_dic.items():
#             file.write(f"{i};{data[0]};{data[1]};{data[2]}\n")

# def deleting_note(n_dic: dict, del_n: int):
#     if del_n is not None:
#         n_dic.pop(del_n)
#     else: print("Такой заметки нет")
#     return n_dic

# def update_note(n_dic: dict, upd_n: int):
#     if upd_n is None:
#         print("Такой заметки нет")
#         return n_dic
    
#     new_dt = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
#     n_dic[upd_n][0] = new_dt
#     new_title = input("Введите заголовок заметки: ")
#     new_note = input("Введите заметку: ")
#     if len(new_title) >= 1:
#         n_dic[upd_n][1] = new_title
#     if len(new_note) >= 1:
#         n_dic[upd_n][2] = new_note
#     return n_dic

# menu()