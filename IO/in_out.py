import random

from functions.functions import *

new_section("open()")

print("""
Для открытия файла используется функция open(). Эта функция имеет два аргумента:

open(file, mode="a")

    аргумент file принимает строку, в которой указан путь к файлу;
    аргумент mode принимает режим, в котором необходимо открыть файл.
""")
print("""
    'r' — открывает файл для чтения. Возвращает ошибку, если указанный файл не существует (задан по умолчанию).
    'w' — открывает файл для записи, причем перезаписывает содержимое, если оно есть. Создает файл, если он не существует.
    'a' — открывает файл для записи и добавляет новую информацию, не перезаписывая существующую. Создает файл, если он не существует.
    't' — открывает как текстовый файл (задан по умолчанию).
    'b' — открывает как двоичный файл.
    '+' — работа с файлом и в режиме чтения, и в режиме записи.
    
    
    
    't' — текстовые, в которых записаны человекочитаемые символы. Такие файлы можно прочитать и редактировать через блокнот и другие стандартные текстовые редакторы.
    'b' — бинарные (двоичные), в которых данные отображаются в закодированной форме с использованием нулей (0) и единиц (1) вместо простых символов.


Если не указывать тип файла, по умолчанию Python работает с текстовыми файлами. 
Для работы с изображениями, мультимедийными файлами и документами формата .pdf нужно указывать, что тип файла относится к бинарным — 'b'.
""")
print("""Открыть файл для работы можно двумя способами:

        Используя функции open(). После завершения работы с файлом нужно закрыть его с помощью close():

        f = open('file.txt', 'a')
        ...
        f.close()

        С помощью менеджера контекста with, который автоматически и самостоятельно закроет файл, после завершения работы с ним:

        with open('file.txt', 'a') as f:
            ...

""")


line("reading from file")
print("""
with open('file.txt', 'r') as f:
    text = f.read()
    
В этом случае в переменной text будет записано содержимое файла целиком.""")

print("""
with open('file.txt', 'r') as f:
    text = f.read(16)

В этом случае в переменной text будут записаны первые 16 символов текста, 
а курсор будет стоять на 17-м символе. Тогда при применении этой функции еще раз, считается следующая часть текста.""")
short_line("coursor")
print("""Также курсор можно сдвинуть на определенную позицию методом seek():

with open('file.txt', 'r') as f: # 'Hello, world!'
    first_part = f.read(8)       # 'Hello, w'
    f.seek(4)
    second_part = f.read(8)      # 'o, world'""")

print("""
В-третьих, можно считывать файл построчно. С помощью метода readline() считывается строка и курсор сдвигается на следующую строку. Таким образом можно считывать строки по порядку.

with open('file.txt', 'r') as f: 
    first_line = f.readline()    # первая строка
    second_line = f.readline()   # вторая строка""")
print("""
В-четвертых, можно прочитать файл целиком, а каждую строку записать в список. Этот список можно использовать как итерируемый объект в цикле:

with open('file.txt', 'r') as f:
    for line in f.readlines():
        print(line)
        ------------------------------------------ or
with open('file.txt', 'r') as f:
    for line in f:
        print(line)""")


line("Запись в файл")

print("тобы записать данные в файл, используют функцию write():")
print("""
with open('file.txt', 'w') as f:
    f.write('text')   # srting""")

print("""Также записывать в файл данные можно построчно с помощью метода writelines(), например, если у вас большой объем информации в виде списка строк:

with open('file.txt', 'w') as f:
    f.writelines(list_of_strings)
""")
print("""
Записать данные в файл можно и с помощью функции print(), передав в нее аргумент file:

with open('file.txt', 'w') as f:
    print(some_data, file=f)
    
В этом случае в print() можно передавать не только строковые аргументы, но и, например, числа — функция сама их преобразует к строковому тип""")
line()

