import time
import random

from functions import *

new_section("Decorators")
print("Декоратор — это функция, которая позволяет модифицировать и расширять поведение функций и методов, не меняя их код .")

def decorator(func):
	print("Делаем что-то перед вызовом функции — изменяем её поведение")
	func()
	print("Делаем что-то после вызова функции — изменяем её поведение")

# Делаем "основную" функцию, поведение которой будем менять
def demo_func():
	print('Работает целевая функция')

changed_function = decorator(demo_func)
# После этой строчки выведется следующее:
# Делаем что-то перед вызовом функции — изменяем её поведение
# Работает целевая функция
# Делаем что-то после вызова функции — изменяем её поведение

## changed_function()
# А попытка "восп   ользоваться" нашей измененной функций вообще приведёт к ошибке
# TypeError: 'NoneType' object is not callable


new_line()
print("> Здесь мы и приходим к тому, что для реализации такого функционала понадобится принцип замыкания.")

def decorator(func):
    # Реализуем принцип Замыкания
    def wrapper():
        print("Делаем что-то перед вызовом функции -- изменяем её поведение")
        func()
        print("Делаем что-то после вызова функции -- изменяем её поведение")
    return wrapper

# Делаем "основную" функцию, поведение которой будем менять
def demo_func():
    print('Работает целевая функция')

changed_function = decorator(demo_func)

changed_function()
# Делаем что-то перед вызовом функции -- изменяем её поведение
# Работает целевая функция
# Делаем что-то после вызова функции -- изменяем её поведение

new_line("giving parameter to decorator function")
def decorator(func):
    def wrapper(parameter):
        print("Делаем что-то перед вызовом функции -- изменяем её поведение")
        func(parameter)
        print("Делаем что-то после вызова функции -- изменяем её поведение")
    return wrapper

def demo_func(parameter):
    print('Работает целевая функция c параметром(-ами):')
    print(parameter)

changed_function = decorator(demo_func)

changed_function('Параметр декорированной функции')
# Делаем что-то перед вызовом функции -- изменяем её поведение
# Работает целевая функция c параметром(-ами):
# Параметр декорированной функции
# Делаем что-то после вызова функции -- изменяем её поведение

short_line()
print("""
Вот теперь всё работает как надо за одним исключением — наш код снова перестанет работать, как только у оригинальной функции изменится количество параметров:""")

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Делаем что-то перед вызовом функции -- изменяем её поведение")
        func(*args, **kwargs)                                 # using *args & **kwargs
        print("Делаем что-то после вызова функции -- изменяем её поведение")
    return wrapper

def demo_func(parameter1, parameter2):
    print('Работает целевая функция c параметром(-ами):')
    print(parameter1)
    print(parameter2)

changed_function = decorator(demo_func)

changed_function('Параметр декорированной функции_1',
                'Параметр декорированной функции_2')

# Делаем что-то перед вызовом функции -- изменяем её поведение
# Работает целевая функция c параметром(-ами):
# Параметр декорированной функции_1
# Параметр декорированной функции_2
# Делаем что-то после вызова функции -- изменяем её поведение

new_line("None return type")

print("""Если для текущей реализации мы попробуем получить возвращаемое значение, то ожидаемо получим 
None (помним, что если в функции не определён оператор return, то она по умолчанию возвращает None:""")

print("нам нужно будет определить оператор return и в wrapper, так как «отрабатывает» именно он:")


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Делаем что-то перед вызовом функции -- изменяем её поведение")
        res = func(*args, **kwargs)
        print("Делаем что-то после вызова функции -- изменяем её поведение")
        return res + ' + Изменяем возвращаемое значение в wrapper'
    return wrapper

def demo_func(parameter1, parameter2):
    print('Работает целевая функция c параметром(-ами):')
    print(parameter1)
    print(parameter2)
    return 'Возвращаемое значение оригинальной функции'


changed_function = decorator(demo_func)

result = changed_function('Параметр декорированной функции_1',
                'Параметр декорированной функции_2')
