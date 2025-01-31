from functions import new_section, new_line, short_line
new_section("Generator & operator yield")
"generator example"
x = [n**2 for n in range(1, 5)]
print(x)
print("(<операция> for <переменная> in <итерируемый объект>)")
x = (n**2 for n in range(1, 5))
print(x)
new_line("function next()")
print("next(iterator, default)")

print("""
    iterator — это итератор, из которого нужно получить следующий элемент;
    default — это значение, которое функция next() вернёт, если в итераторе больше нет элементов. 
        Если значение default не указано и в итераторе больше нет элементов, функция next() вызовет исключение StopIteration.
""")
print("""Так вот, при помощи функции next() мы также последовательно можем получать значения и из генератора, поскольку он также является и итератором:""")

# print(next(x))
# # 1
# print(next(x))
# # 4
# print(next(x))
# # 9
# print(next(x))
# 16
print("Но как только мы выйдем за пределы, если не определяли параметр default в next, то получим StopIteration:")
# print(next(x))      # StopIteration
print(next(x, None))         # А вот как можно избежать этой ошибки:
print("""При этом пройтись по значениям генератора можно лишь единожды, повторного доступа к этим элементам из генератора у нас нет""")


for n in x:
   print(n)

print("""
Выражения-генераторы в отличие от списков, да и тех же генераторов списков, не хранятся в памяти целом, а записывают их в память по мере необходимости — генерации новых значений. 
Следовательно, у нас появляется возможность работы с очень большими объемами данных, экономя при этом память.""")
new_line("MemoryError")
print("very_big_data = list(range(1000000000000))")
# MemoryError
print("---------А выражение-генератор позволяет этой ошибки избежать:")
very_big_data = (n for n in range(1000000000000))
for n in very_big_data:
   print(n, end=' ')
   if n == 10:
       break
print()
short_line()
print("> put generated elements in the list")
very_big_data = (n for n in range(10000))
very_big_data = list(very_big_data)
print(type(very_big_data), len(very_big_data))
# <class 'list'> 10000
print("generated as a list")
very_big_data = [(n for n in range(10000))]
print(type(very_big_data), len(very_big_data))
# <class 'list'> 1

new_line("Функции генераторы")
print("""
Оператор yield в отличие от оператора return не заканчивает выполнение функции, 
а лишь останавливает-замораживает её до следующего вызова функции, 
замораживая функцию целиком — вместе с состоянием локальных переменных. """)
print()
def generate_test_data(n):
   for i in range(n):
       yield f"test_data_{i}"
test_data = generate_test_data(10)
print(test_data, type(test_data))
# <generator object generate_test_data at 0x000002299B216E40> <class 'generator'>
print(next(test_data))
# test_data_0
print(next(test_data))
# test_data_1
# OR on loop
for test in generate_test_data(10):
   print(test)
# for test in generate_test_data(10):
#    print(test)

new_line()
print("generating combinations")
def generate_combinations(colors, sizes):
   for color in colors:
       for size in sizes:
           yield color, size


combination_generator = generate_combinations(["red", "blue"], ["small", "large"])
for combination in combination_generator:
   print(combination)
print("При желании можно было было бы описать это и выражением-генератором:")
combination_generator = ((color, size) for size in ["small", "large"] for color in ["red", "blue"])
print("""Но во-первых такой код перестанет быть читаемым при добавлении даже одного дополнительного параметра, 
а в реальном мире их могут быть сотни, а во-вторых — по такому генератору мы сможем пройтись лишь единожды, 
а при помощи функции создавать их столько, сколько нам нужно.""")

print("""
--- Генераторы позволяют обрабатывать данные по мере необходимости, не загружая их полностью в память. 
    Это особенно ценно при работе с очень большими данными или потоками данных.
    
--- С помощью оператора yield мы можем заморозить выполнение функции и вернуться к нему позже, сохраняя состояние функции.
    
--- Генераторы обеспечивают более эффективное использование памяти, поскольку генерируют значения по одному, а не хранят все значения в памяти.
    
--- Генераторы могут быть использованы в любом месте, где ожидается итерируемый объект — как мы, например, помещали его в цикл for.
    
--- В контексте QA-инжиниринга и тестирования программного обеспечения генераторы могут быть использованы для создания тестовых данных, 
    параметризации тестов, работы с большими лог-файлами и многих других сценариев.
""")


new_line("CW1")
def generate_urls(url, start_point, end_point):
    return [url + str(i) for i in range(start_point, end_point)]

print(list(generate_urls("https://example.com/page_", 1, 6)))

new_line("CW2")

def generate_user_data(length, name_list, surname_list, age_list):
    count = 0
    for name in name_list:
        for surname in surname_list:
            for age in age_list:
                if count >= length:
                    return  # Завершаем генерацию
                yield name, surname, age
                count += 1

first_names = ["Alice", "Bob", "Charlie"]
last_names = ["Smith", "Johnson", "Williams"]
user_data_generator = generate_user_data(5, first_names, last_names, [18, 60])
for user in user_data_generator:
   print(user)
short_line()                         # use randome.choice()
import random
def generate_user_data1(count, first_names, last_names, age_diapason):
   for _ in range(count):
       name = random.choice(first_names)
       surname = random.choice(last_names)
       age = random.randint(age_diapason[0], age_diapason[1])
       yield name, surname, age
user_data_generator = generate_user_data1(5, first_names, last_names, [18, 60])
for user in user_data_generator:
   print(user)
short_line()