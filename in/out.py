print("--------------------input()--------------------------")
data = input("input()>1 ")
print(data * 5)

print("--------------------sys--------------------------")

import sys

data = sys.stdin.readline()
print(data * 5)

name = input("Введите ваше имя: >3 ")
print(f"Приветствую, {name}!")

digit = input("Введите число: >4 ")
print(digit * 10)

digit = input("Введите число: >5 ")
print(int(digit) / 10)

print("--------HW----------")
data = input("Type your IP address |")
if len(data) < 7 or data.count(".") != 3:
    data = input("IP address is not valid!\nPlease type a valid IP address;\nFormat: xxx.xxx.xxx.xxx\n>>>")

data = data.replace(" ", "")
data = data.replace(".", "_")

print(data)
# print('ip = ip.split(',".",')\nprint('"_"'.join(ip))')
print("------------------------------")
import sys

sys.stdout.write("Привет, кожаный мешок!\n")
print("it is the same as a print() method")
print("------------------end=''------------")

print("Эта строка плавно переходит", end="")
print("| в следующую строку.")

print(1, 2, 3, 4, 5, 6, 7, sep="-")


print("--------HW----------")
print(input("type a number |"),input("type a number |"),input("type a number |"),input("type a number |"), sep="-" )
print("--------HW----------")
invitation = "Please write something here -> "
data = input(invitation) + "#"
print(data * 3)

from decimal import Decimal

print("--------HW----------")
print(round(0.33 * 18.42, 4))
print(Decimal("0.33") * Decimal("18.42"))

print(f"{5.724609312:.280f}")
name="Саутуарк"
print("Сегодня утром %i автомобиля и %i омнибуса проехали по мосту %s." %(4, 4, "Саутуарк"))
b = "Сегодня утром {count} автомобиля и {count} омнибуса проехали по мосту {name}.".format(count=4, name=name)
c = f"Сегодня утром {4} автомобиля и {4} омнибуса проехали по мосту {name}."



print("--------HW----------")
tracks = input("number of trucks was ...")
bags = input("number of bags was ...")
factor = int(input("number to factor was ..."))

text = f"За прошедший месяц было продано {bags} мешков картошки и {tracks} тракторов"
print((text + "\n") * factor)



