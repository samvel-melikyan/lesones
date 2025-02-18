print("=============================SETs===================")
print("Set is: \n1. unordered\n2. doesn't allow repetition")
print()
# создаем множество из списка с помощью set()
numbers = set([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 9])
print(numbers)
# создаем множество с помощью {}
numbers = {1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9}
print(numbers)
print("   Обратите внимание, что при создании множеств в примере выше были повторяющиеся элементы, "
      "\nно в итоге они отсутствуют — потому что в множестве элементы не повторяются. "
      "\nПоэтому множества часто используются для удаления повторяющихся элементов из списка. ")
print(type({}))
print(type(set()))
print()
print("Так как во множестве элементы не упорядочены, у них нет своего номера, а значит, и индексы с множествами работать не будут. Попробуйте вызвать элемент множества по индексу:")
numbers = {1, 1, 2, 2, 3, 4, 5}
print("----------------for loop--------------")
# перебор элементов множества
for elem in numbers:
    print(elem)
numbers = {1, 1, 2, 2, 3, 4, 5}
print("-----------------in operator-----------")
num = 115                                       #int(input('Введите число: '))
if num in numbers:
    print('Это число есть во множестве.')
else:
    print('Этого числа нет во множестве.')

print("============================add an element")
numbers = {1, 1, 2, 2, 3, 4, 5}
# добавим элемент в множество
numbers.add(6) ###
print(numbers)
print("============================remove element")
numbers.remove(1)  ###
print(numbers)
print("============================clear set")
numbers.clear()  ###
print(numbers)

print("=====================HW---------------------")

family = tuple(["ggggggggg", "ddddddddd", "ssssssssss", "vvvvvv", "ooooooooo"])
print(family[0])
print(family[-1])
print(family[::2])
print(len(family))

new_num_set = set()
for i in range(0,10):
    new_num_set.add(i)
print("length before if statmant", len(new_num_set))
num = int(input("          type a number _"))
if num in new_num_set:
    print("number is in the set, so I'll delete it ')")
    new_num_set.remove(num)
else:
    new_num_set.add(num)
    print("number is added")
print("length after if statmant", len(new_num_set))
















