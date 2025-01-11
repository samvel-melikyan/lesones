print("Словарь — это неупорядоченная структура данных, элементами которой являются пары ключ:значение.")
print("-----------------------------------------------------------------------------------------------")
# создаем словарь
translator = {'bug': 'ошибка', 'function': 'функция', 'approve': 'согласовать'}
# выводим словарь в консоль
print(translator)
# ключи словаря - метод keys()
print(f'Ключи словаря: {translator.keys()}')
# значения словаря - метод values()
print(f'Значения словаря: {translator.values()}')
# пары ключ:значение - метод items()
print(f'Пары ключ:значение словаря: {translator.items()}')
print()
print("Adding a new word in the dictinary-----------------------------")
# добавляем новую запись в словарь
translator['tester'] = 'тестировщик'
print(f'Словарь с новой записью: {translator}')
# редактируем запись в словаре
translator['tester'] = 'тестер'
print(f'Словарь с отредактированной записью: {translator}')
print()
print("Чтобы удалить запись из словаря, используйте метод >del<, который удаляет элемент словаря по его ключу:")
# удаляем элемент словаря с ключом bug
del translator['bug']
# выводим полученный словарь
print(f'Полученный словарь: {translator}')
print("----------------pop()---------------")
# удаляем элемент словаря с ключом function и выводим его
print(translator.pop('function'))
# выводим полученный словарь
print(f'Полученный словарь: {translator}')
print()
for key, value in translator.items():
            # выводим пары ключ - значение
            print(f'{key} - {value}')

print(translator.keys())
print(translator.values())
print(translator.pop('approve'))
print(translator.keys())
print(translator.values())










































