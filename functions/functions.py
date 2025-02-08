def greet(name):
   print(f"Привет, {name}!")
greet("piter")
def new_section(section_name):
    print()
    print(f"=============================== {section_name} =====================================")
def new_line(header=""):
    if header == "":
        print("-------------------------------------------------------------")
        print()
    else:
        print()
        print(f"----------------------- {header} -----------------------------------")
def short_line(section=''):
    print("\t  -------------------  {}".format(section))

print("- using only name without the call of function, so by this way we may call the function in another variable by using function call sign - () ")
print("another_print = print")
print("another_print('Выводим на экран при помощи переменной another_print!')")
another_print = print
another_print('Выводим на экран при помощи переменной another_print!')
# Выводим на экран при помощи переменной another_print!
# Теперь функция print и another_print выполняют одну и ту же операцию, просто называются по-разному
print("Эти примеры нужны для понимания главной вещи: само по себе имя функции — это просто ссылка, которой мы можем оперировать в привычном для нас ключе. "
      " А использование функции — это использование оператора круглых скобок.")
print()
print("Принцип DRY (Don’t Repeat Yourself — «Избегай самоповтора») — один из основных принципов разработки ПО, "
      "который наставляет нас избегать дублирования кода путём применения различных инструментов и навыков.")
print("""\t
        "Процедурное программирование. - Программа без функций, которая выполняется последовательно сверху вниз.
        "Функциональное программирование. - Программа, которая содержит функции, но всё ещё является процедурным кодом. Однако такой код более компактный, поскольку вся функциональность вынесена за скобки — в функции.
        "Объектно-ориентированное программирование. - Программа строится на основе классов и объектов. С этим типом программирования мы познакомим вас на заключительных этапах.
""")
new_line()
# count_elements() # Вызов до объявления - здесь и получим ошибку
def count_elements(): # Объявление функции
   print('Функция, которая будет считать количество элементов') # Тело функции
count_elements() # Вызов после объявления
# NameError: name 'count_elements' is not defined
new_line()
print("Определение того, что ожидает получить функция, называется параметром. А то, что мы передаём функции при её вызове, называется аргументом.")
print("""def count_elements(input_list): # <- параметр
   print('Считаю элементы в {}'.format(input_list))
list1 = [1, 2, 3, 2, 1]
count_elements(list1) # <- аргумент""")
#===========================================================return
new_section("return two elements")
def count_elements(input_list):
  dict1 = {}
  for i in input_list:
      if i in dict1:
          dict1[i] += 1
      else:
          dict1[i] = 1
  return dict1
  return dict1.keys()
list1 = [1, 2, 3, 2, 1, 1, 1, 2, 3, 3, 3, 3]
result = count_elements(list1)
print(result)
print("""def count_elements(input_list):
  dict1 = {}
  for i in input_list:
      if i in dict1:
          dict1[i] += 1
      else:
          dict1[i] = 1
  return dict1
  return dict1.keys()
list1 = [1, 2, 3, 2, 1, 1, 1, 2, 3, 3, 3, 3]
result = count_elements(list1)
print(result)""")
# {1: 4, 2: 3, 3: 5}
print("this will return the value from the first return operator")
new_line()
print()
def count_elements(input_list):
  dict1 = {}
  for i in input_list:
      if i in dict1:
          dict1[i] += 1
      else:
          dict1[i] = 1
  return dict1, dict1.keys() # Возвращаем два значения
list1 = [1, 2, 3, 2, 1, 1, 1, 2, 3, 3, 3, 3]
result = count_elements(list1)
print(result)
print("""def count_elements(input_list):
  dict1 = {}
  for i in input_list:
      if i in dict1:
          dict1[i] += 1
      else:
          dict1[i] = 1
  return dict1, dict1.keys() # Возвращаем два значения
list1 = [1, 2, 3, 2, 1, 1, 1, 2, 3, 3, 3, 3]
result = count_elements(list1)
print(result)""")
print("this will return a tuple with two values")
new_line()
print("При этом, если функция возвращает кортеж из нескольких объектов, то мы можем сразу же их распаковать в разные переменные следующим образом:")
print("""list1_count_dict, list1_unique_values  = count_elements(list1)
print(list1_count_dict)
print(list1_unique_values)""")
print("Если мы используем такую конструкцию, то должны знать, сколько переменных возвращает функция, иначе можно наткнуться на ошибку:")
new_line()
print("""def count_elements(input_list):
   if type(input_list) not in (list, tuple, str): # not in tuple
       return "Недопустимый тип переданного аргумента" """)
