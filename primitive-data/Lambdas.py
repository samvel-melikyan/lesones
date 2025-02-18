def new_section(header):
    print(f"\n======================== {header.upper()} =====================\n")
def new_line(paragraph=""):
    print(f"\n----------------------- {paragraph} -----------------------")
def short_line():
    print("---------------------------")
new_section("lambda")

print("""lambda param1, param2, ... : command""")
print("lambda x, y: x**y")
print("""usagee:
f = lambda x, y: x**y""")
print("""print(f(2, 5))""")
f = lambda x, y: x**y
print(f(2, 5))
funcs = [lambda *args : sum(args) / len(args), lambda x, y : x**y]
short_line()
print("> funcs = [lambda *args : sum(args) / len(args), lambda x, y : x**y]")
print(funcs[0](15, 30, 24))
print(funcs[1](2, 8))

new_line("Передача lambda-функций в качестве аргумента функциям высшего порядка".upper())
new_line("Функция sorted")

print("""В Python функция sorted() применяется для сортировки итерируемых объектов. Синтаксис её вызова в общем случае выглядит так:
sorted(iterable, *, key=None, reverse=False)""")
x = [15, -125, 0, 0.3]
x = sorted(x)
print(x)
short_line()

people = [
   {'name': 'Анна', 'age': 20},
   {'name': 'Борис', 'age': 25},
   {'name': 'Виктор', 'age': 19}
]

def get_age(person):
   return person['age']

sorted_people = sorted(people, key=get_age) # sort by keys that will be iterated by sorted() function, mentioned array and keys
print(sorted_people)
print("\n> классические функции предполагают выполнение больших наборов инструкций, "
      "причём многократно, а здесь — всего лишь получение значения по ключу для единичного словаря.")
# lambda with sorted
sorted_people = sorted(people, key=lambda person: person['age']) # key= here is a logic of get_age function, but as argument to sorted() function -> in lambda function
print(sorted_people)
short_line()
new_line("lambda-функции для быстрой обработки данных".upper())
test_results = [
   {'name': 'test1', 'status': 'fail', 'time': 2.5},
   {'name': 'test2', 'status': 'pass', 'time': 1.1},
   {'name': 'test3', 'status': 'fail', 'time': 3.1},
   {'name': 'test4', 'status': 'pass', 'time': 0.9}
]
print("""for result in test_results:
   result['status'] = (lambda x: x == 'pass')(result['status'])""")
for result in test_results:
   result['status'] = (lambda x: x == 'pass')(result['status'])
print("""При этом наша лямбда-функция заключена в круглые скобки — так мы группируем выражения, чтобы интерпретатор Python нас правильно понял. А зачем мы группируем выражения? 
Потому что мы сразу хотим вызвать нашу лямбда-функцию. Идущая следом запись (result['status']) — это вызов функции и передача ей в качестве аргумента result['status']""")
short_line()
new_line("Использование lambda-функции вместе с классическими функциями".upper())
test_reports = [
   {'name': 'test1', 'status': 'fail', 'time': 2.5, 'details': {'error': 'NullPointerException', 'attempt': 1}},
   {'name': 'test2', 'status': 'pass', 'time': 1.1, 'details': {'attempt': 1}},
   {'name': 'test3', 'status': 'fail', 'time': 3.1, 'details': {'error': 'AssertionError', 'attempt': 2}},
   {'name': 'test4', 'status': 'pass', 'time': 0.9, 'details': {'attempt': 1}}
]
print("""Ваша задача заключается в том, чтобы создать функцию, которая принимает список отчетов и функцию извлечения, 
и возвращает список значений, которые вам нужны. Это может быть полезно, например, при сборе определенных метрик или при анализе результатов тестов.""")
def extract_data(reports, extraction_func):
   # Применяем переданную функцию к каждому словарю и генерируем новый список
   return [extraction_func(report) for report in reports]
execution_times = extract_data(test_reports, lambda x: x['time'])
print(execution_times)
attempt_counts = extract_data(test_reports, lambda x: x['details']['attempt'])
print(attempt_counts)


new_line("CW1")
strings = ["apple", "banana", "cherry", "date", "elderberry"]

def sort_strings_by_last_char(string):
    sorted_sring = sorted(string, key= lambda p: p[-1:])
    return sorted_sring

print(sort_strings_by_last_char(strings))
new_line("CW2")

def apply_function(numbers, func):
    return [func(num) for num in numbers]
short_line()
print("""def apply_function(list, func):
    return [func(element) for element in list] -> [-logic-] means that this logic will be applyed to every element in the list and as result will be returned a new list""")
short_line()
print("""- Перебирает каждый элемент num в списке numbers.
- Применяет функцию func(num) к каждому элементу.
- Результаты собираются в новый список [].""")

numbers = [1, 2, 3, 4, 5]
print(apply_function(numbers, lambda x: x**2))

new_line("CW3")

def sort_by_age(list):
    return sorted(list, key=lambda elem: elem[1])
people = [("Anna", 23), ("John", 21), ("Alice", 25)]
print(sort_by_age(people))







