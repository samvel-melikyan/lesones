from functions import *
new_section("annotations and docstrings")
print("def is_valid_email(email: str):")
print("""Если с визуальной чистотой мы начали работать — добавили аннотацию параметру email, 
то техническая требует доработки, например, чтобы не рушить программу, мы будем возвращать None, 
если не получили ожидаемого типа:""")
print("""def is_valid_email(email: str):
    if type(email) != str:
        return None
    
    if email.count("@") != 1:
        return False
    local_part, domain_part = email.split("@")
    if not local_part or not domain_part:
        return False
    if domain_part.count(".") != 1:
        return False

    return True""")
print("def имя_функции(параметр1: ссылка_на_тип, параметр2: cсылка_на_тип, ...):")

print("""азобравшись с базовой аннотацией параметров, можно задаться очевидным вопросом — 
наверное можно как-то аннотировать тогда и тип возвращаемого значения?

Ответ — да, можно, для этого давайте вернёмся к той же функции для валидации почты. 
Тип возвращаемого значения в ней еще более неочевиден.
def имя_функции(параметр: ссылка_на_тип) -> ссылка_на_тип:
    ... 
-----------------------------------------
def is_valid_email(email: str) -> bool:
    if email.count("@") != 1:
        return False
    local_part, domain_part = email.split("@")
    if not local_part or not domain_part:
        return False
    if domain_part.count(".") != 1:
        return False

    return True

multiple annotations for changeable variable type

def calculate_power(base: int | float, exponent: int | float) -> int | float:
    return base ** exponent

""")
print(""" Using typing ---------------

from typing import Union

def calculate_power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    return base ** exponent

from typing import Union

def weighted_average(x: list[Union[int, float]], w: list[Union[int, float]]) -> float:
    return sum(a*b for a,b in zip(x, w))/sum(w)
    
> in Python 3.9
from typing import List, Union

def weighted_average(x: List[Union[int, float]], w: List[Union[int, float]]) -> float:
    return sum(a * b for a, b in zip(x, w)) / sum(w)

Для возвращаемого значения все делается точно так же, как и для параметра:
def count_letters(words: dict[str, int]) -> dict[str, int]:
	letter_count = {}
	for word in words:
    	for letter in word:
        	if letter in letter_count:
            	letter_count[letter] += 1
        	else:
            	letter_count[letter] = 1
	return letter_count

for python 3.9 and lower
from typing import Dict

def count_letters(word_list: Dict[str, int]) -> Dict[str, int]:
""")

line("Vector")
print("""
Vector = list[float]
vector1 = [1.0, 2.0, 1.0, 3.0]

И для чего нам это пригодится? Разумеется, для функций, которые будут работать с такими векторами, 
вот пример функции, которая меняет направление вектора:

def reflect(vector: Vector) -> Vector:
    return [ -num for num in vector]""")

line("Callable")
print("""
from typing import Callable

def apply_function(f: Callable[[int], str], x: int) -> str:
    return f(x)
Запись f: Callable[[int], str] говорит о том, что функция, которая передается в параметр f должна принимать 
один аргумент типа int, а возвращаемое значение должно быть типа str.

""")






line("iterable")
print("""Если наш объект итерируемый (например список или кортеж), то мы можем это также указать в аннотации. Это, очевидно, 
необходимо делать в случае, если по этому объекту в теле функции будут проходиться циклом.

Указать это можно при помощи того же модуля typing:

from typing import Iterable

def get_first_element(items: Iterable[int]) -> int:
    return next(iter(items))""")

from typing import Iterable

def process_data(data: Iterable[tuple[int, str]]) -> None:
    for number, name in data:
        print(f"Processing {name} with ID {number}")



new_section("Docstring")

print("""def is_valid_email(email):
    '''Check if an email is valid.'''
    
    При этом docstrings могут быть многострочными. 
    Обычно первая строка — это краткое описание того, что делает функция. 
    Затем следует пустая строка, а затем более подробное описание:
    
    example:    
    '''Check if an email is valid.

    This function takes a string representing an email address, and checks
    if it is formed correctly. An email is considered valid if it contains
    exactly one '@' symbol, and the domain part contains exactly one dot ('.').
    '''
И, наконец, заключительный и лучший вариант — это добавить в docstring еще более подробное описание параметров:
    '''
    Check if an email is valid.

    This function takes a string representing an email address, and checks
    if it is formed correctly. An email is considered valid if it contains
    exactly one '@' symbol, and the domain part contains exactly one dot ('.').

    :param email: The email address to check.
    :return: True if the email is valid, False otherwise.
    '''

""")

short_line("help() function")
print("Просматривать документационные строки мы можем прямо в коде "
      "(или же в Python Console, что более реалистичный вариант) при помощи функции help():")
print("help(is_valid_email)")















