new_line()
new_section("Arguments and Parameters")
print("""def show_card(name, age, sex):
   print("Name: {}\nAge: {}\nSex: {}".format(name, age, sex))
   ---------
# changing the order of giving arguments by giving it like a key=value 
show_card(age=22, sex='Male', name='Lev') # Используем ключи
   ----------
# or give first positional argument then the rest as key=value
show_card('Lev', sex='Male', age=22)
   ----------
# this will cause an error; positional argument is given at the end
show_card(name='Lev', age=22, 'Male') # <- это аргументы
# SyntaxError: positional argument follows keyword argument""")
new_line("default argument")
print("""def power(base, exponent=2):  # "exponent" - параметр со значением по умолчанию
   return base ** exponent
print(power(10))  # "10" - позиционный аргумент, "exponent" будет равен 2""")

print("Стоит взять себе за правило, что в качестве значений по умолчанию у параметров нужно указывать только неизменяемые типы данных. ")
print("""def create_start_list(start_value, lst=None):
   if lst is None:
       lst=[]
   lst.append(start_value)
   return lst

l1 = create_start_list(1)
print(l1)
# [1]
l2 = create_start_list(2)
print(l2)
# [2]""")

new_section("*args & **kwargs")
new_line("*args")
print("""\tNew way of calling same function multiple time \n\ttest_calculate_discount((100, 10, 90), (200, 20, 160), (300, 50, 150), (405, 0, 400))""")
print("""def my_func(*args):
   print(args)
my_func(1, 2, 3, 4)""")
print("> Всё дело в операторе *, который нужно ставить перед именем параметра — это оператор упаковки позиционных аргументов, переданных функций.")
print("""> Вместо имени args можно использовать любое другое имя в качестве параметра, 
который будет принимать произвольное количество аргументов, а *args работает только на уровне соглашений между программистами:""")
print("""def func(*params):
   for param in params:
       print(param)
func(1, 2, 3)""")
new_line()
print("""def my_func(a, *args):
   print(a)
   print(args)
my_func(1, 15, 25, 35)""")
print("""def my_func(a, *args, default_param=0):
   print(a)
   print(args)
   print(default_param)
my_func(1, 15, 25, 35)""")
print(">> Таким образом выглядит порядок объявления параметров функции (a, *args, default_param=0): "
      "\n>> позиционные аргументы, *args и затем параметры со значением по умолчанию.")
def calculate_discount(price, discount):
   return price - (price * discount / 100)
print("""...
def test_calculate_discount(*test_data):
   for data in test_data:  <<<
   >>> price, discount, expected_result = data | >data< here is a tuple with data that will be assigned to each variable from left side of = sign (100, 10, 90)
       result = calculate_discount(price, discount)
       ...""")
def test_calculate_discount(*test_data):
   for data in test_data:
       price, discount, expected_result = data # is a tuple with data that will be assigned to each variable from left side of = sign (100, 10, 90)
       result = calculate_discount(price, discount)
       if abs(result - expected_result) < 0.01:  # использование abs для учёта погрешности вычислений с плавающей точкой
           print(f"Test passed for price={price}, discount={discount}")
       else:
           print(f"Test failed for price={price}, discount={discount}, expected {expected_result}, got {result}")
#	И использовать её мы можем следующим образом:
test_calculate_discount((100, 10, 90), (200, 20, 160), (300, 50, 150), (405, 0, 400))
new_line("**kwargs")
print("> Для принятия произвольного количества именованных аргументов используется оператор **, а в качестве имени параметра, в который осуществляется упаковка, выбирают kwargs.")
print("""def my_func(**kwargs):
   print(type(kwargs))
   print(kwargs)
my_func(body={"name": "John"}, headers={"Content-Type": "application/json"})
""")
def my_func(**kwargs):
   print(type(kwargs))
   print(kwargs)
my_func(body={"name": "John"}, headers={"Content-Type": "application/json"})
print("""def send_request(url, method, **kwargs):
   print(f"Отправка {method}-запроса на {url} с параметрами {kwargs}")
send_request('https://my-api.com/resources', 'POST', body={"name": "John"}, headers={"Content-Type": "application/json"})""")
def send_request(url, method, **kwargs):
   print(f"Отправка {method}-запроса на {url} с параметрами {kwargs}")
