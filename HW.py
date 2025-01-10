from datetime import datetime
from mimetypes import inited

to_do = []
while True:
    data = datetime.now()
    q_take_note = input("take note?    _")
    if q_take_note == "yes" or "y" in q_take_note:
        note = input("          _")
        to_do.append(note + " / " + str(data))
        for i in to_do:
            print(f"{to_do.index(i)+1}. {i}")
    else:
        for i in to_do:
            print(f"{to_do.index(i)+1}. {i}")
    q_delete_note = input("delete note?    _")
    if "y" in q_delete_note:
        note_index = int(input("          which one _"))
        to_do.pop(note_index-1)
        for i in to_do:
            print(f"{to_do.index(i)+1}. {i}")
    else:
        for i in to_do:
            print(f"{to_do.index(i)+1}. {i}")
    q_end = input("     end the program? _")
    if q_end == "yes" or "y" in q_end:
        for i in to_do:
            print(f"{to_do.index(i)+1}. {i}")
        break
    else:
        continue
print()
# n = int(input('Введите количество дел на сегодня: '))
# todo = []
#
# print('Введите задачи на сегодня: ')
# for i in range(n):
#     task = input(f'{i + 1}) ')
#     todo.append(task)
#
# print('Список дел на сегодня:')
# print(todo)
#
# n = int(input('Введите номер дела, которое нужно отредактировать: '))
# task = input('Введите новое описание для дела: ')
# todo[n - 1] = task
#
# n = int(input('Введите индекс дела, которое нужно удалить: '))
# todo.pop(n)
#
# print('Список дел на сегодня:')
# print(todo)
