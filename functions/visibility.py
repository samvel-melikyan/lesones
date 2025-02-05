# global keyword
# nonlocal keyword
from random import random

from lesones.functions.functions import new_section, new_line

new_section("global")
x = 20
def change_global_var():
	global x
	x = 30
print(x, "before function call")  # Вывод: 20
change_global_var()
print(x, "after function call")  # Вывод: 30
print("""
При этом менять область видимости переменной нужно в самом начале тела функции, 
потому что если вы создадите переменную с именем x (то есть переменную x в локальной области видимости функции change_global_var), 
и только потом скажете, что меняете ее область видимости, это приведет к ошибке SyntaxError:""")
print("""-------------------------------------------
x = 20
def change_global_var():
	x = 15
	global x
	x = 30
change_global_var()

#	global x
#	^^^^^^^^
# SyntaxError: name 'x' is assigned to before global declaration""")
print("""-------------------------------------------
def change_global_var():
	global x
	x = 30
change_global_var()
print(x)
# 30""")


new_section("nonlocal")
print("""То есть внутри локальной области видимости inner_function можно работать 
с переменной x, которая находится в локальной области видимости outer_function.
""")
x = 0
print('Global x: {}'.format(x))
def outer_function():
	x = 1
	def inner_function():
            nonlocal x
            x = 2
            print('Inner x: {}'.format(x))
	inner_function()
	print('Outer x: {}'.format(x))
outer_function()
# Global x: 0
# Inner x: 2
# Outer x: 2

print("nonlocal keyword sees a variable as from outer function's view."
      "But you can't use it to access to the variable from global scope. "
      "To access to a global variable you need to use the keyword global")

new_line()
tests_run = 0
tests_failed = 0

def run_test(test):
    global tests_run
    global tests_failed
    if test():
        tests_run += 1
    else:
        tests_failed += 1



















