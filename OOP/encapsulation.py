from lesones.functions.functions import *

new_section("encapsulation")

class User:
    def __init__(self, login, password, name, email, role):
        self.login = login
        self.password = password
        ...

# u1 = User("JohnD", "mloz512qyt", "John Doe", "john.doe@example.com", 'TechLead')

# print(u1.login, u1.password)
# print(getattr(u1, 'login'), getattr(u1, 'password'))
# print(u1.__dict__['login'], u1.__dict__['password'])

# u1 = User("JohnD", "mloz512qyt", "John Doe", "john.doe@example.com", 'TechLead')
# print(u1.login, u1.password)

# u1.login = 'JaneJr'
# u1.password = 'asfkno1Q'
# print(u1.login, u1.password)

print("""Инкапсуляция — это принцип объектно-ориентированного программирования, который позволяет 
скрыть детали реализации объекта от внешнего мира и предоставить интерфейс для взаимодействия с ним.""")

line("privacy level")
print("""Вместо ключевых слов в Python используется специальное соглашение, в соответствии с 
которым уровни доступа устанавливаются с помощью нижних подчеркиваний ('_') перед атрибутами:""")

print("""
(0x _'s) public - self.var_name = value that everywhere visible and accessible from everywhere
(1x _'s) protected - self._var_name = value that visible and accessible inside the class and its children 
(2x _'s) private - self.__var.name = value that visible and accessible only inside the class 

Аналогичное соглашение об уровне доступа к атрибутам работает и для методов класса. То есть имена 
защищённых методов начинаются с _, например, _predict(), а имена приватных методов с __, например, __predict().
""")

class User:
    def __init__(self, login, password, name, email, role):
        # Меняем уровень доступа атрибутов login и password на защищённый
        self._login = login
        self._password = password
        ...

# u1 = User("JohnD", "mloz512qyt", "John Doe", "john.doe@example.com", 'TechLead')
print("""
print(u1.login, u1.password)
# AttributeError: 'User' object has no attribute 'login'. Did you mean: '_login'?
""")
# print(u1._login, u1._password)   # works fine

print("""
class User:
    def __init__(self, login, password, name, email, role):
        # Меняем уровень доступа атрибутов login и password на приватный
        self.__login = login
        self.__password = password
        ...

u1 = User("JohnD", "mloz512qyt", "John Doe", "john.doe@example.com", 'TechLead')
print(u1.__login, u1.__password)

# AttributeError: 'User' object has no attribute '__login'

Теперь уже интерпретатор не даёт нам обратиться к этим атрибутам 
и мы можем быть спокойны и уверены в том, что теперь никто не сможет к ним обращаться.
""")
line("setter and getter")

class User:

    def __init__(self, login, password, name, email, role):
        self.__login = login
        self.__password = password
        ...

    def get_login_password(self):
        return self.__login, self.__password

    def set_login_password(self, login, password):
        self.__login = login
        self.__password = password


# u1 = User("JohnD", "mloz512qyt", "John Doe", "john.doe@example.com", 'TechLead')
# print(u1.get_login_password())

line()

class User:
    # Задаём атрибуты на уровне класса
    PASSWORD_MIN_LEN = 5
    PASSWORD_MAX_LEN = 16

    def __init__(self, login, password, name, email, role):
        self.__login = login
        self.__password = password
        ...

    def get_login_password(self):
        return self.__login, self.__password

    # Определяем метод для валидации пароля
    # Method decorator
    @classmethod
    def __validate_password(cls, password):
        if not(cls.PASSWORD_MIN_LEN <= len(password) <= cls.PASSWORD_MAX_LEN and type(password) == str):
            raise AttributeError('Password not valid')

    # Меняем код для установки пароля
    def set_login_password(self, login, password):
        if not self.__validate_password(password):
            raise AttributeError('Password not valid')
        self.__login = login
        self.__password = password

print("""
u1 = User("JohnD", "mloz512qyt", "John Doe", "john.doe@example.com", 'TechLead')
u1.set_login_password('JognD', 'qwe1')

# AttributeError: Password not valid""")
short_line()
print("""Мы забыли добавить проверку в инициализатор, ведь пока что никто не запретит 
нам установить неверные значения при создании экземпляра класса:

# Задаём пользователю пароль "qwe1" недопустимой длины  
u1 = User("JohnD", "qwe1", "John Doe", "john.doe@example.com", 'TechLead')
print(u1.get_login_password())

# ('JohnD', 'qwe1')""")

class User:
   PASSWORD_MIN_LEN = 5
   PASSWORD_MAX_LEN = 16

   def __init__(self, login, password, name, email, role):
       # Добавили проверку пароля в инициализатор
       # ----------------------
       self.__validate_password(password)
       # ----------------------
       self.__login = login
       self.__password = password
       ...

   def get_login_password(self):
       return self.__login, self.__password

   @classmethod
   def __validate_password(cls, password):
      if not(cls.PASSWORD_MIN_LEN <= len(password) <= cls.PASSWORD_MAX_LEN and type(password) == str):
          raise AttributeError('Password not valid')

   def set_login_password(self, login, password):
       self.__validate_password(password)
       self.__login = login
       self.__password = password

short_line(":( access to private variables and methods")
print("""
А что если попробовать обратиться к этим именам через наш экземпляр:

u1 = User("JohnD", "majesk123", "John Doe", "john.doe@example.com", 'TechLead')
print(u1._User__login, u1._User__password)

# JohnD majesk123
""")
# u1 = User("JohnD", "majesk123", "John Doe", "john.doe@example.com", 'TechLead')
# print(u1.__dir__())
# print(u1._User__login, u1._User__password)

# JohnD majesk123


print("""
К тому же никто не говорит о том, что эти условности не нужно соблюдать. 
Практическое назначение уровней доступа в Python заключается прежде всего в «понимании» вашего класса 
другим человеком, который благодаря наличию уровня доступов у атрибутов сможет понять, какими атрибутами 
в каких именно местах программы он сможет ими пользоваться.""")

line()
# --------------------------------------------------------------------------------------
class TaskList:
    def __init__(self):
        self.__task_list = []

    def __is_task_in_list(self, task):

        if task in self.__task_list:
            return True
        else:
            return False


    def add_task(self, task):
        if self.__is_task_in_list(task):
            print(f"Задача {task}  уже есть в списке")
        else:
            self.__task_list.append(task)
            print(f"Задача {task} добавлена в список")

    def remove_task(self, task_name):
        for task in self.__task_list:
            if task_name == task:
                self.__task_list.remove(task)
                print(f"Задача {task} удалена из списка")
            else:
                print(f"Задачи {task} нет в списке")


task_list = TaskList()
task_list.add_task("Task 1")
task_list.add_task("Task 2")
print(task_list._TaskList__is_task_in_list("Task 2"))





















































