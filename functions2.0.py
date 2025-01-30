from functions import new_section, new_line, short_line

new_section("Recursion")
def recursive_func(n=0):
    print(n)
    recursive_func(n + 1)

# recursive_func(3)

print("\n> Каждый раз, когда вы создаете рекурсию, вы на самом деле, организуете стек вызова функций, который состоит из прямого и обратного прохода.")
print("\n> Стек — это абстрактный тип данных (структура), список элементов, организованных по принципу LIFO.(last in, first out)")
print("\n> Первоначальный вызов функции — мы кладем одну нашу функцию в стек, затем она вызывает сама себя, мы кладём её в стек выше изначальной и так далее. ")

print("""
    recursive_function(0)_____________
    recursive_function(1)            |
                                     |
   |D                       recursive_function(1)_____________
   |E                       recursive_function(2)            |
   |P                                                        |
   |T                                               recursive_function(2)_____________
   |H                                               recursive_function(3)            |
  \|/                                                                                |
   '                                                                        recursive_function(3)
                                                                            recursive_function(4)            

""")
new_line("Заполнение и освобождение стека функций")
def recursive_func(n=0):
   print('Вывод до запуска рекурсии: ', n)
   if n < 3:
       recursive_func(n + 1)
   print('Вывод после запуска рекурсии: ', n)
recursive_func()

print("Последний уровень рекурсии заканчивает свою работу. — что дальше? Дальше мы освобождаем стек, "
      "завершаем выполнение всех прошлых функций. Они запустили рекурсию, "
      "и пока эта функция не будет выполнена (вызванная самой функций), они находятся в режиме ожидания.")



print("""
                           ______________               _____________          ______________________
                           |            |               |           |          |                    |    
        steck                           steck                       steck                           steck
        ---------------------           ---------------------       ---------------------           ---------------------
        recursive_functino(0)           recursive_functino(0)       recursive_functino(0)           recursive_functino(0)
                                        recursive_functino(1)       recursive_functino(1)           recursive_functino(1)
                                                                    recursive_functino(2)           recursive_functino(2)
                                                                                                    recursive_functino(3)
       
                           ______________               _____________          ______________________
                           |            |               |           |          |                    |    
        steck                           steck                       steck                           steck
        ---------------------           ---------------------       ---------------------           ---------------------
        recursive_functino(3)           recursive_functino(2)       recursive_functino(0)           recursive_functino(0)
        recursive_functino(2)           recursive_functino(1)       recursive_functino(1)           
        recursive_functino(1)           recursive_functino(0)
        recursive_functino(0)
""")

new_line("Factorial")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

print("""
Дерево — иерархическая структура данных, которая имеет корневой элемент и набор поддеревьев, также представляющих собой деревья.

Элементы дерева называются узлами. Каждый узел может иметь ноль или больше дочерних узлов — потомков (детей). Узел без детей называется листом.
Простейшее дерево содержит только один узел, называемый корнем.""")

class Node:
   def __init__(self, value, children=None):
       self.value = value
       self.children = children if children else []

root = Node(5, [
   Node(3, [
       Node(1),
       Node(4)
   ]),
   Node(2, [
       Node(6),
       Node(-1)
   ])
])

# Получение значения в узле-корне
print(root.value)
# 5

# Получение значений дочерних узлов
print(root.children[0].value, root.children[1].value)
# 3 2

# Получение значений листьев
print(root.children[0].children[0].value, root.children[0].children[1].value)
print(root.children[1].children[0].value, root.children[1].children[1].value)
# 1 4
# 6 -1
def test_tree_structure(node):
    # у node есть  value — значение
    # и children — список других node
    # Базовый случай
    if node.value < 0:
        return False
    # Рекурсия
    for child in node.children:
        if not test_tree_structure(child):
            return False
    return True

print(test_tree_structure(root))

print("""* Тестирование иерархических структур. Многие системы включают в себя иерархические структуры данных, например деревья. 
Рекуррентные функции могут быть использованы для обхода этих структур и проверки определенных условий или свойств на каждом уровне.

* Тестирование глубоко вложенных сценариев. В некоторых случаях необходимо проверить глубоко вложенные условия или логику, где поведение системы зависит от множества вложенных условий. 
Рекуррентные функции могут значительно упростить этот процесс, предоставляя понятный и эффективный способ тестирования.

*Автоматическое восстановление после сбоев. Рекуррентные функции могут быть использованы для автоматического восстановления тестовых 
сценариев после сбоев путем рекурсивного повторения теста с измененными параметрами или условиями, пока тест не будет успешно пройден 
или не будет достигнут определенный предел попыток.  Это особенно полезно в тестировании систем, где возможны временные сбои или ошибки, 
зависящие от внешних факторов. Например, если система не отвечает из-за временной потери сети, рекурсивная функция может повторять попытку 
подключения через определенные промежутки времени, пока соединение не будет восстановлено. Такой подход помогает обеспечить стабильность и 
надежность тестируемой системы.""")


new_line("CW 1")

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1 :
        return 1
    else:
        return fibonacci(n - 1) +  fibonacci(n - 2)



def fibonacci_backward(n):
    for i in range(1000000):
        if fibonacci(i) == n:
            return i


# def fibonacci_backward2(n):
#     fibo = 0
#     if n == 0 or n == 1:
#         return fibo
#     else:
#         fibo += 1
#         return fibonacci_backward2(n) - fibonacci_backward2(n - 1)


number = fibonacci(15)
print(f"Fibonacci of {fibonacci_backward(number)} is ", number)

new_line("CW 2")

def binary_search(list, number):
    if len(list) == 0:
        return False
    sorted(list)
    mid = len(list) / 2

    if mid == number:
        return True
    elif mid < mid:
        binary_search(list[:mid], number)
    elif mid > mid:
        binary_search(list[mid:], number)
# def binary_search(lst, target):
#    if len(lst) == 0:
#        return False
#    else:
#        midpoint = len(lst) // 2
#        if lst[midpoint] == target:
#            return True
#        else:
#            if lst[midpoint] < target:
#                return binary_search(lst[midpoint+1:], target)
#            else:
#                return binary_search(lst[:midpoint], target)


print(binary_search([1, 2, 3, 4, 5], 4))

new_line("CW 3")

# def is_palindrome(s):
#     str = s.reverse()
#     if s == str:
#         return True

def is_palindrome(s):
   if len(s) < 2:
       return True
   if s[0] != s[-1]:
       return False
   return is_palindrome(s[1:-1])
print(is_palindrome("olo"))
























