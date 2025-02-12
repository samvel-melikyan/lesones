from functions.functions import *

new_section("OOP")
print("""
Процесс написания кода существенно улучшили три основные парадигмы ООП:

• Инкапсуляция. Упростила поддержку и модификацию кода, так как изменять внутреннее состояние объекта можно без вмешательства в остальную часть кода;
• Наследование. Уменьшило дублирование кода и упростило его повторное использование;
• Полиморфизм. Повысил гибкость и упростил написание программ, способных работать с огромным количеством разнообразных объектов.

С этими концепциями мы и познакомимся в предстоящем цикле модулей, посвященным ООП, и рассмотрим практические примеры, отражающие их. """)
short_line("class")
print("Класс — это шаблон, в котором описываются атрибуты (свойства) и методы (функции) будущего объекта.")
short_line("object")
print("Объект — это экземпляр класса, сущность, созданная в соответствии с выбранным шаблоном.")

line("declaration")

print("""class <название_класса>:
    <тело_класса>   """)

class User:
   login = 'user_login'
   role = 'Python Developer'

print(User.login)
print(User.role)
User.role = 'Data Scientist'
print(User.role)

print("""
Еще можно воспользоваться коллекцией __dict__ для того, чтобы увидеть все атрибуты класса сразу, выглядит это следующим образом:
class User:
   login = 'user_login'
   role = 'Python Developer'
print(User.__dict__)""")
class User:
   login = 'user_login'
   role = 'Python Developer'

print(User.__dict__)

line("creating an objects")
class User:
   login = 'user_login'
   role = 'Python Developer'
u1 = User()
u2 = User()
print("obj fields")
print(u1.login, u1.role)
print(u2.login, u2.role)


print("""Но это не идентичные объекты, и вы можете сами убедиться в этом, проверив значения ячеек в памяти этих атрибутов при помощи функции id():

print(id(u1), id(u2))  
""")
print(id(u1), id(u2))
# 2192065736512 2192065736464

print(u1.__dict__)
print(u1.login, u1.role)

line("Adding a field to a class")
User.email = 'user@gmail.com'

print(User.__dict__)
short_line("function setattr()")
print("""Аналогично создавать или изменять атрибуты можно при помощи встроенной функции settatr(). Она принимает:

    пространство имен (имя класса или экземпляра класса);
    имя атрибута (в виде строки);
    его значение.

class User:
   login = 'user_login'
   role = 'Python Developer'

u1 = User()
# Установка (либо изменение) нового атрибута класса
setattr(User, 'email', 'user@gmail.com')

# Установка (либо изменение) локального атрибута экземпляру класса
setattr(u1, 'login', 'DEIvanov')""")

short_line("function getattr()")
print("""
принимающая в себя:

    имя класса или экземпляра класса;
    имя искомого атрибута;
    опциональный (необязательный) третий аргумент — возвращаемое значение, в случае, если атрибута не существует.

Посмотрим пример использования:

print(getattr(User, 'email', False))
""")
print("""Дело в том, что может возникнуть ситуация, когда мы будем получать имена атрибутов извне, не зная даже имени этого атрибута, 
так как оно может храниться в переменной. Тут на помощь придет функция getattr(), в которую мы передадим переменную, 
хранящую имя этого атрибута, и получим его значение.""")

some_hidden_attr_name = 'email'
print(getattr(User, some_hidden_attr_name, False))


line("deleting attribute")
print("С добавлением атрибутов разобрались. Теперь поговорим об их удалении. Удалять атрибуты можно при помощи ключевого слова del.")
print("""
Важно! После удаления атрибута проверяется его наличие функцией hasattr(), которая принимает в 
себя имя класса или объекта и его атрибута. Ею также можно воспользоваться перед тем, как вы собираетесь 
удалить атрибут, в существовании которого не уверены.""")


User.email = 'email_template@gmail.com'
print(hasattr(User, 'email'))

del User.email
print(hasattr(User, 'email'))

print("""
del User.email
print(hasattr(User, 'email'))

Таким образом, мы вначале добавили атрибут email, 
проверили его наличие функцией hasattr(), удалили его при помощи ключевого слова  del и 
убедились в успешном удалении атрибута опять же функцией hasattr().""")

