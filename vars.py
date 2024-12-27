import math
import sys
from decimal import Decimal

a,b,c,d = 1,2,3,4
print(a,b,c,d)

m = 1,2,3,4   # =(1, 2, 3, 4)
print(m);print("is m")
print(m + (1,2,3))  # jsut concatinate as a strings
a = 10 + 17
print(type(a)," - ", a)
a = 4 / 4
print(type(a)," - ", a)
a = 15 / 4
print(type(a)," - ", a)
a = 15 // 4
print(type(a)," - ", a)
a = 15 % 4
print(type(a)," - ", a)  # only the rest remained
print("-------------------------------")
print()
print(2 ** 8)
print(666 ** 999)
print("The length of the string that has a count of symbols in the 666**999: -> ", len(str(666 ** 999)))
# print(len(str(66666 ** 999)))
# a = 7777777 ** 999999
# print(type(a)," - ", a)
a = -66666 ** 99
print(a)
print(666.33 ** 109)
print("-------------------------------")
print()
a = math.sqrt(64)
print("square root - ",a, " -> " , type(a))
print(math.sqrt(218))
print("-------------------------------")
r = 10
print(2 * math.pi * r)
print(True == 1)
print(True == 0)
a = 10
if a >= 10:
    b = 1
else:
    b = 0
print(b)
print("-------------------------------")
print(2.79 > Decimal("2.79"))  # Про Decimal и особенности чисел с плавающей точкой будет рассказано ниже.
print(33 < 33.1)
print(0b100 > math.pi)
print(40.0 == 40)
print(12 >= 0xc)
print(55 != 0o102)
print("-------------------------------")
print(10 + 5 * 6 < 50)
print("-------------------------------")
print(5 + (10 > 5) * 3)   # True = 1
print(5 + (10 < 5) * 3)   # False = 0
print("-------------------------------")
print(3 * 4 - 8 * 2 * (7 - 5.0) + 2)
print((10 + 2) / 3 * (15.0 == 15) - 4)