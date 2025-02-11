from functions.functions import *
import json

new_section("JSON")
print("import json")
import json
line("transfer to dict")
short_line("json.load()")
# открываем файл в режиме чтения
with open("translator.json", "r") as my_file:
    translator_json = my_file.read()
# преобразовываем строку json в словарь
translator = json.loads(translator_json)
print(type(translator))

with open("translator.json", "r") as my_file:
# считываем информацию из файла и преобразовываем строку json в словарь
    translator = json.load(my_file)

print(translator)

print("Если же, наоборот, нужно сохранить словарь в файл в формате JSON, используют метод json.dumps:")
print("""translator = {
'bug':'ошибка',
'function':'функция',
'approve':'согласовать'
}
# преобразовываем словарь в json
translator_json = json.dumps(translator)
# записываем полученную строку в файл
with open("translator.json", "w") as my_file:
    my_file.write(translator_json)
    """)
translator = {
'bug':'ошибка',
'function':'функция',
'approve':'согласовать'
}
# преобразовываем словарь в json
translator_json = json.dumps(translator)
# записываем полученную строку в файл
with open("translator.json", "w") as my_file:
    my_file.write(translator_json)


print("Еще один способ записи в файл JSON объекта — использовать метод json.dump")

print("""with open("translator.json", "w") as my_file:
# преобразовываем словарь в json и записываем в файл
    json.dump(translator, my_file)
    """)
with open("translator.json", "w") as my_file:
# преобразовываем словарь в json и записываем в файл
    json.dump(translator, my_file)

line()
print("task")
data = {
'translator' :
    {
    'bugs':'ошибка',
    'function':'функция',
    'approve':'согласовать'
    },
1:'int key',
'set':(0, 1, 2, 3),
'empty value':None
}
json_data = json.dumps(data)
with open("data.json", 'w') as my_file:
    my_file.write(json_data)

with open("data.json", "r") as my_file:
    json_data_from_file = json.load(my_file)

print(json_data_from_file)







