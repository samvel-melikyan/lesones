numbers1 = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9])
numbers2 = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9])
numbers3 = (1,)            # Обратите внимание, если создаете кортеж, состоящий из одного элемента, после элемента нужно написать запятую: numbers = (1,).

numbers_tuple = (1, 2, 3, 4, 5, 6)
numbers_list = [1, 2, 3, 4, 5, 6]

# определим размер с помощью .__sizeof__() ---------------------
print(f'''Размер кортежа: {numbers_tuple.__sizeof__()}
Размер списка: {numbers_list.__sizeof__()}''')

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# выведем нулевой элемент кортежа
print(numbers[0])
# выведем третий элемент кортежа
print(numbers[3])
# выведем последний элемент кортежа
print(numbers[-1])

# numbers[0] = 0 # will trow an error because tuple is immutable
print()
print("Также по кортежу можно сделать срез, принцип работы такой же, как и со списками:")
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# срез всего кортежа
# start=0 stop=10 step=1
print(numbers[:])
# срез c нулевого по пятый элемент кортежа
# start=0 stop=5 step=1
print(numbers[:5])
# срез c первого по последний элемент кортежа
# start=1 stop=10 step=1
print(numbers[1:])
# срез с третьего по шестой элемент кортежа
# start=3 stop=6 step=1
print(numbers[3:6])
# каждый второй элемент кортежа (четные индексы)
# start=1 stop=10 step=2
print(numbers[1::2])
print("-----------------looping is also the same as in with the arrays" )
for elem in numbers:
    print(elem)
print("----------------checking availability also the same")
# if num in numbers:
#         print('Это число есть в кортеже.')
#     else:
#         print('Этого числа нет в кортеже.')

user = ('Michael', 'Scott', 40)

print("разложим кортеж на отдельные переменные")
name, surname, age = user
print(user)
print(name)
print(surname)
print(age)










































































































