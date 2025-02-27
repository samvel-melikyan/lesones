import functools
from datetime import datetime

from functions.functions import *

new_section("Decorators 2.0")

print("""
Как же обернуть любую нашу функцию, заставив её работать вместе с декоратором? Для этого нужно сделать следующие вещи:

              1.  Создать функцию, код которой мы хотим декорировать.
              2.  Создать переменную, которую мы будем использовать в качестве декоратора.
""")


def my_decorator(func):
    def wrapper():
        print("Начало выполнения функции.")
        func()
        print("Конец выполнения функции.")

    return wrapper


#Эту функцию мы будем декорировать
def my_first_decorator():
    print("Это мой первый декоратор!")


my_first_decorator = my_decorator(my_first_decorator)
my_first_decorator()
short_line()


def working_hours(func):
    def wrapper():
        if 9 <= datetime.now().hour < 18:
            func()
        else:
            pass  # Нерабочее время, выходим

    return wrapper


def writing_tests():
    print("Я пишу тесты на python!")


writing_tests = working_hours(writing_tests)
writing_tests()
short_line()

# from decorators import do_twice
#
#
# @do_twice
# def _test_twice():
#     print("Это вызов функции test_twice!")


# _test_twice()

print("""Python предоставляет довольно мощный инструмент, называемый интроспекцией. С его помощью мы можем получить информацию о любом объекте. Для нашего примера будет достаточно возвращать имя функции:

@do_twice
def test_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))
    return "Done"

print(test_twice.__name__)

Но что произойдет сейчас, если мы вызовем такой код?

- wrapper

Наш декоратор сломал нам поведение интроспекции из-за того, что «берёт инициативу в свои руки». Чтобы избежать этого, достаточно переделать наш декоратор следующим образом:

def do_twice(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
      func(*args, **kwargs)
      return func(*args, **kwargs)
  return wrapper

и еще добавить импорт в файл, где находится функция-декоратор:

import functools

Теперь вызов print(test_twice.__name__) выведет корректную информацию об имени функции.""")


def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


@do_twice
def _test_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))
    return "Done"

short_line()
print(_test_twice.__name__)
line("Debugger")

import functools

def debug(func):
    """Выводит сигнатуру функции и возвращаемое значение"""
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Вызываем {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} вернула значение - {value!r}")
        return value
    return wrapper_debug


@debug
def age_passed(name, age=None):
  if age is None:
    return "Необходимо передать значение age"
  else:
    return "Аргументы по умолчанию заданы!"

age_passed("Роман")
age_passed("Роман", age=21)