from functions.functions import *
new_section("inheritance")

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

# Объявляем еще один дочерний класс, наследуемый от базового
class CheckingAccount(Account):
    def __init__(self, account_number, transaction_fee, currency='USD'):
        super().__init__(account_number, currency)
        self.account_number = account_number
        self.balance = 0
        self.transaction_fee = transaction_fee
        self.currency = currency


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

# -------------------------------------------------------------------------------------------------------------
# Создание экземпляров класса
savings_account = SavingsAccount(account_number="SAV-001",
                                 interest_rate=0.05,
                                 currency='USD')



# Использование методов класса
savings_account.deposit(1000)               # Внесение депозита на счёт
savings_account.calculate_interest()        # Расчёт и начисление процентов

# Выводим информацию о сберегательном счёте
print("Savings account №{}, balance: {}, interest rate: {}".format(
    savings_account.account_number,
    savings_account.balance,
    savings_account.interest_rate
))

checking_account = CheckingAccount(account_number="CHK-001",
                                   transaction_fee=2.50,
                                   currency='USD')

# Использование методов класса
checking_account.deposit(1000)              # Внесение депозита на счёт
checking_account.withdraw(500)              # Снятие суммы со счёта
checking_account.deduct_transaction_fee()   # Снятие комиcсии

print("Checking account №{}, balance: {}, transaction fee: {}".format(
    checking_account.account_number,
    checking_account.balance,
    checking_account.transaction_fee
))

# Создание экземпляра класса
# Создание экземпляров класса
checking_account = CheckingAccount(account_number="CHK-001",
                                   transaction_fee=2.50,
                                   currency='USD')

# Использование методов класса
checking_account.deposit(1000)              # Внесение депозита на счёт
checking_account.withdraw(500)              # Снятие суммы со счёта
checking_account.deduct_transaction_fee()   # Снятие комиcсии

print("Checking account №{}, balance: {}, transaction fee: {}".format(
    checking_account.account_number,
    checking_account.balance,
    checking_account.transaction_fee
))
# ---------------------------------------------------------------------------------
line()


class SoundEquipment:
    def switch_on(self):
        self.state = True

    def switch_off(self):
        self.state = False


class Microphone(SoundEquipment):
    def __init__(self, volume: int, state: bool):
        if volume <= 10 and volume >= 0:
            self.volume = volume
        elif volume > 10:
            self.volume = 10
        elif volume < 0:
            self.volume = 0
        self.state = state

    def adjust_volume(self, vol):
        volume = self.volume + vol
        if volume <= 10 and volume >= 0:
            self.volume = volume
        elif volume > 10:
            self.volume = 10
        elif volume < 0:
            self.volume = 0
        print(f"Volume is now {self.volume}")


class Speaker(SoundEquipment):
    def __init__(self, bass: int, state: bool):
        if bass <= 10 and bass >= 0:
            self.bass = bass
        elif bass > 10:
            self.bass = 10
        elif bass < 0:
            self.bass = 0
        self.state = state

    def adjust_bass(self, bass_vol):
        bass = self.bass + bass_vol
        if bass <= 10 and bass >= 0:
            self.bass = bass
        elif bass > 10:
            self.bass = 10
        elif bass < 0:
            self.bass = 0
        print(f"Volume is now {self.bass}")


mic = Microphone(volume=5, state=True)
# mic.adjust_volume(7)

sp = Speaker(7, False)
# sp.adjust_bass(8)

























