from datetime import datetime
from typing import List, Dict, Any

from lesones.functions.functions import new_line

print("----  Task N1   ----")


def calculate_age(birth_date: str) -> int:
    """
    Calculates the age of a user based on their birth date.

    The function extracts the birth year, day, and month from the given birth date
    (formatted as "year-day-month") and compares it with the current date to
    determine the user's age.

    Age is calculated as the difference between the current year and birth year,
    with adjustments based on whether the birth month and day have passed in the
    current year.

    Example:
        calculate_age("2000-08-02") -> 24 (if the current date is after August 2, 2024)

    :param birth_date: The birth date in the format "YYYY-DD-MM".
    :return: The user's age as an integer.
    """
    b_year, b_day, b_month = map(int, birth_date.split('-'))
    year, day, month = map(int, datetime.now().strftime("%Y-%d-%m").split('-'))
    if b_month < month:
        return int(year) - int(b_year)
    elif b_month > month:
        return int(year) - int(b_year) - 1
    elif b_month == month:
        if b_day == day or b_day < day:
            return int(year) - int(b_year)
        elif b_day > day:
            return int(year) - int(b_year) - 1



def filter_adults(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    This function filters and returns in the list only adult users.
    Using filter function and converting it into a list.
    Lambda function in the filter function checks a condition, that if a user's age is greater then or equal to 18,
    to get the age of user used function calculate_age().

    :param users: is a list with the user data that every element is a dictionary with the key : value -
    {'first_name': str, 'last_name': str, 'birth_date': str (in format - yyyy-dd-mm)}
    :return: a list only with user datas that are adults
    """
    return list(filter(lambda x: calculate_age(x['birth_date']) > 18, users))


def generate_username(first_name: str, last_name: str) -> str:
    """
    Generates a username based on the user's first and last name.

    The username is created using the first letter of the first name (in lowercase),
    followed by a dot (.), and then the entire last name in lowercase.

    Example:
        generate_username("John", "Doe") -> "j.doe"

    :param first_name: The first name of the user.
    :param last_name: The last name of the user.
    :return: A formatted username in the pattern "{first_initial}.{last_name}".
    """
    return f"{first_name[:1].lower()}.{last_name.lower()}"


# print(calculate_age("1990-05-15"))
# # 33
# users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15'},
#               {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22'},
#               {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01'}]
#
# print(filter_adults(users_data))
# print(generate_username("John", "Doe"))
users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '2020-05-15'},
              {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22'},
              {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01'}]
to_test = [calculate_age("1945-06-06"), filter_adults(users_data), generate_username("Lev", "Sergeev")]
# print(to_test)

new_line()
from datetime import date
from typing import List, Dict, Any

def calculate_age(birth_date: str) -> int:
    birth_date = date.fromisoformat(birth_date)
    print(birth_date)
    today = date.today()
    print(today)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def filter_adults(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    adults = [user for user in users if calculate_age(user['birth_date']) >= 18]
    return adults

def generate_username(first_name: str, last_name: str) -> str:
    username = f"{first_name[0].lower()}.{last_name.lower()}"
    return username

# print(calculate_age("2001-22-04"))


print("----  Task N2   ----")

def convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]:
    return list(map(lambda x: f"{x['first_name']} {x['last_name']}", users))

def find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> set:
    result =  {x['email'] for x in users1 if any(x['email'] == y['email'] for y in users2)}
    return result

def combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    result = dict()
    for i in users[0].keys():
        result[i] = tuple(map(lambda x: x[i] ,users))
    return result

users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'},
             {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22', 'email': 'bobJ@gmail.com'},
             {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01', 'email': 'lev46@gmail.com'}]

users_data_ext = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'}]

# print(convert_to_full_name(users_data))
# ['John Doe', 'Bob Johnson', 'Lev Sergeev']
# print(find_matching_emails(users_data, users_data_ext))
# {'johndoe@gmail.com'}
# print(combine_user_data(users_data))
# {'first_name': ('John', 'Bob', 'Lev'), 'last_name': ('Doe', 'Johnson', 'Sergeev'), 'birth_date': ('1990-05-15', '1985-10-22', '2015-01-01'), 'email': ('johndoe@gmail.com', 'bobJ@gmail.com', 'lev46@gmail.com')}
from typing import List, Dict, Any
from functools import reduce

def convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]:
    full_names = list(map(lambda user: f"{user['first_name']} {user['last_name']}", users))
    return full_names

def find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> set:
    emails1 = set(map(lambda user: user['email'], users1))
    emails2 = set(map(lambda user: user['email'], users2))
    matching_emails = emails1.intersection(emails2)
    return matching_emails

def combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    keys = users[0].keys()
    combined_data = dict(zip(keys, zip(*[user.values() for user in users])))
    return combined_data

print("----  Task N3   ----")

import time
from typing import Callable

def time_it(func: Callable):
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        duration = int(round(time.time() - start_time, 1))
        print(f"Execution time of '{func.__name__}': {duration} seconds")
        return duration
    return inner

print("----  Task N4   ----")
import warnings

warnings.filterwarnings('ignore')
from typing import List


def log_filter(logs: str, log_level: str):
    logs_list = logs.split('\n')
    return [x for x in logs_list if log_level in x ]

def log_filter(logs_string, log_level):
   for line in logs_string.split('\n'):
       if line and log_level in line:
           yield line.strip()
# used yield unlike me
logs = "2023-08-15 14:15:24 INFO Starting the system.\n2023-08-15 14:15:26 WARN System load is above 80%.\n2023-08-15 14:15:27 ERROR Failed to connect to database.\n2023-08-15 14:15:28 INFO Connection retry in 5 seconds.\n"
to_test = list(log_filter(logs, log_level="ERROR"))

print(to_test)


print("----  Task N5   ----")

categories = {
   "Электроника": {
       "Телефоны": {
           "Смартфоны": {},
           "Проводные": {}
       },
       "Компьютеры": {
           "Ноутбуки": {},
           "Стационарные": {
               "Игровые": {},
               "Для работы": {}
           }
       }
   },
   "Одежда": {
       "Мужская": {
           "Джинсы": {},
           "Куртки": {}
       }
   }
}


def category_dict(dict_names: Dict, parent_path: str) -> List:
    if dict_names.value < 0:
        return False
    # Рекурсия
    for child in dict_names.children:
        if not category_dict(child):
            return False
    return True



def extract_categories(category_dict, parent_path=''):
   paths = []
   for category, subcategories in category_dict.items():
       current_path = f"{parent_path} > {category}" if parent_path else category
       paths.append(current_path)
       paths.extend(extract_categories(subcategories, current_path))
   return paths



















