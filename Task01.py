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
    print("Введите 5, чтобы найти заметку по дате")
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
        if num == 5:
            date = input("Введите дату в формате дд/мм/гггг: ")
            filtering_date(notes_dic, date)
 
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
    print("Заметка сохранена")

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

def filtering_date(n_dic: dict, f_date: str):
    if len(n_dic) == 0:
        print("Заметок нет")
    else:
        filtered_notes = []
        for i, data in n_dic.items():
            note_date = data[0].split(", ")[0]
            if note_date == f_date:
                filtered_notes.append((i, data))
        
        if len(filtered_notes) == 0:
            print("Нет заметок за указанную дату")
        else:
            for i, data in filtered_notes:
                print(f"ID заметки: {i}")
                print(f"Дата/время создания: {data[0]}")
                print(f"Заголовок: {data[1]}")
                print(f"Заметка: {data[2]}")
                print("-----------------------------------")

menu()