short_line("delattr()")

print("""Также удалить атрибут можно при помощи встроенной функции delattr(), которой мы передаем имя экземпляра класса или класса и имя атрибута:""")
User.email = 'email_template@gmail.com'
print(hasattr(User, 'email'))
# True
delattr(User, 'email')
print(hasattr(User, 'email'))
# False

print("""Различие между hasattr() и getattr() с опциональным третьим параметром в том, что hasattr() 
возвращает либо True, либо False, а getattr() либо значение атрибута, если он существует, 
либо значение третьего параметра, переданного ей, если не существует. """)

print("""Но вот механизм удаления атрибутов при помощи del или delattr() позволит вам 
удалить только атрибуты, содержащиеся в __dict__  самого экземпляра, но не атрибуты класса, на которые этот экземпляр может ссылаться.""")

line("class as a data type")

u1 = User()
print(type(u1))
print(type(u1) == User, "type(u1) == User")
print(isinstance(u1, User), "isinstance(u1, User)")

short_line("isinstance()")
print("""Функция isinstance(object, classinfo) вернет True , если проверяемый объект object является экземпляром указанного класса 
(классов) или его подкласса (прямого, косвенного или виртуального). Если объект object не является экземпляром данного типа, то функция всегда возвращает False.""")
print("""
Для того, чтобы вывести полный список атрибутов и методов, доступных для встроенного в Python класса можно воспользоваться встроенной функцией dir():
simple_str = 'hello'
print(type(simple_str))
print(dir(simple_str))""")
simple_str = 'hello'
print(type(simple_str))
print(dir(simple_str))

def func():
    pass

print(type(func))
print(dir(func))
short_line()


class Student:
   course = "Data Science"


s1 = Student()
print(s1.course)

name = "Иван"
surname = "Иванов"
semester = 1
result = s1.__dict__
print()
print(Student.__dict__)


line("self")
print("""class User:
   login = 'user_login'
   role = 'Python Developer'
   
   # объявление метода
   def demo_method_print():
      print('Method call')

u1 = User()
# вызов метода
u1.demo_method_print()
# TypeError: User.demo_method_print() takes 0 positional arguments but 1 was given

Ошибка говорит нам о том, что метод demo_method_print не принимает ни одного позиционного аргумента, 
но один ему все-таки был передан, хотя коде мы ничего не делали.

Если у вас появился вопрос о назначении этого функционала, то вспомните, что каждый экземпляр класса 
образует собственное пространство имен, т.е у каждого экземпляра могут быть свои атрибуты и совершенно разные значения этих атрибутов, 
а такой механизм очень просто позволит обращаться к атрибутам именного того экземпляра, из которого он был вызван.

Получается, что для корректной работы нашей программы нам необходимо добавить аргумент методу u1, 
чтобы он смог принять ссылку на объект, из которого будет вызван. """)

print("Для этого аргумента существует общепринятое название — self, что в переводе можно воспринимать как «сам объект».")
print("""   
   login = 'user_login'
   role = 'Python Developer'

   def demo_method_print(self):
       print(f'Method call by {self}')

u1 = User()
print(u1)

u1.demo_method_print()

-----------
Теперь снова попробуем вызвать этот метод, но уже через класс, как мы делали это в самом начале:

User.demo_method_print()

# TypeError: User.demo_method_print() missing 1 required positional argument: 'self'

И как вы уже могли догадаться, в случае с вызовом методов через сам класс никакой подстановки не происходит, и нам необходимо передавать вручную объект в метод:

u1 = User()
User.demo_method_print(u1)

# Method call by <__main__.User object at 0x7f766c45a3e0>

""")
class User:
   login = 'user_login'
   role = 'Python Developer'

   def demo_method_print(self):
       print(f'Method call by {self}')

   def show_attrs(self):
       print(f'Login: {self.login}, role: {self.role}')

u1 = User()
u1.show_attrs()


class User:
    private_key = ""

    def set_private_key(self, string: str):
        self.private_key = string

    def show_private_key(self):
        print(f"Приватный ключ пользователя {self.private_key}")
user1 = User()
user1.set_private_key('uox00b_12x')
user1.show_private_key()