from lesones.functions.functions import *
new_section("@property")
print("""В Python для реализации инкапсуляции данных используется декоратор @property. 
Он позволяет определить методы-геттеры и методы-сеттеры для доступа к атрибутам объектов и 
контролировать чтение и запись значений этих атрибутов через привычные нам интерфейсы, поскольку 
до этого момента наши с вами геттеры и сеттеры были весьма «условны».""")


class User:
    PASSWORD_MIN_LEN = 5
    PASSWORD_MAX_LEN = 16

    def __init__(self, login, password, name, email, role):
        self.__validate_password(password)
        self.__login = login
        self.__password = password
        self.name = name
        self.email = email
        self.role = role

    def get_login_password(self):
        return self.__login, self.__password

    @classmethod
    def __validate_password(cls, password):
        if not (cls.PASSWORD_MIN_LEN <= len(password) <= cls.PASSWORD_MAX_LEN and type(password) == type(" ")):
            raise AttributeError('Password not valid')

    def set_login_password(self, login: str, password: str):
        self.__validate_password(password)
        self.__login = login
        self.__password = password

# ---------------------------------------------------------------------
u1 = User("JohnD", "majesk123", "John Doe", "john.doe@example.com", 'TechLead')
u1.set_login_password('JohnDale', 'Kolqs12')
print(u1.get_login_password())


line()
print("""В Python property— это специальный встроенный тип данных, 
который позволяет классу управлять доступом к его свойствам с помощью методов.""")
print("""
propertyпредоставляет методы для установки (setter) и получения (getter) значения
свойства класса (а также удаления (deleter), но данный метод мы опустим, так как это выходит за рамки курса).""")
short_line("syntax")
print("<имя_атрибута> = property(<имя_геттера>, <имя_сеттера>)")
class User:
    PASSWORD_MIN_LEN = 5
    PASSWORD_MAX_LEN = 16

    def __init__(self, login, password, name, email, role):
        self.__validate_password(password)
        self.__login = login
        self.__password = password
        self.name = name
        self.email = email
        self.role = role

    @classmethod
    def __validate_password(cls, password):
        if not (cls.PASSWORD_MIN_LEN <= len(password) <= cls.PASSWORD_MAX_LEN and type(password) == type(" ")):
            raise AttributeError('Password not valid')

    def get_login(self):
        return self.__login

    def set_login(self, new_login):
        self.__login = new_login

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__validate_password(new_password)
        self.__password = new_password
    # -----------------------------------------------------------
    login = property(get_login, set_login)
    password = property(get_password, set_password)
    # -----------------------------------------------------------
print("""
Объявленное свойство password в классе ссылается на объект property, 
которому, в свою очередь, переданы ссылки на геттер и сеттер — get_passwordи 
set_password(именно в этом порядке) для работы с этим свойством. При этом заметьте, 
что переданы именно ссылки, без круглых скобок.""")

print("""При этом, как вы могли заметить, методы доступа, определенные с использованием property , 
пишутся после методов, потому что они зависят от существования уже определенных методов. 
Если бы они были определены перед методами, то в момент определения свойств не было бы 
возможности использовать методыget_login(), set_login(), get_password() и set_password(), 
так как они ещё не были определены.""")
short_line()
u1 = User("JohnD", "majesk123", "John Doe", "john.doe@example.com", 'TechLead')

# В момент переопределения значения вызывается метод set_password
u1.password = 'Krop88'
# В момент получения доступа к значению вызывается метод get_password
print(u1.password)
# Krop88

# u1.password = '123'
# AttributeError: Password not valid
short_line()
u1 = User("JohnD", "majesk123", "John Doe", "john.doe@example.com", 'TechLead')
print(u1.__dict__)
u1.password = 'Krop88'
print(u1.password)

line("Декоратор @property")

print(
    """
    Декоратор @property в Python — это встроенная функция, 
    которая превращает метод в свойство класса, с которым можно работать, 
    как с обычным атрибутом, то есть устанавливать ему значение и обращаться к его значению"""
)
print("""
По сути декоратор @property — это более общая и более удобная версия 
реализации объекта property, рассмотренного выше.""")

class DemoClass:
   def __init__(self):
       self.__some_private_property = None

   @property
   def some_private_property(self):
       """Геттер для свойства __some_private_property."""
       return self.__some_private_property

   @some_private_property.setter
   def some_private_property(self, value):
       """Сеттер для свойства __some_private_property."""
       self.__some_private_property  = value
print("""Декоратор @property превращает метод some_private_property в свойство, 
которое можно получать, но не изменять напрямую. Возвращаемое значение метода 
будет использоваться как значение свойства.

А декоратор @some_private_property.setter превращает метод some_private_property в 
сеттер свойства, который позволяет устанавливать его значение.""")
short_line()
print("""Таким образом для геттера мы прописываем в качестве декоратора @property, а для сеттера @имя_метода_геттера.setter.""")

# -------------------------------------------------------------
demo_object = DemoClass()
# Используем @some_private_property.setter
demo_object.some_private_property = 15
# Используем @property
print(demo_object.some_private_property)

line()
class User:
    PASSWORD_MIN_LEN = 5
    PASSWORD_MAX_LEN = 16

    def __init__(self, login, password, name, email, role):
        self.__validate_password(password)
        self.__login = login
        self.__password = password
        self.name = name
        self.email = email
        self.role = role

    @classmethod
    def __validate_password(cls, password):
        if not (cls.PASSWORD_MIN_LEN <= len(password) <= cls.PASSWORD_MAX_LEN):
            raise AttributeError('Password not valid')

    # Оборачиваем геттер атрибута __login декоратором @property
    # Превращаем метод в свойство, которое можно получать
    @property
    def login(self):
        return self.__login

    # Оборачиваем геттер атрибута __password декоратором @property
    # Превращаем метод в свойство, которое можно получать
    @property
    def password(self):
        return self.__password

    # Оборачиваем сеттер атрибута __login декоратором @login.setter
    # Добавляем возможность изменять свойство login, созданное ранее
    @login.setter
    def login(self, login):
        self.__login = login

    # Оборачиваем сеттер атрибута __password декоратором @password.setter
    # Добавляем возможность изменять свойство password, созданное ранее
    @password.setter
    def password(self, password):
        self.__validate_password(password)
        self.__password = password

u1 = User("JohnD", "majesk123", "John Doe", "john.doe@example.com", 'TechLead')

# Используются методы с декоратором @property
print(u1.login, u1.password)
# Используется метод с декоратором  @login.setter
u1.login = 'JohnDaveric'
# Используется метод с декоратором  @password.setter
u1.password = 'Aakj12_123qsfS'

# JohnD majesk123



















