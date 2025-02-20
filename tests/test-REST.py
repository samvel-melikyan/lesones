import requests
from Tools.scripts.highlight import ansi_highlight

from functions.functions import *
new_section("REST")
line("requests")
print("res = requests.get(url, headers=headers, params=params)")
print("""
    res.status_code — код состояния ответа,
    res.text — текстовые данные ответа от сервера,
    res.json() — преобразование полученных текстовых данных в формат json.
""")

res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'}, headers={'accept': 'application/json'})

print("Status Code:", res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

print("""
if 'application/json' in response.headers['Content-Type']:
    response.json()
else:
    response.text""")
short_line("POST")
print("""
Используется для отправки любых данных на сервер для их обработки или сохранения в базу данных.""")
print("res = requests.post(url, headers=headers, data=data)")
print("""
data — это данные, отправляемые на сервер в теле запроса. Передаются в формате словаря data = {‘key1’: ‘value1’, ‘key2’: ‘value2’}.""")
short_line("DELETE")
print("""
Используется для  удаления какого-либо объекта данных на сервере. Для этого в качестве параметров запроса также обязательно передаётся url-адрес, 
на который делается запрос. В зависимости от того, как сервер читает входящий запрос, соответственно передаются и остальные параметры.""")
print("res = requests.delete(url, **kwargs)")
short_line("PUT")
print("""
Используется для изменения данных на сервере. В качестве параметров также принимает url и данные data для внесения изменений. """)
print("res = requests.put(url, data=data)")