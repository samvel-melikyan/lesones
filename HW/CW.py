from lib2to3.pgen2.token import NUMBER

from functions import *


def is_valid_password(password, min_length=8, require_upper=True, require_lower=True, require_digit=True):
    if len(password) >= min_length:
        min_length = True
    else:
        min_length = False
    upper = 0
    if require_upper:
        for i in password:
            if i.isupper():
                upper += 1
        if upper == 0:
            require_upper = False
    else:
        require_upper = True
    lower = 0
    if require_lower:
        for i in password:
            if i.islower():
                lower += 1
        if lower == 0:
            require_lower = False
    else:
        require_lower = True

    num = 0
    if require_digit:
        for i in password:
            if i.isnumeric():
                num += 1
        if num == 0:
            require_digit = False
    else:
        require_digit = True

    return min_length and require_upper and require_lower and require_digit
#==========================================

def format_date(data, format="dmy"):
    format_data = {}
    given_data_list = data.split("-")
    for (i, j) in zip(given_data_list, "ymd"):
        format_data[j] = i
    result = ""

    for i in format:
        if i in format_data.keys():
            result += format_data[i]
        else:
            return data
    return result
print(format_date("2023-07-01"))
#==========================================

def compare_lists(list1, list2, ignore_case=False):
    list = []
    casefolded_list2 = [x.casefold() for x in list2]
    for i in list1:
        if ignore_case == True:
            if i.casefold() in casefolded_list2:
                continue
            else:
                list.append(i)
        else:
            if i in list2:
                continue
            else:
                list.append(i)
    return list
    # element in list1 but not in list2
new_line(1)
def calculate_average(*args):
    average = [x for x in args]
    return sum(average) / len(average)
print(calculate_average(1.2, 0.9, 1.3, 1.1, 1.7))
new_line(2)
def check_data_format(**kwargs):
    for i,j in zip(kwargs.keys(), kwargs.values()):
        if type(i) is str and j.isnumeric():
            print(j.isnumeric())
            continue
        else:
            return False
    return True

def test_function(func, kwargs, expected_result):
    return func(**kwargs) == expected_result

print(test_function(check_data_format, {"a": -1, "b": -2.5, "c": 0}, True))
# print(check_data_format(uid=24191, age="30", height=156 ))