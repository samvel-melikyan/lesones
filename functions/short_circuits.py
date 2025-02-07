import time
from datetime import datetime

from numpy.ma.core import inner

from functions import *


def outer_function(param):
    def inner_function():
        print('Вложенная функция имеет доступ к <{}>'.format(param))
    return inner_function  # Возвращаем ссылку на функцию

x = outer_function('Some_Parameter')  # В x теперь хранится ссылка на объект-функцию
x()  # Вызываем её
# Вложенная функция имеет доступ к <Some_Parameter>

print("""Замыкание в Python — это функция, которая динамически генерируется другой функцией 
и изменяет или использует значения переменных, которые были созданы внешней функцией.
""")
print("Если же функция внутри другой функции не использует переменные внешней функции, то это не принцип замыкания")
def outer_function(param):
    def inner_function():
        print('Вложенная функция имеет доступ к <{}>'.format(param))
    return inner_function

x1 = outer_function('Some_Parameter_1')
x2 = outer_function('Some_Parameter_2')
x1()
x2()
# Вложенная функция имеет доступ к <Some_Parameter_1>
# Вложенная функция имеет доступ к <Some_Parameter_2>
print("""
By using short-circuits we can once authenticate in server and because the inner function that is 
the return 'object' of the outer function, remembers data that has given him, use that data, by having short circuit - 
reference to exact inner function from global scope""")
short_line()
# Сначала создайте внешнюю функцию и имитируйте аутентификацию:
import random
print("""# import random 
def authenticate(user, password):
     session_id = random.randint(1000, 9999)
     print('User authorized: {} {}'.format(user, password))
     print('Session ID: {}'.format(session_id))
     return session_id

 def create_test(user, password):
     session_id = authenticate(user, password)  # Предположим, что функция authenticate возвращает идентификатор сессии после аутентификации
    # В этом моменте у нас есть идентификатор сессии, который мы хотим использовать в наших тестах.""")

# Затем перейдите к созданию вложенной функции:

print("""def authenticate(user, password):
    session_id = random.randint(1000, 9999)
    print('User authorized: {} {}'.format(user, password))
    print('Session ID: {}'.format(session_id))
    return session_id

def call_api(endpoint, session_id):
    print('Called {} with {}...'.format(endpoint, session_id))
    return 1 # Пока что всегда будем возвращать единицу как успешный ответ

def create_test(user, password):
    session_id = authenticate(user, password)  # Предположим, что функция authenticate возвращает идентификатор сессии после аутентификации
    # В этом моменте у нас есть идентификатор сессии, который мы хотим использовать в наших тестах.
    def test_func(endpoint, expected_result):
        # Предположим, что функция call_api вызывает API с заданным идентификатором сессии
        response = call_api(endpoint, session_id)
        # Здесь мы используем идентификатор сессии, полученный на первом шаге.
    return test_func()""")
# Верните внутреннюю функцию из внешней:
def authenticate(user, password):
    session_id = random.randint(1000, 9999)
    print('User authorized: {} {}'.format(user, password))
    print('Session ID: {}'.format(session_id))
    return session_id

def call_api(endpoint, session_id):
    print('Called {} with {}...'.format(endpoint, session_id))
    return 1 # Пока что всегда будем возвращать единицу как успешный ответ

def create_test(user, password):
    session_id = authenticate(user, password)  # Предположим, что функция authenticate возвращает идентификатор сессии после аутентификации
    # В этом моменте у нас есть идентификатор сессии, который мы хотим использовать в наших тестах.
    def test_func(endpoint, expected_result):
        # Предположим, что функция call_api вызывает API с заданным идентификатором сессии
        response = call_api(endpoint, session_id)
        # Здесь мы используем идентификатор сессии, полученный на первом шаге.
        assert response == expected_result, f"Expected {expected_result}, got {response}"

    return test_func  # Возвращаем функцию теста

#  И, наконец, проверьте работоспособность вашей функции. Вы увидите, что такая реализация позволяет сохранять идентификатор сессии:

# Создаем функцию теста для определенного пользователя
test = create_test('user', 'password')

# Запускаем тесты
test('/endpoint1', 1)
test('/endpoint2', 1)
# И теперь все эти тесты используют тот же идентификатор сессии, который был получен при вызове функции create_test!

# Вывод:
# User authorized: user password
# Session ID: 1364
# Called /endpoint1 with 1364...
# Called /endpoint2 with 1364...


new_line("Incapsulation")
def make_account(balance):
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance -= amount
        return balance

    return deposit, withdraw

deposit, withdraw = make_account(100)
print(deposit(15))
# 115
print(withdraw(30))
# 85



print("Верно. Если вложенная функция не ссылается на значения из объемлющей функции, то это просто функция внутри другой функции, а не замыкание.")


def create_unique_checker():
    meanning = set()
    def inner(char):
        nonlocal meanning
        len_data = len(meanning)
        meanning.add(char)
        if len(meanning) > len_data:
            return True
        else:
            return False

    return inner
    #
    # def create_unique_checker():
    #     seen = set()
    #     def checker(value):
    #         if value in seen:
    #             return False
    #         else:
    #             seen.add(value)
    #             return True
    #
    #     return checker


# new_line()
# def timer():
#     local_time = ""
#     def inner():
#         nonlocal local_time
#         local_time = datetime.now().strftime("%S")
#         return int(local_time)
#     return inner
import time

def timer():
    start = time.time()

    def elapsed():
        nonlocal start
        end = time.time()
        elapsed = end - start
        start = end
        return elapsed

    return elapsed

# my_timer = timer()
# t1 = int(my_timer())
# print(t1)
# time.sleep(1)
# t2 = int(my_timer())
# print(t2)
# to_test = t2 - t1
# print(to_test)

elapsed_timer = timer()

print("Test 1: No wait")
time.sleep(0.5)
print(round(elapsed_timer(), 1))


# m = datetime.now().strftime("%H:%M:%S")
# print(datetime.now().strftime("%H:%M:%S"))
# print(type(m))

new_line()
import random

def create_password_generator(length, symbols):
    used_passwords = set()

    def generator():
        nonlocal used_passwords
        while True:
            password = ''.join(random.choice(symbols) for _ in range(length))
            if password not in used_passwords:
                used_passwords.add(password)
                return password

    return generator
