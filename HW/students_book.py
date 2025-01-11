import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
#выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')





# Добавьте вывод информации по всем оценкам для определенного ученика.

# Добавьте вывод среднего балла по каждому предмету по определенному ученику.

# Добавьте еще команды, которые, на ваш взгляд, могут быть полезны для этой задачи.



while True:
    print('''
            Список команд:
            Добавить оценки ученика по предмету----------------------------- 1 
            Вывести средний балл по всем предметам по каждому ученику------- 2
            Вывести все оценки по всем ученикам----------------------------- 3
            Выход из программы---------------------------------------------- 4
            Удалять--------------------------------------------------------- 5
            Редактировать--------------------------------------------------- 6
            ''')
    command = input('Введите номер команды:_')
    if "1" in command:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif "2" in command:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()

    elif "3" in command:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            if student in students_marks.keys():
                print(student)
                # цикл по предметам
                for class_ in classes:
                    if class_ in students_marks[student].keys():
                        print(f'\t{class_} - {students_marks[student][class_]}')
                    else:
                        continue
            else:
                continue
            print()

    elif "4" in command:
        print('4. Выход из программы')
        break

    elif "5" in command:  # Удалять
        print('''
                    Список команд:
                        Удалять данные по:
                            Oценкам----------------------------- 1
                            предметам--------------------------- 2
                            ученикам---------------------------- 3 
                    ''')
        command = input('Введите номер команды:_')
        if "1" in command:
            print("Удалять данные по оценкам")
            # считываем имя ученика
            student = input('Введите имя ученика:_')
            # считываем название предмета
            class_ = input('Введите предмет:_')
            # считываем оценку
            mark = int(input('Введите оценку:_'))
            if mark in students_marks[student][class_]:
                students_marks[student][class_].remove(mark)
                print(f'Для {student} по предмету {class_} удалено оценка {mark}')
            else:
                print('ОШИБКА: не правельное оценка или у студента нет ткаого оценка')


        elif "2" in command:
            print("Удалять данные по предметам")
            # считываем имя ученика
            student = input('Введите имя ученика:_')
            # считываем название предмета
            class_ = input('Введите предмет:_')
            if student in students_marks.keys() and class_ in students_marks[student].keys():
                students_marks[student].pop(class_)
                print(students_marks[student])
                print(f'Для {student} предмет {class_} удалено')
            else:
                print('ОШИБКА: не правельный придмет или студент не проходить такой придмет')

        elif "3" in command:
            print("Удалять данные по ученикам")
            # считываем имя ученика
            student = input('Введите имя ученика:_')
            if student in students_marks.keys():
                students_marks.pop(student)
                print(f'Студент {student} удалено')
            else:
                print('ОШИБКА: не правельный ввод имени студента или студент не регистрирован')

    elif "6" in command:      # Редактировать
        print('''
                            Список команд:
                                Редактировать данные по:
                                    Oценкам----------------------------- 1
                                    предметам--------------------------- 2
                                    ученикам---------------------------- 3 
                            ''')
        command = input('Введите номер команды:_')
        if "1" in command:
            print("Редактировать данные по оценкам")
            # считываем имя ученика
            student = input('Введите имя ученика:_')
            # считываем название предмета
            class_ = input('Введите предмет:_')
            # считываем оценку
            mark = int(input('Введите оценку:_'))
            new_mark = int(input('Введите новую оценку: '))
            if mark in students_marks[student][class_]:
                students_marks[student][class_] = new_mark
                print(f'Для {student} по предмету {class_} изменено оценка {mark} на {new_mark}')
            else:
                print('ОШИБКА: не правельное оценка или у студента нет ткаого оценка')


        elif "2" in command:
            print("Редактировать данные по предметам")
            # считываем имя ученика
            student = input('Введите имя ученика:_')
            # считываем название предмета
            class_ = input('Введите предмет:_')
            new_class_ = input('Введите новый предмет:_ ')
            if class_ in students_marks[student].keys():
                # ====================================================
                # change

                students_marks[student][new_class_] = students_marks[student][class_]
                print(f'Для {student} предмет {class_} изменено на {new_class_}')
            else:
                print('ОШИБКА: не правельный придмет или студент не проходить такой придмет')

        elif "3" in command:
            print("Редактировать данные по ученикам")
            # считываем имя ученика
            student = input('Введите имя ученика:_')
            new_student = input('Введите имя нового ученика:_')
            if student in students:
                students[student] = new_student
                print(f'Студент {student} изменень на {new_student}')
            else:
                print('ОШИБКА: не правельный ввод имени студента или студент не регистрирован')



