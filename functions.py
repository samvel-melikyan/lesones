def greet(name):
   print(f"Привет, {name}!")
greet("piter")
def new_section(section_name):
    print()
    print(f"==============================={section_name}=====================================")
def new_line():
    print("-------------------------------------------------------------")
    print()
print()
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










































