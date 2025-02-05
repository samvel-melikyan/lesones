import math

from functions import new_section, new_line, short_line

new_section("MAP()")

print("""map(function, iterable, ...)""")
print("""
    function — функция, которую необходимо применить к элементам итерабельного объекта.
    iterable — один или более итерабельных объектов (например, список, кортеж, множество).
""")
new_line("example")
print("""squared = map(lambda x: x**2, [1, 2, 3, 4])
print(list(squared))
# [1, 4, 9, 16]""")
short_line()
print("1 - map(int, [numbers in string], instead of ,ap(int(), [list]")
print("2 - returns interator")
numbers_int = map(int, ['1', '2', '3', '4'])
print(numbers_int)
print(list(numbers_int))
print("in one line")
numbers_int = list(map(int, ['1', '2', '3', '4']))

test_cases = [1, 0, -1, 2, -2]
result = list(map(lambda x: x > 0, test_cases))
print(result)
print("""Генератор:
Можно создать, просто определив функцию с оператором yield. Каждый раз, когда функция встречает yield, 
она «приостанавливает» свою работу, возвращая значение, и «продолжает» её при следующем вызове.""")

print("""Итератор:
Обычно создается путем определения класса, в котором реализованы методы __iter__() и __next__() — о чем было сказано в определении.""")

print("""Генератор:
Также не создает элементы заранее. Однако, благодаря механизму yield, он может сохранять свое состояние между вызовами, 
что позволяет эффективно работать с большими последовательностями без необходимости загружать все элементы в память""")
print("""
    Итератор:
    Подходит для более сложных и гибких структур данных или когда нужно реализовать специальное поведение при итерации.
    Генератор:
    Подходит для простых итераций, когда нужно быстро и лаконично определить итератор без создания отдельного класса.
""")

short_line()
print("""Task 1:
You are given a list of temperatures in Celsius. Write a Python program that converts these temperatures to Fahrenheit using the map() function. The conversion formula is:
F=(C×9/5)+32
""")
celsius_temperatures = [0, 20, 37, 100]
fahrenheit_temperatures = list(map(lambda x: (x*9/5)+32, celsius_temperatures))
print(f"Given : {celsius_temperatures}\nThe Result:",fahrenheit_temperatures)
print("""Task 2:
You are given a list of strings representing numerical values. Your goal is to:
    Convert the list of strings into a list of floating-point numbers.
    Round each number to 2 decimal places using map().""")
numbers = ["3.14159", "2.71828", "1.61803", "0.57721"]
result = list(map(lambda x: round(x, 2),list(map(float, numbers))))
print(f"Given : {numbers}\nThe Result is:",result)


new_section("FILTER")
new_line("filter()")

print("filter(function, iterable)")
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))
test_cases = [
   {"id": 1, "category": "UI", "description": "Тестирование интерфейса"},
   {"id": 2, "category": "Backend", "description": "Тестирование API"},
   {"id": 3, "category": "UI", "description": "Проверка элементов управления"},
]

ui_tests = filter(lambda x: x["category"] == "UI", test_cases)
print(list(ui_tests))
tests = [
   {"name": "test_login", "executed": True},
   {"name": "test_registration", "executed": False},
   {"name": "test_password_reset", "executed": True},
   {"name": "test_profile_update", "executed": False},
]
excecute_tests = filter(lambda x: x["executed"], tests)
print(list(excecute_tests))

new_section("ZIP")
new_line("zip()")
print("zip(*iterables)")
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 88]
paired = zip(names, scores)
print(list(paired))

print("> zip() can be helpful with comparing data, for example if we have a expected results and we need to compare it with the actual result")
expected = [200, 404, 500]
actual = [200, 404, 500.05]
for e, a in zip(expected, actual):
   if e != a:
       print(f"Expected {e}, but got {a}")
print("> By using zip() we can easy combine two list of data into a dictionary")
headers = ["name", "age", "gender"]
row = ["Alice", 28, "Female"]
user_data = dict(zip(headers, row))
print(user_data)

new_section("ALL & ANY")
new_line("any()")
print("function any() returns True if one of the elements of iterable object is True"
      "\nvalues = [False, False, True, False]")
values = [False, False, True, False]
result = any(values)
print(result)
new_line("all()")
print("function all() returns True if all the elements of iterable object is True otherwise returns False"
      "\nvalues = [False, False, True, True]")
values = [False, False, True, True]
result = all(values)
print(result)
data = [3, 1, 9, 7]
assert all(x > 0 for x in data), "Not all elements are positive"
# Ошибки нет, все числа положительные
# assert any(x == 5 for x in data), "The value 5 is not in the list"
# AssertionError: The value 5 is not in the list


errors = ["", "", "Page not found", ""]
# assert not any(errors), "There were errors during testing!"
test_results = [True, True, True, True]
assert all(test_results), "Not all tests passed!"

data = [0, 1, 2, 3]
contains_positive = any(num > 0 for num in data)


print("""
Тренажер не умеет работать с input - система уйдет в бесконечную загрузку.

Условие: QA-инженерам часто приходится проверять, как система реагирует на разные типы данных. Допустим, у вас есть форма регистрации на сайте, где одним из полей является «Телефон». Вы хотите проверить, обрабатывается ли введенный телефон корректно.
Пусть у вас есть список номеров телефонов в разных форматах:

['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890'].

Напишите функцию format_phone_number, которая с помощью filter приводит номер к единому формату: 1234567890.
А затем в formatted_numbers с помощью map сохраните результат применения функции format_phone_number к списку phone_numbers.""")


phone_numbers = ['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890']
def format_phone_number(phone_list):
    return "".join(filter(lambda x: x.isdigit(), phone_list))
formatted_numbers = list(map(format_phone_number, phone_numbers))
print(formatted_numbers)

new_line()

print("""Условие: У вас есть два списка: один с ожидаемыми результатами тестов, и второй с фактическими результатами тестов. Напишите функцию compare_test_results, 
которая принимает оба списка и возвращает список булевых значений (True или False), показывающих, совпадает ли ожидаемый результат с фактическим для каждого теста. """)
def compare_test_results(expected, actual):
    def sec():
        for i,j in zip(expected, actual):
            if i == j:
                yield True
            else:
                yield False
    return list(sec())

def compare_test_results1(expected, actual):
   return [exp == act for exp, act in zip(expected, actual)]






















