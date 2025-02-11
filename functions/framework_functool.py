from functions import *

new_section("Functools")
line("lru_cache")
import time

def is_valid_email_without_lru_cash(email):
    # Фиктивно замедляем функцию
    time.sleep(2)

    if email.count("@") != 1:
        return False
    local_part, domain_part = email.split("@")
    if not local_part or not domain_part:
        return False
    if domain_part.count(".") != 1:
        return False

    return True


print("""Декоратор functools.lru_cache в Python предоставляет простой способ кэширования результатов вызовов функций. 
Он использует стратегию наименее недавно использованных (least-recently-used), что означает, что если кэш заполнен, 
он сначала отбрасывает наименее использовавшиеся элементы, чтобы освободить место для новых элементов.""")

short_line()

# Импортируем декоратор из библиотеки functools
from functools import lru_cache

# Добавляем декоратор к нашей функции
# Функция для проверки почты
@lru_cache
def is_valid_email(email):
    # Фиктивно замедляем функцию
    time.sleep(2)

    if email.count("@") != 1:
        return False
    local_part, domain_part = email.split("@")
    if not local_part or not domain_part:
        return False
    if domain_part.count(".") != 1:
        return False

    return True
start_time = time.time()
test_email = "example@example.com"
test_size = 10
for _ in range(test_size):
    result = is_valid_email(test_email)

print('With lru_cash\nTotal time: {}'.format(time.time()- start_time))
# Total time: 2.000363826751709
print()
start_time = time.time()
# for _ in range(test_size):
#     result = is_valid_email_without_lru_cash(test_email)
# print('Without lru_cash\nTotal time: {}'.format(time.time()- start_time))
# Total time: 20.003348112106323

for i in range(test_size):
    start_time = time.time()
    result = is_valid_email(test_email)
    print('Operation {} time: {}'.format(i, time.time()- start_time))
    ...

print('Total time: {}'.format(time.time()- start_time))

print("""Таким образом, когда вы впервые вызываете функцию c декоратором lru_cache, с определенным набором параметров, 
функция будет выполняться как обычно. Но если вы снова вызовете ту же функцию с теми же параметрами, 
Python извлечет результат из кэша, а не снова запустит функцию.""")

short_line("arguments")
print("""По умолчанию (когда мы не передаем декоратору аргументы) в нём содержатся следующие значения параметров:

@lru_cache(maxsize=128, typed=False)

Здесь maxsize отвечает за максимальный размер кэша, при этом если передать maxsize=None, 
то он сможет возрастать бесконечно (гипотетически, на деле — пока у вас не кончится память).

А если typed установить True, то вызовы функции с различными типами данных будут кэшироваться отдельно.

И подводя итоги: декоратор lru_cache может быть крайне полезен при тестировании сценариев, когда одну и ту же функцию 
нужно вызывать несколько раз с одними и теми же аргументами. Кэшируя результаты вызовов этих функций, мы можем значительно ускорить наши тесты.""")

line("patrial")

from functools import partial
def test_api(endpoint, method, params):
    print('Test started for {}...'.format(endpoint))
    # Остальной код для тестирования
    ...

# Создаем новую функцию, указывая исходную и какой параметр сделать статическим:
test_get = partial(test_api, method="GET")

# И теперь используем функцию без необходимости указания параметра method:
test_get(endpoint="/api/v1/users", params={})
test_get(endpoint="/api/v1/orders", params={})

# Test started for /api/v1/users...
# Test started for /api/v1/orders...

print("""
When we have a function with two arguments, but we have specific value for 
one argument, we can use partial function, specify function and as 2nd argument 
specify the argument we want to be same for a wile, and then use this variable which 
contains the modified function, and use it with one argument that can be changeed. 
""")


line("reduce")


