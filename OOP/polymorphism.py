from functions.functions import *

new_section("Polymorphism")
print("""
Это и есть полиморфизм — мы имеем один и тот же интерфейс (например: оператор +), однако реализации у этого интерфейса разные.

Строго говоря, полиморфизм в Python бывает двух видов:

    полиморфизм в функциях;
    полиморфизм в классах.
""")

line("полиморфизм в функциях")

class PathHolder:
   def __init__(self, paths):
       self.paths = paths

   def __len__(self):
       return len(self.paths)

p1 = PathHolder(['./datapath1', './datapath2', './datapath3'])
print(len(p1))

line("Полиморфизм в классах")

print("""
savings_account1 = SavingsAccount("SAV-001", 0.05, 'EUR')
savings_account2 = SavingsAccount("SAV-002", 0.07)
savings_account3 = SavingsAccount("SAV-003", 0.1, 'RUB')
checking_account1 = CheckingAccount("CHK-001", 2.50)

# Поменяем их в контейнер -- список
accounts = [savings_account1, savings_account2, savings_account3, checking_account1]
for account in accounts:
    account.display_info()      
    # it is same interface (method (display_info()) in this case with the same name) we are using but different classes  // Polymorphism in classes
    """)

line("Абстрактные методы")

print("""
class InvestmentAccount(Account):
    def __init__(self, account_number, investment_type, currency='USD'):
        super().__init__(account_number, currency)
        self.investment_type = investment_type
        
investment_account = InvestmentAccount("INV-001", "Stocks")
investment_account.display_info()

# AttributeError: 'InvestmentAccount' object has no attribute 'display_info'

-------------------------------------------------------
 У разработчиков на Python есть для этого специальное соглашение. Для того, чтобы показать, 
 что метод должен быть обязательно определён в дочернем классе, нужно объявить обязательный метод в 
 базовом классе и в нём вызывать ошибку NotImplementedError. Это специальный тип исключений, который указывает 
 читателю вашего кода, что в базовом классе отсутствует реализация какого-то метода, хотя этот метод является 
 обязательным для работы дочерних классов.

Давайте добавим в базовый класс Account реализацию метода display_info() так, чтобы при его вызове поднималась ошибка:
       
       

    def display_info(self):
        raise NotImplementedError(f'Method display_info not implemented in {self.__class__}')
        
Проверим, что теперь при попытке вызвать метод display_info() от имени объекта класса InvestmentAccount наш код упадёт с нужной нам ошибкой:
-----------------------------------------------------------------------------------------
investment_account = InvestmentAccount("INV-001", "Stocks")
investment_account.display_info()

# NotImplementedError: Method display_info not implemented in <class '__main__.InvestmentAccount'>""")

new_section("abstract methods")
print("""Методы, которые определены в базовом классе, но не имеют там собственной реализации и 
должны быть обязательно переопределены в дочернем, называются абстрактными (abstract method).""")

new_section("abstract classes")
print("""Класс, который не содержит всех реализаций методов, необходимых 
для полной работы, называется абстрактным классом (abstract class).""")



# Объявляем базовый класс
class Account:
    # Добавили атрибут уровня класса
    withdrawal_limit = 1000

    # Добавили инициализатор в базовый класс
    def __init__(self, account_number, currency='USD'):
        self.account_number = account_number
        self.balance = 0
        self.currency = currency

    # Выносим общие методы в базовый класс
    def deposit(self, amount):
        # Внесение депозита на счёт
        self.balance += amount

    def withdraw(self, amount):
        # Добавили ограничение на снятие
        if amount > self.withdrawal_limit:
            print("Withdrawal limit exceeded")
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display_info(self):
        raise NotImplementedError(f'Method display_info not implemented in {self.__class__}')

# Объявляем дочерний класс, наследуемый от базового
class SavingsAccount(Account):
    def __init__(self, account_number, interest_rate, currency='USD'):
        super().__init__(account_number, currency)
        # Инициализация объекта сберегательного счёта
        self.account_number = account_number
        self.balance = 0
        self.interest_rate = interest_rate
        self.currency = currency

    def calculate_interest(self):
        # Расчёт и начисление процентов на остаток по счёту
        interest = self.balance * self.interest_rate
        self.balance += interest

    def display_info(self):
        print("Savings account №{}, balance: {} {}, interest rate: {}".format(
            self.account_number, self.balance,
            self.currency, self.interest_rate))

class CheckingAccount(Account):
    def __init__(self, account_number, transaction_fee, currency='USD'):
        # Вызываем инициализатор класса-родителя при помощи super()
        super().__init__(account_number, currency)
        self.transaction_fee = transaction_fee

    def deduct_transaction_fee(self):
        # Вычет комиссии за транзакцию
        self.balance -= self.transaction_fee

    # Переопределили метод базового класса в дочернем
    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print("Withdrawal limit exceeded")
        # Проверяем наличие достаточного количества денег на счёте
        elif self.balance >= amount + self.transaction_fee:
            self.balance -= amount
            # Снимаем комиссию за снятие
            self.balance -= self.transaction_fee
        else:
            print("Insufficient funds")

    def display_info(self):
        print("Checking account №{}, balance: {}{}, transaction fee: {}".format(
            self.account_number, self.balance,
            self.currency, self.transaction_fee))

class InvestmentAccount(Account):
    def __init__(self, account_number, investment_type, currency='USD'):
        super().__init__(account_number, currency)
        self.investment_type = investment_type



# ---------------------------------------------------------------------------------------------------
# Создаем экземпляры классов
savings_account1 = SavingsAccount("SAV-001", 0.05, 'EUR')
savings_account2 = SavingsAccount("SAV-002", 0.07)
savings_account3 = SavingsAccount("SAV-003", 0.1, 'RUB')
checking_account1 = CheckingAccount("CHK-001", 2.50)

# Поменяем их в контейнер -- список
accounts = [savings_account1, savings_account2, savings_account3, checking_account1]
for account in accounts:
    account.display_info()      # it is same interface (method in this case with the same name) we are using but different classes  // Polymorphism in classes













