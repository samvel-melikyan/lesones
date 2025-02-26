import sys
from datetime import datetime

from functions.functions import *
new_section("fixtures")
print("""
Фикстуры — это функции, выполняемые pytest до или после тестовых функций. 
Код в фикстуре может делать все, что вам необходимо: подготавливать данные для теста, настраивать 
логирование приложения и т.д. Иными словами, фикстуры обеспечивают механизм отделения непосредственно 
кода тестов от «подготовки к» и «очистке после» исполнения тестов.""")


import pytest

@pytest.fixture()
def some_data():
    return 42

def test_some_data(some_data):
    assert some_data == 42



def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print (f"\nТест шел: {end_time - start_time}")

print("""
@pytest.fixture()
def get_key():
    # переменные email и password нужно заменить своими учетными данными
    response = requests.post(url='https://petfriends.skillfactory.ru/login',
                             data={"email": email, "pass": password})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    return response.request.headers.get('Cookie')

def test_getAllPets(get_key):
    response = requests.get(url='https://petfriends.skillfactory.ru/api/pets',
                            headers={"Cookie": get_key})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'""")

line("scopes of fixtures")
print("""
@pytest.fixture(scope="class", autouse=True)

def session_fixture():
    print("\nclass fixture starts")

@pytest.fixture(scope="function", autouse=True)
def function_fixture():
    print("\nfunction fixture starts")

class TestClass23:

    def test_first(self):
        pass

def test_second(self):
    pass
    
Теперь при запуске тестов session_fixture вызовется лишь единожды, тогда как function_fixture будет вызываться перед каждым тестом.
""")

line("Фикстура request")
@pytest.fixture()
def request_fixture(request):
    print(request.fixturename)
    print(request.scope)
    print(request.function.__name__)
    print(request.cls)
    print(request.module.__name__)
    print(request.fspath)
    if request.cls:
        return f"\n У теста {request.function.__name__} класс есть\n"
    else:
        return f"\n У теста {request.function.__name__} класса нет\n"


def test_request_1(request_fixture):
    print(request_fixture)


class TestClassRequest:

    def test_request_2(self, request_fixture):
        print(request_fixture)

line("@pytest.mark фикстура")
short_line("pytest.mark.skip")
print("""
Данная фикстура помечает тест как пропущенный, то есть при запуске тест не будет выполняться. 
Например, у нас написан определенный тест на регистрацию, но мы знаем, что в приложении существует баг, 
который не собираются исправлять в ближайшее время. Такой тест имеет смысл пропускать, иначе каждый запуск 
тестов будет неудачным из-за этого теста. Простой декоратор над тестовой функцией позволит нам сделать это:

@pytest.mark.skip(reason="Баг в продукте - <ссылка>")
def test_one(): … # Это наш тест, который находит тот самый баг""")


short_line("pytest.mark.skipif")
(print("""
Фикстура делает то же самое, что и предыдущая, но мы имеем возможность управлять игнорируемыми тестами. 
Довольно простые примеры, которые хорошо иллюстрируют, как можно пользоваться такой фикстурой — это пропуск 
тестов в случае, когда версия Python ниже определенной.

""")
@pytest.mark.skipif(sys.version_info < (3, 6), reason="Тест требует python версии 3.6 или выше"))
def test_python36_and_greater():
    ...
minversion = pytest.mark.skipif(
    sys.version_info < (3, 6), reason="at least mymodule-1.1 required"
)

@minversion
def test_python36_and_greater():
    ...
short_line("pytest.mark.xfail")
(print("""
Помечает тест как падающий. Например, вы написали тест, который отлично работает на локальной машине, 
прошли код-ревью, и вот он уже оказался в ветке с остальными тестами. Однако по какой-то причине этот тест 
довольно часто завершается с ошибкой в инфраструктуре организации. Чтобы не забыть починить такой тест, 
удобно пометить его как нестабильный, используя фикстуру xfail:

""")
 @pytest.mark.xfail)
def test_flaky():
        ...

@pytest.mark.xfail(sys.platform == "win32", reason="Ошибка в системной библиотеке") # На платформе Windows ожидаем, что тест будет падать
def test_not_for_windows():
    ...

print("""
Как мы видим, для этого теста указан также reason.

Если мы хотим быть более конкретными в причинах падения, то мы можем указать такую причину в 
аргументе raises фикстуры xfail. Например, следующий тест будет помечен xfail только в том случае, 
если произойдет исключение типа RuntimeException, в противном случае тест будет выполняться как обычно 
(помечаться passed, если пройдет успешно, и failed, если пройдет неуспешно):
""")
@pytest.mark.xfail(raises=RuntimeError)
def test_x_status_runtime_only():
    ...
line("Пользовательские группы")
print("""
Этот механизм ничем не отличается от предыдущих — необходимо написать, что мы помечаем тест, и дать имя группы 
(@pytest.mark.auth). Далее необходимо в проекте создать файл pytest.ini, туда внести информацию об описанных в тестах группах. 
Давайте разберём непосредственно в коде. У нас есть четыре теста, два из них на аутентификацию пользователя, остальные два — 
это тесты мероприятий. В каждой такой группе соответственно API и UI тесты:""")

@pytest.mark.api
@pytest.mark.auth
def test_auth_api():
   pass

@pytest.mark.ui
@pytest.mark.auth
def test_auth_ui():
   pass

@pytest.mark.api
@pytest.mark.event
def test_event_api():
   pass

@pytest.mark.ui
@pytest.mark.event
def test_event_ui():
   pass

print("""В корне проекта создадим файл pytest.ini и добавим туда описание наших категорий. 
Тесты будут запускаться и без этого файла, но его наличие избавит нас от постоянных предупреждений в отчетах:\

Все, что нам осталось сделать — это научиться фильтровать такие тесты. Например, 
если нам нужно запустить только API тесты, то в консоли надо набрать:

pytest test.py -v -m "api"         # test.py замените на имя своего файла в проекте


Можно отбирать тесты по нескольким группам сразу, используя логические операторы. 
Например, если мы хотим запустить только UI тесты авторизации, то команда в консоли будет выглядеть так:

pytest test.py -v -m "ui and auth"
А если нам нужно запустить все виды тесты на модули авторизации и мероприятий, то команда для запуска будет следующая:

pytest test.py -v -m "auth or event""")