print("\t---------------------------")
send_request('https://my-api.com/resources', 'POST', body={"name": "John"}, headers={"Content-Type": "application/json"})
print(""">> B каком порядке нужно их перечислять при объявлении:

    1. Сначала идут обязательные позиционные параметры.
    2. Затем указываем параметры со значением по умолчанию.
    3. Затем идёт *args, который упакует все последующие переданные позиционные аргументы.
    4. После *args мы можем указать параметры, которые могут быть переданы только по имени.
    5. В конце указываем **kwargs для упаковки последующих именованных аргументов.

На примере ниже наглядно показана данная последовательность:  
def func(a, b, c=0, d=1, *args, e, f, **kwargs):

\tВ данном примере a и b — обязательные позиционные параметры, c и d — параметры со значениями по умолчанию, 
\t*args собирает все оставшиеся позиционные аргументы, e и f — параметры, которые можно передать только по имени, 
\tи **kwargs собирает все оставшиеся именованные аргументы.

> Обратите внимание на то, что e и f в данном примере должны передаваться именно как именованные аргументы, а не позиционные, даже если они указаны после *args.

И, соответственно, передавать аргументы такой функции мы будем следующим образом:

func(1, 2, 3, 4, 5, 6, e=7, f=8, g=9, h=10)

- a и b — это обязательные позиционные аргументы. Они получают значения 1 и 2.
- c и d — это необязательные позиционные аргументы, они имеют значения по умолчанию и получают значения 3 и 4. 
    Если бы мы не указали их при вызове функции, они получили бы значения по умолчанию — 0 и 1 соответственно.
- *args собирает все дополнительные позиционные аргументы в кортеж. В данном случае args будет равен (5, 6).
- e и f — это обязательные ключевые аргументы. Они могут быть переданы только по ключу. В данном случае они получают значения 7 и 8.
- **kwargs собирает все дополнительные ключевые аргументы в словарь. В данном случае kwargs будет равен {'g': 9, 'h': 10}.

> Таким образом вы можете передавать в функцию разные типы аргументов, и каждый из них будет обработан соответствующим образом.""")
new_line("operator /")
print("Оператор / в определении функции указывает, что все параметры перед ним должны быть переданы исключительно позиционно. "
      "\nЭто означает, что эти параметры не могут быть переданы по имени как ключевые аргументы.")
print("""def func(a, b, /, c, d, *, e, f):
   print(a, b, c, d, e, f)
   
    a и b могут быть переданы только позиционно;
    c и d могут быть переданы и позиционно, и по ключу;
    e и f могут быть переданы только по ключу.
    
    func(1, 2, 3, d=4, e=5, f=6)""")
new_line()
print("""list1, *list2 = [1, 2, 3, 4, 5]
print(list1)
# 1
print(list2)
# [2, 3, 4, 5]

*list1, list2 = [1, 2, 3, 4, 5]
print(list1)
# [1, 2, 3, 4]
print(list2)
# 5

> Такую операцию можно применять к любому итерируемому объекту — строке, списку или кортежу:

# Кортеж
*case1, case2 = (1, 2, 3, 4, 5)
print(case1)
# [1, 2, 3, 4]
print(case2)
# 5
\t -----------------
# Строка
case1, *case2 = "str"
print(case1)
# s
print(case2)
# ['t', 'r']
""")
str, *str = " string"
print(str)
short_line()
print("""list1 = [1, 2, 3]
tuple1 = (4, 5, 6)
list2 = [True, False]
tuple2 = ('O', 'OX')
result = [*list1, *tuple1, *list2, *tuple2]
""")
list1 = [1, 2, 3]
tuple1 = (4, 5, 6)
list2 = [True, False]
tuple2 = ('O', 'OX')
result = [*list1, *tuple1, *list2, *tuple2]
print(result)
short_line()
print("> А при помощи оператора ** мы можем упаковывать и распаковывать словари, например, следующим образом мы можем объединить два словаря в один:")
print("""dict1 = {'1':891239912, '2':19245912, '3': 12300123}
dict2 = {'4':81249912, '5':678912, '6': 123003453}
print({**dict1, **dict2})
> concatenated""")
dict1 = {'1':891239912, '2':19245912, '3': 12300123}
dict2 = {'4':81249912, '5':678912, '6': 123003453}
print({**dict1, **dict2})