print("functools.reduce(function, initializer)")
print("""Первый аргумент функции, function — это бинарная функция, которая принимает два аргумента, 
этитерируемый аргумент — о последовательность (например, список или кортеж) элементов для сокращения, 
а необязательный аргумент инициализатора initializer — это значение, которое используется в качестве первого аргумента при первом вызове функции

Одним из практических сценариев для QA-инженера, где пригодится reduce, 
может быть агрегирование результатов тестирования. Допустим, у нас есть несколько результатов тестов в виде логических значений в списке 
(True, если они пройдены, False, если они не пройдены), и мы хотим вынести окончательный вердикт, все ли тесты пройдены или нет.

Вот как мы могли бы сделать это без reduce:

test_results = [True, True, False, True, True]
all_passed = True
for result in test_results:
    all_passed = all_passed and result
print(all_passed)
# False

Теперь давайте посмотрим, как мы можем использовать функцию reduce, чтобы сделать то же самое более лаконично:

from functools import reduce
test_results = [True, True, False, True, True]
all_passed = reduce(lambda a, b: a and b, test_results)
print(all_passed)
# False


При этом вы справедливо могли вспомнить о функции all, которая еще сильнее упростит данную операцию:
test_results = [True, True, False, True, True]
all_passed = all(test_results)
print(all_passed) 
# False
--------------------
К выбору инструмента нужно подходить осознанно, разумеется, в контексте этого 
примера лучшим (в контексте читаемости и простоты) решением будет all, а функцию reduce в 
реальном мире стоит приберечь для более сложных примеров.

Так, например, если у нас есть список тестовых случаев следующего вида:
--------------""")
test_cases = [
    {'name': 'Test 1', 'passed': True, 'time': 1.0},
    {'name': 'Test 2', 'passed': False, 'time': 0.5},
    {'name': 'Test 3', 'passed': True, 'time': 1.5}
]
from functools import reduce

summary = reduce(
    lambda acc, test: {
        'total_time': acc['total_time'] + test['time'],
        'passed': acc['passed'] + (1 if test['passed'] else 0),
        'failed': acc['failed'] + (0 if test['passed'] else 1),
    },
    test_cases,
    {'total_time': 0.0, 'passed': 0, 'failed': 0}
)

print(summary)
# {'total_time': 3.0, 'passed': 2, 'failed': 1}

print("""Теперь благодаря декоратору lru_cache ваши функции станут работать еще быстрее, 
partial поможет вам гибко подстраиваться под существующие реализации, а 
reduce стал новым и мощным способом обработки и анализа данных.""")

short_line("Task N1 --- lru_cache")
"""Optimize the function's work"""

@lru_cache()
def calculate_factorial(n):
    """Функция вычисляет факториал числа n."""
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

@lru_cache()
def fibonacci(n):
    """Функция вычисляет число Фибоначчи для n."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
@lru_cache()
def calculate_power(base, exponent):
    """Функция вычисляет значение степени числа base в степени exponent."""
    return base ** exponent

short_line("Task N2 --- partial()")



def form_request(url, method='GET', headers=None, data=None, params=None):
    dict_ = {"headers": headers,
           "data": data,
           "params": params}
    return f"{url}-::-{method}-::-{dict_}"


form_post_request = partial(form_request, method='POST')

print(form_post_request('dummy_api'))
# dummy_api-::-POST-::-{'headers': None, 'data': None, 'params': None}


short_line("Task N3 --- reduce")

cart = [
    {'product_name': 'Мышка', 'price': 15.99},
    {'product_name': 'Клавиатура', 'price': 25.50},
    {'product_name': 'Наушники', 'price': 10.75}
]

def calculate_total_price(dict_list):
    return reduce(lambda x, y: x + y['price']  , dict_list, 0)


total_price = calculate_total_price(cart)
print(f"Общая стоимость товаров в корзине: ${total_price:.2f}")

print("""
reduce(function, iterable, initializer) is used to accumulate the total price.
function (lambda x, y: x + y['price']):
x: The accumulated total (starting at 0, because of the initializer).
y: Each dictionary (product) in cart.
y['price']: Extracts the price from the dictionary.
x + y['price']: Adds the price to the running total.""")
























