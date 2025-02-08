from functions import *

new_section("Functools")
new_line("lru_cache")
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

new_line("patrial")

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


new_line("reduce")


print("functools.reduce(function, initializer)")
print("""Первый аргумент функции, function — это бинарная функция, которая принимает два аргумента, 
итерируемый аргумент — это последовательность (например, список или кортеж) элементов для сокращения, 
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
# False""")




