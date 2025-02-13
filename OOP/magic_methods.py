from lesones.functions.functions import *

new_section("Magic Methods")
line("__call__()")
print("""
Определить, что именно должен делать объект при его вызове, 
поможет «магический» метод__call__(), в котором и определяется то, как должен вести себя 
объект или что он должен возвращать, так, например, если не переопределять «магический» 
метод __call__() у класса, то он возвращает свой экземпляр.""")

print("""
Метод__init__() можно реализовать следующим образом:

class User:
   # Объявляем инициализатор
   def __init__(self, login, password, name, email, role):
       self.login = login
       self.password = password
       self.name = name
       self.email = email
	  self.role = role

   def create_task(self, project, description):
       project.add_task(self, description)""")
short_line()

class User:
    # Объявляем инициализатор
    # def __init__(self, login, password, name, email, role):
    def __init__(self, login, password, name, email=None, role=None):
        self.login = login
        self.password = password
        self.name = name
        self.email = email
        self.role = role


def create_task(self, project, description):
    project.add_task(self, description)


user1 = User("JohnD", "mloz512qyt", "John Doe", "john.doe@example.com", 'TechLead')
print(user1.__dict__)

print("\n> In order to don't get an error for passing not all arguments, we'll make some arguments a key arguments")
print("""
class User:
   def __init__(self, login, password, name, email=None, role=None):
       self.login = login
       self.password = password
       self.name = name
       self.email = email
       self.role = role
       
user1 = User("JohnD", "mloz512qyt", "John Doe")
print(user1.__dict__)
""")
user1 = User("JohnD", "mloz512qyt", "John Doe")
print(user1.__dict__)


print("""
Стоит упомянуть, что метод __init__() автоматически вызывается при создании 
экземпляра класса, но он вызывается не самым первым. Перед ним стоит вызов «магического» 
метода __new__(), который фактически формирует новый объект.""")