def generate_text():
    word_count = random.randint(5,20)
    words = [
        "tree", "ocean", "mountain", "river", "valley", "desert", "thunderstorm", "waterfall", "sunset", "sunrise",
        "computer", "smartphone", "processor", "algorithm", "database", "encryption", "network", "software", "hardware",
        "automation",
        "pizza", "burger", "pasta", "chocolate", "strawberry", "avocado", "cheesecake", "coffee", "pancake", "cinnamon",
        "happiness", "sadness", "excitement", "frustration", "anger", "relief", "curiosity", "anxiety", "nostalgia",
        "surprise",
        "run", "jump", "swim", "dance", "whisper", "explore", "create", "destroy", "build", "analyze"
    ]

    random_words = random.choices(words, k=word_count)
    return " ".join(random_words) + "."


file = "C:/Users/User/PycharmProjects/SkillFactory/IO/file_to_test.txt"
with open(file, 'a') as f:
    f.write(generate_text())


with open(file, 'r') as f:
    print(f.read(10))

new_section("refferance")
line("path")
print("""
Корректно указать путь можно тремя способами:

    с помощью r-строк: r'"""r'C:\Users\Liudmila\Python\file.txt'"""'
    с помощью двойных обратных слэшей: 'C:\\Users\\Liudmila\\Python\\file.txt'
    с помощью одинарных слешей: 'C:/Users/Liudmila/Python/file.txt'

Чаще всего использует первый вариант описания пути к файлу — с помощью r-строк.""")

line("working with directory")
print("Для работы с файлами и директориями в Python используют модуль os")
short_line("get current directory path")
print("""
Метод getcwd() возвращает путь к текущей рабочей директории в виде строки:

import os
print(os.getcwd())""")
short_line("get list of files")
print("""
Чтобы получить список всех файлов и директорий текущего рабочего каталога, используется метод os.listdir():

import os
print(os.listdir())
""")
short_line("create directory")
print("""Для создания новой директории используется метод os.mkdir(). В метод нужно передать полный путь до новой директории:

import os
cwd = os.getcwd() # 'C:\\Users\\Liudmila\\Python'
new_dir = 'test'
path = os.path.join(cwd, new_dir) # генерируем путь до новой папки
os.mkdir(path) # создаем новую папку
print(os.listdir())
""")

line("working with files")
print("""Теперь давайте рассмотрим работу с файлами внутри директорий. 
Для этого будем использовать модуль shutil, который содержит набор функций для обработки файлов и папок. 
Функции позволяют копировать, перемещать и удалять файлы и папки.""")
short_line("copy")
print("""
Для копирования файлов используется метод shutil.copy(), который принимает два аргумента — путь до файла и директорию, в которую нужно скопировать файл:

import shutil
path = r'"""'C:/Users/Liudmila/Python/test'"""'
file = r'"""'C:/Users/Liudmila/Python/file.txt'"""'
copy_file = shutil.copy(file, path)

Здесь мы поместили копию файла file.txt в папку test.""")

print("Также можно скопировать сразу всё содержимое каталога с помощью метода shutil.copytree():")
print("""
import shutil
path = '...\Liudmila\Python'
new_path = '...\Liudmila\Python\ test'
copy_dir = shutil.copytree(path, new_path)

В этом примере содержимое папки Python скопировалось и переместилось в папку test.""")
short_line("move")
print("""
Для перемещения файлов используется метод shutil.move():

import shutil
path = '...\Liudmila\Python'
new_path = '...\Liudmila\Python\ test'
dir = shutil.move(file, path)

Здесь мы переместили файл file.txt в папку test.""")
short_line("delete directory")
print("""Для удаления директории вместе со всеми файлами используют shutil.rmtree():

import shutil
path = r'...\Liudmila\Python\ test'
shutil.rmtree(path)""")
short_line("delete file")
print("""
Для удаления файлов используют метод os.remove():

import os
path = """''r'C:\Users\Liudmila\Python\ file.txt'''"""
os.remove(path)""")


line()
print('Copy and paste a file')
import shutil
import os

cwd = os.getcwd()
new_dir = 'copy_here'
path = os.path.join(cwd, new_dir) # генерируем путь до новой папки

if new_dir in os.listdir(cwd):
    pass
else:
    os.mkdir(path) # создаем новую папку
    shutil.copy(file, path)
    os.remove(file)
print(os.listdir())





























