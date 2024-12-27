a = "string"
b = 'string'
c = """string"""
d = '''string'''
print(a == b == c == d)
print(a is b is c is d)
a = "проприетарный"[3]
print(a)
b = 'сколопендра'[1:4]
print(b)
print(type('сколопендра'[1:4]))
print("Современное телевидение было переведено на цифровое вещание."[:23])
print("Современное телевидение было переведено на цифровое вещание."[23:])
string = "2023-02-15 14:21:46.353 ERROR message: Ай, случилася беда!"
print(string[39:])
print("--------------------------------")
print('some text message'[:])
print("просто строка"[-2])
print("просто строка"[-6:])
print("просто строка"[:-6])
print("И это просто строка"[-14:-6])
print("А это не просто строка"[6:-7])
print("--------------------------------")
print("1234567890"[::2])         # every second

#А если мы хотим из этого ряда взять только чётные, то нам надо начать с элемента с индексом 1 — с двойки. Укажем этот индекс в качестве нижней границы среза:
print("1234567890"[1::2])
print("1234567890"[1:-1:2])
print("abrvabrvabrvabrvabrvabrvabrvabrvabrvabrvabrvab"[3::4])  # каждый четвёртый, начиная с четвёртого
print('абвгдеёжзиклмнопрст')
print('абвгдеёжзиклмнопрст'[::-1])
print("--------------------------------")

string = 'abcdefghijk 1456 ahalai-mahalai! Восстань, сын трёхголового дракона!'
print(string[7:42:3])
string = string[7:43][::3] # == string[7:42:3]

print(string)
print("--------------------------------")
print("---------------search-----------")
print("---------------index()----------")
print("лебеда".index('беда'), " :   'лебеда'.index('беда')")
print("---------------find()-----------")
text = "5423534 lajksdfij;jhh абракадабра dfasdfs9d6f7686"
text = "12435514234 ERROR index: big_terrible_mistake message: Ай, случилася беда!"
template = 'message: '
# print(text.find(template))
index = text.find(template)
if index != -1:
    print(text[index + len(template):])
else:
    print("looks like index == -1")
print("* Если бы мы использовали метод index(), то при обработке строки с “абракадаброй” получили бы исключение, так как искомого слова “message” в ней нет")
print("* А при использовании find() всего лишь получаем –1.")
print("---------------in-----------------")
text = "12435514234 ERROR index: big_terrible_mistake message: Ай, случилася беда!"
if template in text:
    index = text.index(template)
    print(text[index + len(template):])

print("---------------count()-----------------", " * позволяет подсчитать, сколько раз искомое слово встречается в строке.")
print("абракадабра".count("а"))
print("---------------startswith()-----------------")
print("_name".startswith("_"))
name = "internal_attr_2"
if not name.startswith("_"):
    print(name)

print("---------------endswith()-----------------")
word = "мышь"
if word.endswith("ь"):
    print("Это существительное женского рода:", word)

print("Метод islower() проверяет, все ли символы строки являются строчными:", "is lower case")
print("Метод isupper() проверяет, все ли символы строки являются прописными:", "is upper case")
print("Метод istitle() проверяет, начинается ли строка с заглавной буквы и следуют ли за ней строчные:")
print("Метод isnumeric() проверяет, состоит ли представленная строка только из цифр:")
print("Метод isalpha() проверяет, наоборот, не содержит ли строка чего-либо помимо букв алфавита (любого):")

print("Here is the link to all methods: ","https://docs.python.org/3/library/stdtypes.html#str.isalnum")
print("HW-----------")
string = "dd"
if len(string) == 0:
    print(False)
else:
    print(string.isascii())
print("HW-----------")
string = "sidfghsdf_"
string = ""
if len(string) is 0:
    print(False)
else:
    print(string.endswith("_"))

print("HW-----------")
string = "Я типа пошёл типа вчера гулять типа вот типа ага."
print(string.count("типа"), ": հատ ՛типа՛")