print(result)

# Делаем что-то перед вызовом функции -- изменяем её поведение
# Работает целевая функция c параметром(-ами):
# Параметр декорированной функции_1
# Параметр декорированной функции_2
# Делаем что-то после вызова функции -- изменяем её поведение
# Возвращаемое значение оригинальной функции + Изменяем возвращаемое значение в wrapper

new_line("Prototype for Decorators")
print("""def decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wrapper""")
# У ваших декораторов будут свои имена, которые будут отражать их намерения
# То есть для их именования нужно руководствоваться теми же правилами, что
# и для функций
def decorator(func):
    # А вот вложенную функцию, если она одна, практически всегда
    # именуют wrapper -- общепринятое и неформальное соглашение
    def wrapper(*args, **kwargs):  # *args и **kwargs выступают параметрами в большинстве случаев, но это не обязательное правило
        # Здесь вы можете поместить свои инструкции, которые должны предшествовать
        # вызову оригинальной функции (а можете и не помещать -- всё зависит от ваших намерений)
        res = func(*args, **kwargs)
        # Здесь вы можете поместить свои инструкции, которые должны идти после
        # вызова оригинальной функции (а можете и не помещать -- всё зависит от ваших намерений)
        return res  # Сами решаем, возвращаем: оригинальное значение, измененное или вообще ничего
    return wrapper  # Реализуем принцип замыкания


new_section("Convenience of wrapping functions with decorators & > @ < operator ")
print("""
На самом деле, создание измененной функции путем вызова декоратора — не самый удобный и не общепринятый способ обертывания функций декоратором.
В Python есть специальный оператор «@» при помощи которого мы можем обернуть функцию декоратором прямо в её объявлении:""")
print("""\ndef decorator(func):
    def wrapper(*args, **kwargs):
        print("Отработал декоратор")
        res = func(*args, **kwargs)
        return res
    return wrapper

@decorator
def demo_func():
    print('Отработала оригинальная функция')
    
demo_func()""")
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Отработал декоратор")
        res = func(*args, **kwargs)
        return res
    return wrapper

@decorator
def demo_func():
    print('Отработала оригинальная функция')
print("\nИ теперь, если мы воспользуемся после этого нашей функций, то она автоматически уже будет обернута в декоратор:")
short_line()
demo_func()

# Отработал декоратор
# Отработала оригинальная функция


new_line("function work time")

print("""def large_sum(n):
    return sum(range(n))

def prime_numbers(n):
    primes = []
    for possiblePrime in range(2, n):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
        if isPrime:
            primes.append(possiblePrime)
    return primes""")

import time
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        work_time = time.time() - start_time
        print(f'Функция {func.__name__} отработала за {work_time} секунд')
        return res
    return wrapper
print("""
import time
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        work_time = time.time() - start_time
        print(f'Функция {func.__name__} отработала за {work_time} секунд')
        return res
    return wrapper
    """)
print("""Запись func.__name__: позволяет получать имя функции, когда у нас его по сути нет, 
и мы имеем только переменную, в которой содержится ссылка на эту функцию""")
@timeit
def large_sum(n):
    return sum(range(n))
@timeit
def prime_numbers(n):
    primes = []
    for possiblePrime in range(2, n):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
        if isPrime:
            primes.append(possiblePrime)
    return primes

short_line()

test_data = 193700

prime_numbers = prime_numbers(test_data)
# Функция prime_numbers отработала за 2.0152699947357178 секунд

result = large_sum(test_data)
# Функция large_sum отработала за 0.004996538162231445 секунд

@timeit
def power_sum(n, p):
    """Функция возвращает сумму первых n чисел, возведенных в степень p."""
    return sum(i**p for i in range(n))

result = power_sum(10000, 2)
# Функция power_sum отработала за 0.002002239227294922 секунд
print(result)
# 333283335000


