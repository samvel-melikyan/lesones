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

print("---------------split()-----------------")

print("А роза упала на лапу Азора".split())
print("Разобьём по букве А, например")
print("А роза упала на лапу Азора".split('а'))
print("---------------strip()-----------------")
print("Это метод strip() («раздеть», по сути — «скинуть лишнее»):")
print( "\t  \n  строка с ерундой по краям   \t  \n\n".strip())
print("можно передать в него последовательность любых символов, которую он уберёт. ")
print("авбвааббв Три слона на перепутье бббаааввв".strip("абв"))

print("авбвааббв Три слона на баобабе бббаааввв".removeprefix("абв"))
print("авбвааббв Три слона на баобабе бббаааввв".removeprefix("авб"))
print("авбвааббв Три слона на баобабе бббаааввв".removesuffix("ааввв"))

print("пРивЕт от пАдоНкаФФ".lower())
print("А роза упала на лапу Азора".lower().split("а"))
print("---------------casefold()-----------------")

print("Он возвращает все символы Юникода в виде, подходящем для сравнения, и это не всегда просто маленькие буквы. Например, буква немецкого алфавита ẞ (читается как «эс цет»), не имеющая отдельного строчного написания, превращается согласно правилам языка в ss")
print("а" == "А".casefold())
print( "Фраза с БОЛЬШИМИ буквами".casefold())
print("Отдай мой пирожок!".upper())

print("---------------replace()-----------------")
print("Он позволяет заменить все вхождения указанной строки на любую другую:")
print( "У коня четыре ноги, а у машины - четыре колеса".replace("четыре", "4"))
print("----------------------------------------")

text = "А роза упала на лапу Азора"
prepared_text = text.casefold().replace(' ', '')
print(prepared_text == prepared_text[::-1])
enfdprint("---------------join()-----------------")

splitted = "Вася нехороший человек занял три рубля и отказывается отдавать!".split()
print(splitted)
print(", блин, ".join(splitted))
print("connect's after every element in the list (array) and turn's into a string")

print("HW-----------")

text = "Три утёнка по три раза тёрли лапки потрёпанными мочалками и крякали друг другу: „смотри, мои лапки чище твоих!“ Смотри, утёнок, насквозь не протри!"
substring = "тр"
print(len(text.casefold().split(substring)), " : ==> ", text.split(substring))
print(string.casefold().count(substring.casefold()))
print("HW-----------")

text = "--+-- Запись номер 1 --+--"
print(text[:-5])
print(text.removesuffix("--+--"))
print("HW-----------")

text = ["Да чтоб тебя таращило!", "Где мои деньги???", "Тестовый текст 3(!)", "(Что бы это ни значило :)", "!!!Куда смотрит правительство???"]
for i in text:
    print(i.rstrip("!().?"))
print("---------------'%s ' %'replacement'()-----------------")

print("Мы видим, что в исходной строке — она называется «шаблон» — присутствует конструкция %s. Встречая её,"
      " интерпретатор понимает, что на это место надо вставить что-то другое. И это что-то указывается после самой строки вместе с символом %.")
print('"%s Доу женат на Маргарет из семьи Кэссиди." % "Джон"')
print("%s Доу женат на Маргарет из семьи Кэссиди." % "Джон")
print("-----------")
print('"Пицца %s лучше, чем пицца %s!" % ("Дядя Дональд", "Мама Смит")')
print("Пицца %s лучше, чем пицца %s!" % ("Дядя Дональд", "Мама Смит"))
print("-----------")

print("При этом символ после % внутри строки имеет значение — он подсказывает "
      "интерпретатору, переменная какого типа сюда будет вставлена. Например, s означает строку, а d — число:")
print('"Вчера велосипедист %s проехал %d километров." % ("Вася", 50)')
print("Вчера велосипедист %s проехал %d километров." % ("Вася", 50))
print("---------------format()-----------------")
print('"Пробег автомобиля с госномером {} составляет {} километров.".format("Л666АЙ77", 30000)')
print("Пробег автомобиля с госномером {} составляет {} километров.".format("Л666АЙ77", 30000))
print("-----------  using numbers for each of them")

print('"A {1} has {0} legs and a {2} has {0} legs. So what''s the difference between a {1} and a {2}?".format(4, "cat", "dog")')
print("A {1} has {0} legs and a {2} has {0} legs. So what's the difference between a {1} and a {2}?".format(4, "cat", "dog"))

print("----------- as arguments using names for each of them")
print('"A {animal1} has {number} legs and a {animal2} has {number} legs. So what''s the difference between a {animal1} and a {animal2}?".format(animal1="cat", animal2="dog", number=4)')
print("A {animal1} has {number} legs and a {animal2} has {number} legs. So what's the difference between a {animal1} and a {animal2}?".format(animal1="cat", animal2="dog", number=4))