# def timeit(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         work_time = time.time() - start_time
#         print(f'Функция {func.__name__} отработала за {work_time} секунд')
#     >   print(f'args: {args}')
#     >   print(f'kwargs: {kwargs}')
#         return res
#     return wrapper

@timeit
def prime_numbers(n):
    ...

for i in range(1, 10000, 2000):
    prime_numbers(i)

new_line("real case for QA engineer")

def retry_on_failure(func):
    max_retries = 3
    def wrapper(*args, **kwargs):
        for _ in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Function {func.__name__} failed with error: {e}. Retrying...")
                time.sleep(1)  # В реальном кейсе нам чаще всего надо будет подождать нек-ое кол-во времени
        print(f"Function {func.__name__} failed after {max_retries} retries.")
    return wrapper

@retry_on_failure
def fragile_function(*args, **kwargs):
    if random.random() < 0.5:  # В 50% случаев функция будет "Ломаться"
        raise Exception("An error occurred")
    else:
        return "Success"

# Запускаем функцию
print(fragile_function())

# Function fragile_function failed with error: An error occurred. Retrying...
# Function fragile_function failed with error: An error occurred. Retrying...
# Success
# Как мы видим, на третью попытку наша функция всё-таки отработала без ошибок и вернула "Success".
# А вот как выглядит случай, когда она всё же не смогла успешно выполниться и за три раза:

print(fragile_function())

new_line("Передача аргументов декораторам")


def retry_on_failure(max_retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Function {func.__name__} failed with error: {e}. Retrying...")
                    time.sleep(1)
            print(f"Function {func.__name__} failed after {max_retries} retries.")
        return wrapper
    return decorator

@retry_on_failure(max_retries=5)
def fragile_function(*args, **kwargs):

    if random.random() < 1:  # Специально делаем так, чтобы функция всегда поднимала ошибку
        raise Exception("An error occurred")
    else:
        return "Success"

# Запускаем функцию
print(fragile_function())
short_line()
print("""
    1.Создаём сам декоратор, который принимает аргументы в свои параметры;
    2.Создаём вложенность — decorator, который принимает целевую функцию;
    3.Создаём еще один уровень вложенности — wrapper, который принимает аргументы для целевой функции.
""")
short_line()
print("""
    1.Когда мы оборачиваем целевую функцию @retry_on_failure(max_retries=5) мы по сути вызываем функцию retry_on_failure и передаём ей значение аргумента.
    2.И вся магия происходит дальше: при этом функция, которую мы хотим декорировать, fragile_function автоматически передаётся как параметр func вложенной функции decorator.
    
    При этом все это выглядит довольно лаконично: 
    внешняя функция принимает аргументы, переданные декоратору, 
    вложенная функция принимает целевую функцию, 
    вложенная во вложенную функцию принимает аргументы для целевой функци.
""")
new_line("without @ operator")
def retry_on_failure(max_retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Function {func.__name__} failed with error: {e}. Retrying...")
                    time.sleep(1)
            print(f"Function {func.__name__} failed after {max_retries} retries.")

        return wrapper

    return decorator


def fragile_function(*args, **kwargs):
    if random.random() < 1:  # Специально делаем так, чтобы функция всегда поднимала ошибку
        raise Exception("An error occurred")
    else:
        return "Success"


decorated_func = retry_on_failure(max_retries=5)(fragile_function)
decorated_func()
print("""
decorated_func = retry_on_failure(max_retries=5)(fragile_function)
decorated_func()
                    or
decorator = retry_on_failure(max_retries=5)
fragile_function = decorator(fragile_function)""")


new_line()

import warnings

warnings.filterwarnings('ignore')


def retry_if_result_is_none(times=1):
    def decorator(func):
        def inner(*args, **kwargs):
            for i in range(times):
                if not None in args:
                    return args
                elif None in args:
                    continue
            return f"Получилось получить значение за {times} вызова"
        return inner
    return decorator

import random

random.seed(47)


@retry_if_result_is_none(times=2)
def test_function():
    return random.choice([None, "Passed"])


to_test = test_function()

print(to_test)













